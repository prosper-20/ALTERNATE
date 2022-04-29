from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.service, name="services"),
    path("message/", views.message, name="contact"),
    path("consultation/", views.consult, name="consult")
]
