from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from core.views import AngularApp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?!ng/).*$', AngularApp.as_view(), name="angular_app"),
] + static(
    settings.ANGULAR_URL,
    document_root=settings.ANGULAR_ROOT
)
