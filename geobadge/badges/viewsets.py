from rest_framework import viewsets
from geobadge.badges.models import Badge
from geobadge.badges.serializers import BadgeSerializer


class BadgeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows badges to be viewed and edited.
    """
    serializer_class = BadgeSerializer
    queryset = Badge.objects.none()
    search_fields = (
        'created',
    )

    def get_queryset(self):
        """
        This view should return a list of all the badges
        for the currently authenticated user.
        """
        user = self.request.user
        return Badge.objects.all()
