from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class LogoutCustomView(LogoutView):
    http_method_names = ["post", "get", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
        

schema_view = get_schema_view(
    openapi.Info(
        title="URA API",
        default_version='v1',
        description="API documentation for the project",
        contact=openapi.Contact(email="tferreiraalves@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('atendimento/', include('atendimento.urls')),
    path('cliente/', include('cliente.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/logout/',LogoutCustomView.as_view(), name='logout'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', admin.site.urls, name='homepage'),
]
