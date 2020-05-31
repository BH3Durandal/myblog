from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Category, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from blog.serializers import BannerSerializers


def global_variable(request):
    allcategory = Category.objects.all()
    remen = Article.objects.filter(tui__id=2)[:6]
    tags = Tag.objects.all()
    return locals()

#首页
def index(request):
    allcategory = Category.objects.all()
    tui = Article.objects.filter(tui__id=1)[:5]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:5]
    link = Link.objects.all()
    return render(request, 'index.html', locals())

#列表页
def article(request,page=1):
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    tui = Article.objects.filter(tui__id=1)[:5]
    allarticle = Article.objects.all()
    paginator = Paginator(allarticle, 5)
    try:
        allarticle = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        allarticle = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        allarticle = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'article.html', locals())


#内容页
def show(request,sid):
    show = Article.objects.get(id=sid)
    hot = Article.objects.all().order_by('?')[:10]
    previous_blog = Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show_article.html', locals())

#标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)
    tname = Tag.objects.get(name=tag)
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())

# 搜索页
def search(request):
    ss=request.GET.get('search')
    list = Article.objects.filter(title__contains=ss)
    page = request.GET.get('page')
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())


# 关于我们
def about(request):
    return render(request, 'about.html',locals())


# class Banners(APIView):
#
#     def get(self, request):
#         banners = Banner.objects.all()
#         data = BannerSerializers(banners, context={'request': request}, many=True)
#         return Response(data.data)
