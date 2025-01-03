from .models import Category, SubCategory, Product, Cart, CartItem
from .serializers import CatSer, ProSer, CartSerializer, CartItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class CatGET(APIView):
    @extend_schema(
        operation_id="list_categories",
        summary="Получить список категорий",
        description="Получить список категорий с пагинацией",
        parameters=[
            OpenApiParameter(
                name="page",
                description="Номер страницы",
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 1
        result_page = paginator.paginate_queryset(categories, request)
        serializer = CatSer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class ProGET(APIView):
    @extend_schema(
        operation_id="list_products",
        summary="Получить список продуктов",
        description="Получить список продуктов с пагинацией",
        parameters=[
            OpenApiParameter(
                name="page",
                description="Номер страницы",
                required=False,
                type=int,
                location=OpenApiParameter.QUERY,
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 1
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProSer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только корзину текущего пользователя
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Устанавливаем текущего пользователя как владельца корзины
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Дополнительная логика при обновлении (если требуется)
        serializer.save()

    def perform_destroy(self, instance):
        # Дополнительная логика при удалении (если требуется)
        instance.delete()


