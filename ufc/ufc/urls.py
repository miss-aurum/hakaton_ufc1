from django.contrib import admin
from django.urls import path, include
from .api import router


urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/v1/', include(router.urls)),



]















# from django.urls import path, include, re_path
# from django.conf import settings
# from app_ufc.views import *

# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )   

# from drf_yasg import openapi


# schema_view = get_schema_view(
#    openapi.Info(
#       title="LightCode Restapi Lesson",
#       default_version='v1',
#       description="Mentor GU",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="turdubekaltynkyz@gmail.com"),
#       license=openapi.License(name="BSD License"),
#    ),

#    public=True,
#    permission_classes=[permissions.AllowAny],
# )





# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('app_ufc/', include('app_ufc.urls')),
#     # path('history_app/',include('history_app.urls')),
#     # path('info_futurefees_app/', include('info_futurefees_app.urls')),
#     # path('shop_ufc_app/', include('shop_ufc_app.urls')),
#     # path('api-auth/', include('rest_framework.urls')),
#     re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('sportman_list/', SportmanViewset.as_view({
#     'get':'list',
#     'post':'create',

#     }) )
# ]

