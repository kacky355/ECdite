from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

import os
from .models import(
    Chemicals,
)

class ChemicalListView(LoginRequiredMixin,ListView):
    model = Chemicals
    template_name = os.path.join('defo_store','chemical_list.html')
    
    # リストの絞り込み機能
    def get_queryset(self):
        query = super().get_queryset()
        chemical_type = self.request.GET.get('chemical_type',None)
        chemical_name = self.request.GET.get('chemical_name',None)
        chemical_cas = self.request.GET.get('chemical_cas',None)
        if chemical_type:
            query = query.filter(
                #__nameでChemicalTypeのnameフィールドを指定
                chemical_type__name=chemical_type,
            )
        if chemical_name:
            query = query.filter(
                name=chemical_name,
            )
        if chemical_cas:
            query = query.filter(
                cas=chemical_cas,
            )
        return query
    
    # 絞り込み機能のフォームが検索後に空になるのを防ぐ
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chemical_type'] = self.request.GET.get('chemical_type','')
        context['chemical_name'] = self.request.GET.get('chemical_name','')
        context['chemical_cas'] = self.request.GET.get('chemical_cas','')
        return context
