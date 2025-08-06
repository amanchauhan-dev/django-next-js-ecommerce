from rest_framework import serializers
from .models import Product, ProductImage, Category, Brand

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'alt_text']

class ProductSerializer(serializers.ModelSerializer):
    additional_images = ProductImageSerializer(many=True, required=False)
    seller = serializers.ReadOnlyField(source='seller.username')

    class Meta:
        model = Product
        fields = [
            'id', 'seller', 'name', 'slug', 'description', 'price',
            'discount_price', 'stock', 'image', 'additional_images',
            'is_featured', 'status', 'category', 'brand', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        images_data = self.initial_data.getlist('additional_images')
        product = Product.objects.create(**validated_data)

        for image in images_data:
            ProductImage.objects.create(product=product, image=image)
        return product
