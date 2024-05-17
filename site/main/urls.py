from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("news", views.news_home, name="news_home"),
    # path("news/post", views.create, name="create"),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name="news_detail"),
    path("news/<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update"),
    path("news/<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete"),
    path("news/post", views.CreateView.as_view(), name="create"),
    path("dostup", views.dostup_page, name = "dostup_page"),
]
