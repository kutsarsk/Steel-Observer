from django import template

register = template.Library()


@register.inclusion_tag('pagination.html', takes_context=True)
def render_pagination(context, page_obj):
    request = context['request']
    params = request.GET.copy()
    params.pop('page', None)
    return {
        'page_obj': page_obj,
        'paginator': page_obj.paginator,
        'params': params,
    }
