from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'name', 'persons', 'date', 'time', 'movie', 'seats', 'price')