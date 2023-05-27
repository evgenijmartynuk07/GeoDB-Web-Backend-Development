from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, OpenApiParameter
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
        description="This endpoint creates a new place. (name, description, geom(POINT)",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="List of all Places",
        parameters=[
            OpenApiParameter(
                "latitude",
                type=str,
                description="Specify the latitude parameters in the format like 1.000 (floating-point number)",
            ),
            OpenApiParameter(
                "longitude",
                type=str,
                description="Specify the longitude parameters in the format like 1.000 (floating-point number)",
            ),
        ]
    )
    def list(self, request, *args, **kwargs) -> Response:
        """
        Here you can view a list of all coordinates available in the database.
        Using the provided coordinates, you will be able to find the nearest point.
        """
        latitude = float(request.query_params.get("latitude"))
        longitude = float(request.query_params.get("longitude"))

        point = Point(longitude, latitude, srid=4326)

        nearest_place = Place.objects.annotate(
            distance=Distance("geom", point)
        ).order_by('distance').first()

        serializer = self.get_serializer(nearest_place)
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
        description="This endpoint update a specific place. (name = string, description = text, geom = POINT(1.000, 1.000).",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        methods=['DELETE'],
        summary="Delete a place",
        description="This endpoint deletes a specific place by ID.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


