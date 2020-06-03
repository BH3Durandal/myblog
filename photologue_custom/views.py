from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from photologue.models import Gallery
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Category, Tag, Article
from photologue_custom.serializers import GallerySerializers


def gallery(request):
    page = request.GET.get('page', 1)
    gallerys = Gallery.objects.filter(is_public=True).order_by('-id')
    paginator = Paginator(gallerys, 8)
    try:
        gallerys = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        gallerys = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        gallerys = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'gallery.html', locals())

def gallery_detail(request, gid):
    hot = Article.objects.all().order_by('views')[:5]
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    tui = Article.objects.filter(tui__id=1)[:5]
    gallery = Gallery.objects.get(Q(is_public=True) & Q(pk=gid))
    return render(request, 'gallery_detail.html', locals())

class gallerys(APIView):

    def get(self, request):
        page = request.GET.get('page', 1)
        gallery = Gallery.objects.all()[(page-1)*8:page*8]
        data = GallerySerializers(gallery, context={'request': request}, many=True)
        return Response(data.data)