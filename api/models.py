from django.db import models

# Create your models here.

class Genero(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField( max_length=200)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ['name']

    def __str__(self):
        return self.name

class Filo(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField( max_length=200)

    class Meta:
        verbose_name = 'Filo'
        verbose_name_plural = 'Filos'
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Clase(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField( max_length=200)

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    

class Orden(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField( max_length=200)

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Familia(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField( max_length=200)

    class Meta:
        verbose_name = 'Familia'
        verbose_name_plural = 'Familias'
        ordering = ['name']
 
    def __str__(self):
        return self.name
    
class Especie(models.Model):
    nameComun=models.CharField(max_length=50)
    nameCientifico=models.CharField(max_length=50)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default="")
    id_filo = models.ForeignKey(Filo, on_delete=models.CASCADE , default="")
    id_clase = models.ForeignKey(Clase, on_delete=models.CASCADE, default="")
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE, default="")
    id_familia = models.ForeignKey(Familia, on_delete=models.CASCADE, default="")
    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'
        ordering = ['nameComun']
    def __str__(self):
        return self.nameCientifico

class Pais(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['name']
 
    def __str__(self):
        return self.name

class Departamento(models.Model):
    name=models.CharField(max_length=50)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default="")

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['name']
 
    def __str__(self):
        return self.name

class Ciudad(models.Model):
    name=models.CharField(max_length=50)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, default="", unique=True)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['name']
 
    def __str__(self):
        return self.name

class Lugar(models.Model):
    name=models.CharField(max_length=50)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, default="", unique=True)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        ordering = ['name']
 
    def __str__(self):
        return self.name

class Avistamiento(models.Model):
    name=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    nota=models.CharField(max_length=200)
    latitud=models.CharField(max_length=50)
    longitud=models.CharField(max_length=50)
    id_lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE, default="")
    id_especie = models.ForeignKey(Especie, on_delete=models.CASCADE , default="")
    class Meta:
        verbose_name = 'Avistamiento'
        verbose_name_plural = 'Avistamientos'
        ordering = ['name']
    def __str__(self):
        return self.name
    