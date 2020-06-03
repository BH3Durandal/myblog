from photologue.models import Gallery
from rest_framework import serializers

class GallerySerializers(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ('id', 'title', 'description', 'img_url')

    def get_img_url(self, gallery):
        """
        :param banner:
        :return:返回img.url的绝对路径
        """
        request = self.context.get('request')
        return request.build_absolute_uri(gallery.sample()[0].get_display_url())