from django.contrib import admin
from django.urls import path

from config.views import main, burger_list


# urlpatterns는 리스트, 리스트의 각 path 항목은 메뉴
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main),
    path("burgers/", burger_list),
]

