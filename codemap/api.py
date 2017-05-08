from tastypie import fields
from tastypie.api import Api
from tastypie.resources import ModelResource, ALL
from tastypie.serializers import Serializer
from .models import MemoryMapKey, SignificantValue


class MemoryMapKeyResource(ModelResource):
    values = fields.ToManyField('codemap.api.SignificantValueResource', 'significantvalue_set', full=True)
    class Meta:
        queryset = MemoryMapKey.objects.all()
        resource_name = 'mapkey'
        fields = ['id', 'name', 'frequency']
        filtering = {
            'id': ALL,
            'name': ALL,
        }
        serializer = Serializer(formats=['json', ])


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
