from uuid import uuid4

from django.core.files.storage import FileSystemStorage


class UploadStorage(FileSystemStorage):
    from django.conf import settings

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        # 初始化
        super(UploadStorage, self).__init__(location, base_url)

    # 重写 _save方法
    def _save(self, name, content):
        # name为上传文件名称
        import os, time
        # 文件扩展名
        ext = os.path.splitext(name)[1]
        # 重写合成文件名
        name = 'img/{}/{}.{}'.format(time.strftime('%Y/%m/%d'), uuid4().hex, ext)
        # 调用父类方法
        return super(UploadStorage, self)._save(name, content)