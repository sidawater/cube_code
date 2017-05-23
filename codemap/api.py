from tastypie import fields
from tastypie.api import Api
from tastypie.resources import ModelResource, ALL
from tastypie.serializers import Serializer
from .models import MemoryMapKey, SignificantValue


class MemoryMapKeyResource(ModelResource):
    values = fields.ToManyField('codemap.api.SignificantValueResource', 'significantvalue_set', full=True)

    class Meta:
        queryset = MemoryMapKey.objects.all().prefetch_related('significantvalue_set').order_by('name')
        resource_name = 'mapkey'
        fields = ['id', 'name', 'frequency']
        filtering = {
            'id': ALL,
            'name': ALL,
        }
        serializer = Serializer(formats=['json', ])

    def build_map(self):
        # key_qs = MemoryMapKey.objects.values('id', 'name')
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

        return JsonResponse(memory_map)

class SignificantValueResource(ModelResource):
    key = fields.ForeignKey(MemoryMapKeyResource, 'key')

    class Meta:
        queryset = SignificantValue.objects.all()
        resource_name = 'mapvalue'
        fields = ['id', 'key', 'content', 'remark', 'related_type', 'images', 'supported']
        filtering = {
            'id': ALL,
            'content': ALL,
            'supported': ALL,
        }
        serializer = Serializer(formats=['json', ])


v1_api = Api(api_name='v1')
v1_api.register(MemoryMapKeyResource())
v1_api.register(SignificantValueResource())
