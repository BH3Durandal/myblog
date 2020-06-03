'''
Created on 2019年11月5日

@author: xwx
'''
from django.urls import path
from blog import views
#命名空间
app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),  # 网站首页
    path('article', views.article, name='article'),
    path('article_detail/<int:sid>', views.article_detail, name='article_detail'),  # 内容页
    path('about/', views.about, name='about'),  # 联系我们单页
]