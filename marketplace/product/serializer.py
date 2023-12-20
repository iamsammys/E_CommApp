#!/usr/bin/env python
"""
Module for serializing the product instances
Created on Sep 19, 2021
    By Samuel Ezeh
"""

from rest_framework import serializers
from product.models import (
    Product,
    ProductCategory,
    ProductReview
)
from django.contrib.auth.models import User


class ReadProductSerializer(serializers.ModelSerializer):
    """
    Product serializer class
    """
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'

        extra_kwargs = {
            'description': {'read_only': True},
            'quantity': {'read_only': True},
            'price': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'id': {'read_only': True},
            'name': {'read_only': True},
            'image': {'read_only': True},
        }

class WriteProductSerializer(serializers.ModelSerializer):
    """
    Product serializer class
    """
    category = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'quantity',
            'price',
            'image',
            'category',
        ]

class ProductCategorySerializer(serializers.ModelSerializer):
    """
    Product category serializer class

    Attributes:
        name: Product category name
        description: Product category description

    """
    class Meta:
        model = ProductCategory
        fields = '__all__'
    
    id = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

class ReadProductReviewSerializer(serializers.ModelSerializer):
    """
    Product review serializer class

    Attributes:
        product: Product
        user: User
        rating: Rating
        review: Review
    """
    Product = ReadProductSerializer
    user = serializers.StringRelatedField()

    class Meta:
        model = ProductReview
        fields = '__all__'

class WriteProductReviewSerializer(serializers.ModelSerializer):
    """
    Product review serializer class
    
    Attributes:
        product: Product
        user: User
        rating: Rating
        review: Review
    """
    class Meta:
        model = ProductReview
        fields = [
            'rating',
            'review',
        ]

    def validate(self, value):
        """
        Validate the rating
        """
        product_id = self.context.get('product')
        user = self.context.get('user')
        rating = value.get('rating')

        print('product is {}'.format(Product.objects.filter(id=product_id).exists()))
        if not Product.objects.filter(id=product_id).exists():
            raise serializers.ValidationError({
                'error': "This product does not exist, try creating the product first"
                }
                )
        
        if ProductReview.objects.filter(product_id=product_id, user=user).exists():
            raise serializers.ValidationError("You have already reviewed this product")

        if rating < 1 or rating > 5:
            raise serializers.ValidationError({
                'error': "Rating must be between 1 and 5"
                }
                )
        
        return value
    
    def create (self, validated_data):
        """
        Create a new product review
        
        Arguments:
            validated_data: Validated data
            
        Returns:
            product_review: Product review
        """
        user = self.context.get('user')
        product_id = self.context.get('product_id')
        product_review = ProductReview.objects.create(
            user=user,
            product_id=product_id,
            **validated_data
        )
        return product_review