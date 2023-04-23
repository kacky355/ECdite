from django.contrib import admin
from .models import(
    ChemicalTypes,Manufactures,
    Chemicals,ChemicalPictures,
)

admin.site.register(
    [ChemicalTypes,Manufactures,Chemicals,ChemicalPictures]
)