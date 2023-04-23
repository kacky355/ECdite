from django.db import models

class ChemicalTypes(models.Model):
    name = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'chemical_types'
    
    def __str__(self):
        return self.name


class Manufactures(models.Model):
    name = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'manufactures'
    
    def __str__(self):
        return self.name


class Chemicals(models.Model):
    name = models.CharField(max_length=300)
    cas = models.CharField(max_length=300)
    price = models.IntegerField()
    stock = models.IntegerField()
    chemical_type = models.ForeignKey(
        ChemicalTypes,on_delete=models.CASCADE
    )
    manufacture = models.ForeignKey(
        Manufactures,on_delete=models.CASCADE,
    )
    
    class Meta:
        db_table = 'chemicals'
    
    def __str__(self):
        return self.name


class ChemicalPictures(models.Model):
    picture = models.FileField(upload_to='chemical_pictures/')
    chemical = models.ForeignKey(
        Chemicals,on_delete=models.CASCADE
    )
    order = models.IntegerField()

    class Meta:
        db_table = 'chemical_pictures'
        ordering = ['order']
    
    def __str__(self):
        return self.chemical.name + ':' + str(self.order)