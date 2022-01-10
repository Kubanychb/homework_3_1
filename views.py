from django.http import HttpResponse
from django.shortcuts import render
from . import models


def book(request):
    return HttpResponse('book')


def book_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})
