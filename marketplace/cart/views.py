from django.shortcuts import render
from cart.models import Cart, CartItem
from cart.serializer import (
    ReadCartItemSerializer,
    WriteCartItemSerializer,
    CartSerializer
)
from rest_framework import viewsets


class CartViewSet(viewsets.ModelViewSet):
    """
    Cart viewset class

    Attributes:
        queryset: Cart queryset
        serializer_class: Cart serializer class
    """
    serializer_class = CartSerializer

    def get_queryset(self):
        """
        Get queryset

        Returns:
            Queryset: Cart queryset
        """
        queryset = Cart.objects.select_related('user').\
            prefetch_related('cart_items').\
            filter(user=self.request.user)
        return queryset
    
    def get_serializer_context(self):
        """
        Get context

        Returns:
            dict: Context
        """
        context = {}
        context['user'] = self.request.user
        return context

class CartItemViewSet(viewsets.ModelViewSet):
    """
    CartItem viewset class

    Attributes:
        queryset: CartItem queryset
        serializer_class: CartItem serializer class
    """
    def get_queryset(self):
        """
        Get queryset

        Returns:
            Queryset: CartItem queryset
        """
        queryset = CartItem.objects.select_related('cart', 'product').\
            filter(cart__user=self.request.user)
        return queryset

    def get_serializer_class(self):
        """
        Get serializer class

        Returns:
            Serializer class: CartItem serializer class
        """
        if self.action in ['list', 'retrieve']:
            return ReadCartItemSerializer
        return WriteCartItemSerializer

    def get_serializer_context(self):
        """
        Get serializer context

        Returns:
            dict: Serializer context
        """
        context = {}
        context['user'] = self.request.user
        context['cart_id'] = self.request.data.get('cart_id')
        return context