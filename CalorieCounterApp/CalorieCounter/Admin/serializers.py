from rest_framework import serializers

from .models import Foods, Activities


# Create a model serializer
class FoodsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Foods
        fields = ('name', 'type',  'calories')


class ActivitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activities
        fields = ('Activity_name', 'time_duration', 'calorie_burns')