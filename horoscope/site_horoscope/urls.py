from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("<int:number_zodiac>/", views.num_redirect_info_zodiac),
    path("<str:zodiac_sign>/", views.get_info_zodiac, name='info_zodiac_sign'),
]