from django.urls import path
from . import views

app_name = 'defo_store'
urlpatterns = [
    path('chemical_list/', views.ChemicalListView.as_view(), name='chemical_list'),
]
