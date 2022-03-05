from django.urls import path
from blog.views import HomeView, ArticleDetailView, AddPostView, UpdaePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdaePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
]