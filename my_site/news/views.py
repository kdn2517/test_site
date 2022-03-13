from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import News, Category


def index(request):
	news = News.objects.all()
	content = {'news': news,
			   'title': 'Список новостей',
			   }
	return render(request, 'news/index.html', content)


def get_category(request, category_id):
	news = News.objects.filter(category_id=category_id)
	category = Category.objects.get(pk=category_id)
	content = {'news': news,
			   'title': 'Список новостей',
			   'category': category,
			   }
	return render(request, 'news/category.html', content)


def view_news(request, news_id):
	#news_item = News.objects.get(pk=news_id)
	news_item = get_object_or_404(News, pk=news_id)
	return render(request, 'news/view_news.html', {'news_item': news_item})
