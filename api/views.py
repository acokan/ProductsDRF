from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import ProductType, Product
from api.serializers import ProductTypeSerializer, ProductSerializer


class ProductTypeList(generics.ListAPIView):

    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()


class ProductList(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        product_id = self.request.query_params.get('id', None)
        if product_id is not None:
            queryset = queryset.filter(id=product_id)
        return queryset


class ProductListByID(generics.ListAPIView):

    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['id']
        return Product.objects.filter(id=product_id)
