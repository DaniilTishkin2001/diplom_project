from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("news", views.NewsView.as_view(), name="news_home"),
    path("news/<int:pk>", views.NewsDetailView.as_view(), name="news_detail"),
    path("news/<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update"),
    path("news/<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete"),
    path("news/post", views.CreateView.as_view(), name="create"),
    path("dostup", views.dostup_page, name = "dostup_page"),

]

