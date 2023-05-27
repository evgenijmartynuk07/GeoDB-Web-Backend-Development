from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers
from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    geom = gis_serializers.GeometryField()

    class Meta:
        model = Place
        fields = ("id", "name", "description", "geom")
