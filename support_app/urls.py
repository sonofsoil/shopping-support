from django.urls import path
from support_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tools/", views.tools, name="tools"),
    path("orders/", views.orders, name="orders"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]