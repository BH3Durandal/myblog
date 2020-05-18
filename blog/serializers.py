from blog.models import Banner
from rest_framework import serializers

class BannerSerializers(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Banner
        fields = ('text_info', 'img', 'link_url', 'is_active')

    def get_img(self, banner):
        """
        :param banner:
        :return:返回img.url的绝对路径
        """
        request = self.context.get('request')
        return request.build_absolute_uri(banner.img.url)