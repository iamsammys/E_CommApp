from rest_framework import serializers
from .models import Cart, CartItem
from product.models import Product
from product.serializer import ReadProductSerializer


class ReadCartItemSerializer(serializers.ModelSerializer):
    """
    Read cart item serializer class
    
    Attributes:
        product: Product
        cart: Cart
        quantity: int
        price: int
    """
    product = ReadProductSerializer()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        """
        Cart item serializer meta class
        """
        model = CartItem
        fields = [
            'id',
            'product',
            'cart',
            'quantity',
            'created_at',
            'updated_at'
        ]

class WriteCartItemSerializer(serializers.ModelSerializer):
    """
    Write cart item serializer class
    
    Attributes:
        product: Product
        cart: Cart
        quantity: int
        price: int
    """
    class Meta:
        """
        Cart item serializer meta class
        """
        model = CartItem
        fields = [
            'product',
            'cart',
            'quantity',
            'created_at',
            'updated_at'
        ]
    def validate(self, data):
        """
        Validate cart item data
        
        Args:
            data: Cart item data
        
        Returns:
            data: Cart item data
        """
        if not Cart.objects.filter(user=self.context.get('user'),
                                   pk=self.context.get('cart_id')).exists():
            raise serializers.ValidationError("Cart does not exist")
        
        
        product = data['product']

        try:
            cart_item = CartItem.objects.get(cart_id=self.context.get('cart_id'),
                                                product=product)
            quantity = cart_item.quantity
        except CartItem.DoesNotExist:
            quantity = 0

        if quantity + data['quantity'] > product.quantity:
            raise serializers.ValidationError("Product quantity exceeded")
        
        return data
    
    def create(self, validated_data):
        """
        Create a new cart item
        
        Args:
            validated_data: Validated data
        
        Returns:
            cart_item: Cart item
        """
        product = validated_data['product']
        # if cart exists then the quantity should be created and not creating a new cart
        cart_item, create = CartItem.objects.get_or_create(user=self.context.get('user'),
                                            cart_id=self.context.get('cart_id'),
                                            product=product,
                                            **validated_data)
        
        if not create:
            cart_item.quantity += validated_data['quantity']
            cart_item.save()

        return cart_item

class CartSerializer(serializers.ModelSerializer):
    """
    Cart serializer class

    Attributes:
        user: User
        cart_items: CartItem
    """
    user = serializers.StringRelatedField()
    cart_items = ReadCartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'cart_items',
            'total_price'
            'created_at',
            'updated_at'
        ]

    def validate(self, data):
        """
        Validate cart data

        Args:
            data: Cart data

        Returns:
            data: Cart data
        """
        if Cart.objects.filter(user=data['user']).exists():
            raise serializers.ValidationError("Cart already exists")
        return data
    
    def create(self, validated_data):
        """
        Create a new cart
        
        Args:
            validated_data: Validated data
        
        Returns:
            cart: Cart
        """
        return Cart.objects.create(user=self.context.get('user'), **validated_data)