
from django.contrib import admin
from django.urls import path

from amqp.views import index

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
]
