from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User
       
class MenuItemSerializer(serializers.ModelSerializer):  
    class Meta():
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):  
    class Meta():
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'bookingdate']