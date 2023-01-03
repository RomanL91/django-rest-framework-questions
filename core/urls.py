from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from test_orm.views import EntityViewset

# создаю экземпляр класса DefaultRouter и регистрирую View на пустую строку
router = routers.DefaultRouter()
router.register(r'', EntityViewset, basename='entity_create')

# подключаю пути от router к пустой строке
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] 
       