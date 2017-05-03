from rest_framework import routers
from geobadge.accounts import viewsets as account_viewsets
from geobadge.badges import viewsets as badge_viewsets


router = routers.DefaultRouter()

router.register(r'users', account_viewsets.UserViewSet)
router.register(r'badges', badge_viewsets.BadgeViewSet)

urlpatterns = router.urls
