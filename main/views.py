from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

menu = [
	{'title': "About", 'url': 'about'},
	{'title': "Add post", 'url': 'add-post'},
	{'title': "Sign in", 'url': 'sign-in'},
]

data_db = [
	{'id': 1, 'title': "Angelina Jolie", 'content': "Biography of Angelina Jolie", 'is_public': True},
	{'id': 2, 'title': "Margo Robbie", 'content': "Biography of Margo Robbie", 'is_public': True},
	{'id': 3, 'title': "Julia Roberts", 'content': "Biography of Julia Roberts", 'is_public': True},
]

cats_db = [
	{'id': 1, 'name': 'Actresses'},
	{'id': 2, 'name': 'Singers'},
	{'id': 3, 'name': 'Athletes'},
]


def index(request, cat_id=None):
	data = {
		'title': "Home",
		'menu': menu,
		'posts': data_db,
		'cat_id': cat_id,
	}
	return render(request, 'main/index.html', context=data)


def full_post(request, post_id):
	return HttpResponse(f"<h2>This is post number {post_id}</h2>")


def about(request):
	return render(request, 'main/about.html', {'title': "About", 'menu': menu})


def add_post(request):
	return HttpResponse("<b>THE PAGE YET DOESN'T WORK</b>")


def sign_in(request):
	return HttpResponse("YOU ARE GAY")


def show_cat(request, cat_id: int):
	return index(request, cat_id=cat_id)


def page_not_found(request, exception):
	return HttpResponseNotFound("<h1>This page doesn't exist</h1><p>idi nahui</p>")