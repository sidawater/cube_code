import os
from django import template
from cubecode.settings import DEBUG

register = template.Library()


@register.inclusion_tag('tags/webpack.html', takes_context=True)
def webpack(context, static_file_name):
    css_dir = os.listdir('static/static/css')
    js_dir = os.listdir('static/static/js')
    app_label = static_file_name.split('_')[0]

    css_list = [css for css in css_dir if css.startswith(static_file_name) and css.endswith('.css')]

    app_js_list = [js for js in js_dir if static_file_name in js and js.endswith('.js')]
    first_js = [js for js in js_dir if app_label + '_manifest' in js and js.endswith('.js')]
    second_js = [js for js in js_dir if app_label + '_vendor' in js and js.endswith('.js')]
    all_js_list = first_js + second_js + app_js_list

    context = {
        'debug': DEBUG,
        'js_list': all_js_list,
        'css_list': css_list,
        'static_file_name': static_file_name,
    }
    return context
