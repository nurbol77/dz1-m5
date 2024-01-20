from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status

@api_view(['GET'])
def product_list_api_viem(request, id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error':'Product not Found!'},
                        status=404)
    data = ProductSerializer(products).data
    return Response(data=data)

@api_view(['POST'])
def test_api_view(request):
    json_object = {
         'int': 100,
         'float': 9.99,
         'text': 'hello',
         'dict': {
            'key': 'value'
        },
        'list': [1, 2, 3],
        'bool': True,
     }
    return Response(data=json_object)


def product_detail_api_view(request):
    return None