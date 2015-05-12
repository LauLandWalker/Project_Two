from django.shortcuts import render
from django.views.generic import ListView
from blog_app import models


class BlogIndex(ListView):
    queryset = models.Entry.objects.published()
    template_name = 'blog_app/home.html'
    paginate_by = 2
    context_object_name = 'blog_entries'
