"""campaign_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('api/auth/', include('djoser.urls.authtoken')),
                  path('api/auth/', include('djoser.urls.base')),

                  path('api/auth/', include('djoser.urls.jwt')),
                  path('adminpanel/', admin.site.urls),
                  path('api/identity/', include('identity.urls')),
                  path('api/reserve/', include('reserve.urls')),
                  path('api/zarinpal/', include('zarinpal.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "پنل مدیریت"