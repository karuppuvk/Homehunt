from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("property/<int:pk>/", views.property_detail, name="property_detail"),
    path("favourite/<int:pk>/", views.toggle_favourite, name="toggle_favourite"),
    path("favourites/", views.favourite_list, name="favourite_list"),
]
