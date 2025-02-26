from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('about/', views.about, name='about'),
	path('post/<int:post_id>/', views.full_post, name='post'),
	path('add-post/', views.add_post, name='add-post'),
	path('sign-in/', views.sign_in, name='sign-in'),
	path('category/<int:cat_id>', views.show_cat, name='category')
]