"""
URL configuration for ovinogest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from ovinogestApp.views import new_ovino, adm_ovino, publico_ovino, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('new_ovino/', new_ovino, name='new_ovino'),
    path('adm_ovino/', adm_ovino, name='adm_ovino'),
    path('publico_ovino/', publico_ovino, name='publico_ovino'),

    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
