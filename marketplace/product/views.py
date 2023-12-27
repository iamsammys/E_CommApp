#!/usr/bin/env python3
from django.shortcuts import render
from rest_framework import viewsets
from product.models import (
    Product,
    ProductCategory,
    ProductReview
)
from product.serializer import (
    ReadProductSerializer,
    WriteProductSerializer,
    ProductCategorySerializer,
    ReadProductReviewSerializer,
    WriteProductReviewSerializer
)
from rest_framework.permissions import IsAuthenticated


class ProductView(viewsets.ModelViewSet):
    """
    Product view class
    """
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Return the serializer class to use
        """
        if self.request.method == "GET":
            return ReadProductSerializer
        return WriteProductSerializer
    
    def get_queryset(self):
        """
        Return the queryset to use
        """
        return (
            Product.objects.prefetch_related('reviews').
            select_related('category')
        )
    
class ProductCategoryView(viewsets.ModelViewSet):
    """
    Product category view class
    
    Attributes:
        queryset: Product category queryset
        serializer_class: Product category serializer class
    """
    permission_class = [IsAuthenticated]
    queryset = ProductCategory.objects.prefetch_related('products')
    serializer_class = ProductCategorySerializer

class ProductReviewView(viewsets.ModelViewSet):
    """
    Product review view class
    
    Attributes:
        queryset: Product review queryset
        serializer_class: Product review serializer class
    """
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        """
        Return the queryset to use
        """
        return (
            ProductReview.objects.select_related('product', 'user')\
            .filter(product=self.kwargs.get('product_id'))
            )

    def get_serializer_class(self):
        """
        Return the serializer class to use
        """
        if self.request.method == "GET":
            return ReadProductReviewSerializer
        return WriteProductReviewSerializer
    
    def get_serializer_context(self):
        """
        Return the serializer context to use
        """
        context = {
            'product_id': self.kwargs.get('product_id'),
            'user': self.request.user
            }
        
        return context
    