from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('portfolio/', views.portfolio, name="portfolio"),

    # Django Auth
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)