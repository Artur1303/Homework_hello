import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import View

from api_v1.serializers import ArticleSerializer
from webapp.models import Article


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'Get':
        return HttpResponse()
    return HttpResponseNotAllowed('Only get request are alowed')


class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        objects = Article.objects.all()
        slr = ArticleSerializer(objects, many=True)
        return JsonResponse(slr.data, safe=False)


class ArticleCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        slr = ArticleSerializer(data=data)
        if slr.is_valid():
            article = slr.save()
            return JsonResponse(slr.data, safe=False)
        else:
            response = JsonResponse(slr.errors, safe=False)
            response.status_code = 400
            return response


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        objects = get_object_or_404(Article, pk=kwargs['pk'])
        slr = ArticleSerializer(objects)
        return JsonResponse(slr.data, safe=False)


class ArticleUpdateView(View):
    def put(self, request, *args, **kwargs):
        objects = get_object_or_404(Article, pk=kwargs['pk'])
        data = json.loads(request.body)
        slr = ArticleSerializer(instance=objects, data=data)
        if slr.is_valid():
            article = slr.save()
            return JsonResponse(slr.data, safe=False)
        else:
            response = JsonResponse(slr.errors, safe=False)
            response.status_code = 400
            return response


class ArticleDeleteView(View):
    def delete(self, request, *args, **kwargs):
        objects = get_object_or_404(Article, pk=kwargs['pk'])
        objects.delete()
        return JsonResponse({
            'id': kwargs['pk']

        })