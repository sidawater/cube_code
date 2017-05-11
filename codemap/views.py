from django.shortcuts import render
from cubecode.settings import BASE_DIR

# Create your views here.
def codemap_view(request):
    context = {
        'base_dir': BASE_DIR
    }
    return render(request, 'codemap/base.html', context)
