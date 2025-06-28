from django.views.generic import TemplateView, DetailView, ListView
from news.models import Category, Article


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


class ArticlesListView(ListView):
    model = Article
    template_name = "articles_list.html"
    context_object_name = "articles"
    paginate_by = 10  # sahifalash uchun, har sahifada 10 ta maqola

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "News Portal | Articles"
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"News Portal | {self.object.title}"
        return context


class CategoryArticlesView(ListView):
    model = Article
    template_name = "category_articles.html"
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        category_slug = self.kwargs.get("slug")
        return Article.objects.filter(category__slug=category_slug).order_by("-published_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get("slug")
        category = Category.objects.filter(slug=category_slug).first()
        context["category"] = category
        context["title"] = f"News Portal | {category.title if category else 'Category'}"
        return context
