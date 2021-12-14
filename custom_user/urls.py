from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


app_name = "users"
urlpatterns = [
    path("register/", views.RegistrationView.as_view(), name="register"),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("login/", views.LoginUser.as_view(), name="login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)