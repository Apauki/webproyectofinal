from django.db import models

# Create your models here.
class TipoMenu(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tipo de menú")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "tipo de menu"
        verbose_name_plural = "tipos de menú"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Menu(models.Model):
    tipoMenu = models.ManyToManyField(TipoMenu, verbose_name="Tipo de menú", null=True, blank=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="menu")
    title = models.CharField(max_length=100, verbose_name="Título")
    price = models.DecimalField(decimal_places=2, max_digits=4,verbose_name="Precio")
    reviews = models.SmallIntegerField(verbose_name="Número de reseñas")
    pointReviews = models.CharField(max_length=5, verbose_name="Puntuación (/5)")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "menu"
        verbose_name_plural = "menús"
        ordering = ['-created']

    def __str__(self):
        return self.title
        