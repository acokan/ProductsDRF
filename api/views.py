from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import ProductType, Product
from api.serializers import ProductTypeSerializer, ProductSerializer


class ProductTypeList(generics.ListAPIView):

    serializer_class = ProductTypeSerializer

    # queryset = ProductType.objects.all()

    def get_queryset(self):
        return ProductType.objects.all()


class ProductList(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

