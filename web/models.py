from django.db import models
import uuid

# Create your models here.
class flan(models.Model):
    flan_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        name = self.name
        es_privado = self.is_private
        return f'Nombre: {name} - ¿es privado?: {es_privado}'