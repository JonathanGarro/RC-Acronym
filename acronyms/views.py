from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Acronym, Category
from .forms import AcronymForm, ExportForm
from django.contrib import messages
from django.db.models import Q
import csv
from django.http import HttpResponse
from django.urls import reverse_lazy

def home(request):
    """Home page view - includes search functionality"""
    query = request.GET.get('q')
    
    if query:
        acronyms = Acronym.objects.filter(
            Q(acronym__icontains=query) | 
            Q(definition__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        acronyms = Acronym.objects.all()[:10]  # Show only 10 most recent by default
    
    categories = Category.objects.all()
    
    context = {
        'acronyms': acronyms,
        'categories': categories,
        'query': query
    }
    return render(request, 'acronyms/home.html', context)

class AcronymListView(ListView):
    model = Acronym
    template_name = 'acronyms/acronym_list.html'
    context_object_name = 'acronyms'
    paginate_by = 20
    
    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            return Acronym.objects.filter(category__name=category).order_by('acronym')
        return Acronym.objects.all().order_by('acronym')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class AcronymDetailView(DetailView):
    model = Acronym

class AcronymCreateView(LoginRequiredMixin, CreateView):
    model = Acronym
    form_class = AcronymForm
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, f'Acronym has been created!')
        return super().form_valid(form)

class AcronymUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Acronym
    form_class = AcronymForm
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, f'Acronym has been updated!')
        return super().form_valid(form)
    
    def test_func(self):
        acronym = self.get_object()
        return self.request.user == acronym.created_by or self.request.user.is_staff

class AcronymDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Acronym
    success_url = reverse_lazy('acronym-list')
    
    def test_func(self):
        acronym = self.get_object()
        return self.request.user == acronym.created_by or self.request.user.is_staff
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f'Acronym has been deleted!')
        return super().delete(request, *args, **kwargs)

@login_required
def user_acronyms(request):
    acronyms = Acronym.objects.filter(created_by=request.user).order_by('acronym')
    return render(request, 'acronyms/user_acronyms.html', {'acronyms': acronyms})

@login_required
def export_acronyms(request):
    if request.method == 'POST':
        form = ExportForm(request.POST)
        if form.is_valid():
            export_type = form.cleaned_data['export_type']
            
            # Determine which acronyms to export
            if export_type == 'user':
                acronyms = Acronym.objects.filter(created_by=request.user)
            elif export_type == 'category':
                category = form.cleaned_data['category']
                acronyms = Acronym.objects.filter(category=category)
            else:
                acronyms = Acronym.objects.all()
            
            # Create CSV response
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="acronyms.csv"'
            
            writer = csv.writer(response)
            writer.writerow(['Acronym', 'Definition', 'Description', 'Category'])
            
            for acronym in acronyms:
                category_name = acronym.category.name if acronym.category else ''
                writer.writerow([acronym.acronym, acronym.definition, acronym.description, category_name])
            
            return response
    else:
        form = ExportForm()
    
    return render(request, 'acronyms/export.html', {'form': form})
