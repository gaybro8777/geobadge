"""
URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API Documentation', url='/api/')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    url(r'^api-docs/$', schema_view),

    url(
        r'^api/',
        include('geobadge.api.urls', namespace='api'),
        name='api_root',
    ),
]
