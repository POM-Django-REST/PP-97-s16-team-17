from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = Order
        fields = ['book', 'user', 'user_name', 'plated_end_at']