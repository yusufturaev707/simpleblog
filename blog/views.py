from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', kwargs={"pk": pk}))


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(requests, cats):
    category_posts = Post.objects.filter(category__name=cats.replace('-', ' '))
    data = {
        "category_posts": category_posts,
        "cats": cats.title().replace('-', ' ')
    }
    return render(requests, "blog/category.html", context=data)

class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/article_details.html"
    context_object_name = "post"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    # fields = "__all__"


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = "blog/add_category.html"
    fields = "__all__"


class UpdaePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "blog/update_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')