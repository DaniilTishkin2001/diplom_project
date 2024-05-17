from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormMixin


from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView




class NewsDetailView(FormMixin,DetailView):
    model = Articles
    template_name = "main/details_view.html"
    context_object_name = "article"
    login_url = reverse_lazy("login_page")







class NewsUpdateView(LoginRequiredMixin,UpdateView):
    model = Articles
    template_name = "main/create.html"
    form_class = ArticlesForm
    login_url = reverse_lazy("login_page")


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs["instance"].author:
            return self.handle_no_permission()
        return kwargs

class NewsDeleteView(LoginRequiredMixin,DeleteView):
    model = Articles
    success_url = "/news"
    template_name = "main/news-delete.html"
    login_url = reverse_lazy("login_page")
    def form_valid(self, form):
        if self.object.author != self.request.user:
            return redirect('dostup_page')
        self.object.delete()
        success_url = reverse_lazy('news_home')

        return HttpResponseRedirect(success_url)


data = {
    "title": "Главная страница",
}

def index(request):
    return render(request,"main/index.html", data)

def about(request):
    return render(request, "main/about.html")

def news_home(request):
    news = Articles.objects.order_by("-date")
    info = {
        "news": news
    }
    return render(request,"main/news_home.html", info)





class CreateView(CreateView):
    model = Articles
    template_name = "main/create.html"
    form_class = ArticlesForm
    login_url = reverse_lazy("login_page")


    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def dostup_page(request):
    return render(request,"main/dostup.html")