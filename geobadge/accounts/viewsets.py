from rest_framework import viewsets
from geobadge.accounts.models import User
from geobadge.accounts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed and edited.
    """
    serializer_class = UserSerializer
    queryset = User.objects.none()
    search_fields = (
        'username',
    )

    def get_queryset(self):
        """
        This view should return a list of only the
        users that the current user can view.
        """
        return User.objects.all()
