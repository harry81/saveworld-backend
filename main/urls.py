from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from core import views as core_views

router = routers.SimpleRouter()
router.register(r'api-item', core_views.ItemAPIView, base_name="api-item")
router.register(r'api-image', core_views.ImageAPIView, base_name="api-image")
router.register(r'api-profile', core_views.ProfileAPIView, base_name="api-profile")
router.register(r'api-comment', core_views.CommentAPIView,
                base_name="api-comment")


urlpatterns = [
    url(r'^get_token/', core_views.get_token),
    url(r'^show_api_settings/', core_views.show_api_settings),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^', include(router.urls)),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^comments/', include('django_comments.urls')),
]
