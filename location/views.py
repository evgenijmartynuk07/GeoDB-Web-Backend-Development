from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Place
from .serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        methods=["POST"],
        summary="Create a new place",
        description="This endpoint creates a new place. "
                    "(name, description, geom(POINT)",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="List of all Places",
        parameters=[
            OpenApiParameter(
                "latitude",
                type=str,
                description="Specify the latitude parameters "
                            "in the format like 1.000 (floating-point number)",
            ),
            OpenApiParameter(
                "longitude",
                type=str,
                description="Specify the longitude parameters "
                            "in the format like 1.000 (floating-point number)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs) -> Response:
        """
        Here you can view a list of all coordinates available in the database.
        Using the provided coordinates,
        you can filter the points based on proximity.
        """
        latitude = request.query_params.get("latitude")
        longitude = request.query_params.get("longitude")

        queryset = Place.objects.all()

        if latitude is not None and longitude is not None:
            try:
                latitude = float(latitude)
                longitude = float(longitude)
                point = Point(longitude, latitude, srid=4326)
                queryset = queryset.annotate(
                    distance=Distance("geom", point)
                ).order_by("distance")[:1]
            except ValueError:
                raise ValidationError(
                    "Latitude and longitude must be valid float-point numbers."
                )

        serializer = self.get_serializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    @extend_schema(
        methods=["GET"],
        summary="Retrieve a place by ID",
        description="This endpoint retrieves a specific place by its ID.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        methods=["PUT"],
        summary="Update a place",
        description="This endpoint update a specific place. "
                    "(name = string, description = text, "
                    "geom = POINT(1.000, 1.000).",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        methods=["DELETE"],
        summary="Delete a place",
        description="This endpoint deletes a specific place by ID.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
