from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/article_details.html"
    context_object_name = "post"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    # fields = "__all__"


class UpdaePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "blog/update_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')