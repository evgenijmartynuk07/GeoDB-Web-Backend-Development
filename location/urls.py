from rest_framework import routers

from .views import (
    PlaceViewSet,
)

router = routers.DefaultRouter()
router.register("place", PlaceViewSet)


urlpatterns = router.urls

app_name = "location"
