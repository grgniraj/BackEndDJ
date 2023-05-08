from rest_framework import serializers
from inventory.models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity',
                  'location', 'reorderpoint', 'created_at', 'expirationdate', 'brand']


class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'profile_picture']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        profile_picture = validated_data.pop('profile_picture', None)
        instance = super().update(instance, validated_data)
        if profile_picture:
            instance.profile_picture = profile_picture
            instance.save()
        return instance