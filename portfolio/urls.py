from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('portfolio/photography', views.portfolio, name="photography_portfolio"),
    path('portfolio/professional', views.portfolio, name="professional_portfolio"),
]

urlpatterns += staticfiles_urlpatterns()