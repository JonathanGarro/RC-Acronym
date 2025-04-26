from django import forms
from .models import Acronym, Category

class AcronymForm(forms.ModelForm):
    class Meta:
        model = Acronym
        fields = ['acronym', 'definition', 'description', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class ExportForm(forms.Form):
    EXPORT_CHOICES = [
        ('all', 'All Acronyms'),
        ('user', 'My Acronyms'),
        ('category', 'By Category')
    ]
    
    export_type = forms.ChoiceField(choices=EXPORT_CHOICES, widget=forms.RadioSelect)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        export_type = cleaned_data.get("export_type")
        category = cleaned_data.get("category")
        
        if export_type == 'category' and not category:
            raise forms.ValidationError("Please select a category for category export.")
        
        return cleaned_data
