from django import template 
register = template.Library()
from ..models import Categoria

@register.simple_tag
def Categorias():
	return Categoria.objects.all()