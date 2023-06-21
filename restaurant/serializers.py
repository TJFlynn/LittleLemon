from rest_framework import serializers
from .models import MenuItem, Booking
from django.contrib.auth.models import User
       
class MenuItemSerializer(serializers.ModelSerializer):  
    class Meta():
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):  
    class Meta():
        model = Booking
        fields = ['id', 'name', 'num_guests', 'booking_date']