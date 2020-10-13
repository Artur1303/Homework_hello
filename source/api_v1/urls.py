from django.urls import path

from api_v1.views import get_token_view, ArticleCreateView

app_name = 'api'

urlpatterns = [
    path('get_token/', get_token_view, name='get_token'),
    path('article_create/', ArticleCreateView.as_view(), name='article_create')
]