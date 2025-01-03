from rest_framework import serializers
from .models import Category, SubCategory, Product, Cart, CartItem

class SubCatSer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name']

class CatSer(serializers.ModelSerializer):
    subcategories = SubCatSer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['name', 'subcategories']

class CatSer2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class SubCatSer2(serializers.ModelSerializer):
    category = CatSer2()

    class Meta:
        model = SubCategory
        fields = [ 'name', 'category']

class ProSer(serializers.ModelSerializer):
    subcategory = SubCatSer2()
    class Meta:
        model = Product
        fields = ['name','slug','subcategory','price','image_big','image_medium','image_small']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProSer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total_quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_quantity', 'total_price']

    def get_total_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def get_total_price(self, obj):
        return sum(item.get_total_price() for item in obj.items.all())