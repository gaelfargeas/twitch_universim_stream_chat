from django.urls import path

from . import views

urlpatterns = [
    path(
        "logged/static/css/styles.css",
        views.redirect_style_css,
        name="redirect_style_css",
    ),
    path(
        "logged/static/images/favicon.ico",
        views.redirect_favicon,
        name="redirect_favicon",
    ),
    path("logged/", views.logged, name="logged"),
    path("", views.index, name="index"),
]

