from django import template

register = template.Library()


@register.inclusion_tag('tags/webpack.html', takes_context=True)
def webpack(context, js_file_name):
    return {'js_file_name': js_file_name}
