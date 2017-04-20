from rest_framework import routers
from geobadge.badges import viewsets as badge_viewsets


router = routers.DefaultRouter()

router.register(r'badges', badge_viewsets.BadgeViewSet)

urlpatterns = router.urls
