"""crud_products URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from polaris.common.utilities import CustomOpenAPISchemaGenerator
from rest_framework.routers import SimpleRouter

from crud_products.settings import SWAGGER_URL
from products.views import ProductView

schema_view = get_schema_view(
    openapi.Info(
        title="Products",
        default_version='v1',
        description="Microservicio de productos"
    ),
    generator_class=CustomOpenAPISchemaGenerator,
    public=True,
    url=SWAGGER_URL
)
router = SimpleRouter()
router.register(r'product', ProductView)
urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0))
]
