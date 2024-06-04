from django import template

register = template.Library()


@register.filter()
def url_filter(path):
    if path:
        return f'/media/{path}'
    return '#'


@register.filter()
def url_filter2(path):
    if path:
        return f'/media/{path}'
    return '#'


@register.filter()
def curr_version(ver_list):
    for v in ver_list:
        if v.current:
            return v
    return 'у продукта нет активной версии'

