from django.template import Library
from main import views

register = Library()


@register.simple_tag()
def get_cats():
	return views.cats_db