from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='main_page'),
    path('api/',views.api,name='api'),
]
