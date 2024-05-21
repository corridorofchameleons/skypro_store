from django import template

register = template.Library()


@register.filter()
def url_filter(path):
    if path:
        return f'/{path}'
    return '#'


@register.filter()
def url_filter2(path):
    print(path)
    if path:
        return f'/media/{path}'
    return '#'