from django import template

register = template.Library()

@register.filter
def img(gallery):
    img = gallery.sample()
    if img is None:
        return
    return img[0].get_display_url()