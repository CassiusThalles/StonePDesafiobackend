from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from funcionarios.views import FuncionariosViewSet

router = routers.DefaultRouter()
router.register(r'funcionario', FuncionariosViewSet, base_name='Funcionario')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth', obtain_auth_token),
]
