from rest_framework import serializers
from events.models import Categories, Events


class CategoriesSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class EventsSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
