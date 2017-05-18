from django import template
from cubecode.settings import DEBUG

register = template.Library()


@register.inclusion_tag('tags/webpack.html', takes_context=True)
def webpack(context, js_file_name, is_memory):
    context = {
        'debug': DEBUG,
        'js_file_name': js_file_name,
        'is_memory': is_memory
    }

    return context
