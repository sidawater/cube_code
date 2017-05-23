from django.shortcuts import render
from django.http import JsonResponse
from cubecode.settings import BASE_DIR
from .models import SignificantValue

# Create your views here.
def codemap_view(request):
    context = {
        'base_dir': BASE_DIR
    }
    return render(request, 'codemap/index.html', context)


def build_map(request):
    value_qs = SignificantValue.objects.select_related('key').order_by('key__name').values(
        'key__name', 'content', 'remark', 'related_type', 'images', 'supported')

    temp_dict = {}
    mark_key = ''
    memory_map = {}
    for value in value_qs:
        if mark_key == value['key__name']:
            memory_map[mark_key].append(value)
        else:
            mark_key = value['key__name']
            memory_map[mark_key] = [value]

    return JsonResponse({'status':'success', 'data': memory_map})
