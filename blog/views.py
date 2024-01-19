
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView

from .models import Post

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-Date"]
    context_object_name = "posts"

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-Date"]
    context_object_name = "all_posts"

class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        return context