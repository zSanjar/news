from django.views.generic import TemplateView, DetailView, ListView
from News.models import Category


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        latest_articles = Article.objects.order_by('-published_at')[:5]  # oxirgi 5 ta yangilik

        context["title"] = "News Portal | Home"
        context["categories"] = categories
        context["latest_articles"] = latest_articles
        return context


class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "News Portal | Contact Us"
        return context

