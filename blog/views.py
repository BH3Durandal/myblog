from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from photologue.models import Gallery

from blog.models import Category, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#首页
def index(request):
    allcategory = Category.objects.all()
    gallerys = Gallery.objects.all().order_by('-id')[0:6]
    tui = Article.objects.filter(tui__id=1)[:5]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:5]
    link = Link.objects.all()
    return render(request, 'index.html', locals())

#列表页
def article(request):
    page = request.GET.get('page', 1)
    keyword = request.GET.get('keyword', '')
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    tui = Article.objects.filter(tui__id=1)[:5]
    allarticle = Article.objects.filter(Q(title__contains=keyword) | Q(excerpt__contains=keyword)).order_by('-id')
    paginator = Paginator(allarticle, 10)
    try:
        allarticle = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        allarticle = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        allarticle = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'article.html', locals())


#内容页
def article_detail(request,sid):
    detail = Article.objects.get(id=sid)
    hot = Article.objects.all().order_by('?')[:10]
    previous_blog = Article.objects.filter(created_time__gt=detail.created_time,category=detail.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=detail.created_time,category=detail.category.id).last()
    detail.views = detail.views + 1
    detail.save()
    return render(request, 'article_detail.html', locals())


# 关于我们
def about(request):
    return render(request, 'about.html',locals())


