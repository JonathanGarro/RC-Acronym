from django.urls import path
from . import views
from .views import (
    AcronymListView,
    AcronymDetailView,
    AcronymCreateView,
    AcronymUpdateView,
    AcronymDeleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('acronyms/', AcronymListView.as_view(), name='acronym-list'),
    path('acronym/<int:pk>/', AcronymDetailView.as_view(), name='acronym-detail'),
    path('acronym/new/', AcronymCreateView.as_view(), name='acronym-create'),
    path('acronym/<int:pk>/update/', AcronymUpdateView.as_view(), name='acronym-update'),
    path('acronym/<int:pk>/delete/', AcronymDeleteView.as_view(), name='acronym-delete'),
    path('my-acronyms/', views.user_acronyms, name='user-acronyms'),
    path('export/', views.export_acronyms, name='export-acronyms'),
]
