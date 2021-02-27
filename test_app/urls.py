from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import View

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^rpx/", include("django_rpx_plus.urls")),
 ]
urlpatterns += staticfiles_urlpatterns()
