"""fit_n_bite_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#schema_view = get_schema_view(title='Fit-n-Bite API',renderer_classes=[SwaggerUIRenderer])
schema_view = get_schema_view(
    openapi.Info(
    title="Fit-n-Bite API",
    default_version='v1',
    description="A lightweight API providing details of foods",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="jingcikeili@gmail.com"),
    license=openapi.License(name="BSD License"),
    ),
    public =True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0),name='docs'),   # 配置docs的url路径
    path('redoc/', schema_view.with_ui('redoc',cache_timeout=0),name='redoc')   # 配置docs的url路径
]
