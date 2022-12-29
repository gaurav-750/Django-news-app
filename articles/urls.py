from django.urls import path
from .views import ArticleListView

# articles/
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list')
]
