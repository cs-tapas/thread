from django.shortcuts import render, redirect
from . models import News


def news_home(request):
  news = News.objects.all().order_by("-id")

  if request.GET.get('search'):
    news = news.filter(head__icontains = request.GET.get('search'))

  context = {'news': news, 'search_flag': True}
  return render(request, 'index.html', context)


def news_publish(request):
  if request.method == 'POST':
    data = request.POST

    head = data.get('head')
    body = data.get('body')

    News.objects.create(
      head = head,
      body = body,
    )

    return redirect('/')

  return render(request, 'publish.html')


def news_update(request):
  news = News.objects.all().order_by("-id")

  if request.GET.get('search'):
    news = news.filter(head__icontains = request.GET.get('search'))

  context = {'news': news, 'search_flag': True}
  return render(request, 'update.html', context)


def news_delete(request, id):
  news = News.objects.get(id = id)
  news.delete()
  return redirect('/update/')


def news_edit(request, id):
  news = News.objects.get(id = id)

  if request.method == 'POST':
    data = request.POST

    news.head = data.get('head')
    news.body = data.get('body')

    news.save()
    return redirect('/update/')

  context = {'news': news}
  return render(request, 'edit.html', context)
