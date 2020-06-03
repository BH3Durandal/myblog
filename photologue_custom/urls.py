from django.urls import path

from photologue_custom import views

app_name='photologue_custom'
urlpatterns = [
    path('gallery', views.gallery, name='gallery'),
    path('gallery_detail/<int:gid>', views.gallery_detail, name='gallery_detail'),
    path('diggit', views.diggit, name='diggit'),
    path('gallerys', views.gallerys.as_view(), name='gallerys'),
]