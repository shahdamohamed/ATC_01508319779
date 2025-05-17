from rest_framework import serializers
from .models import Event, Booking
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)  # or UserSerializer if you want

    class Meta:
        model = Booking
        fields = ['id', 'user', 'event']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user