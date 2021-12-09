from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


app_name = "content"
urlpatterns = [
    path("books/", views.BooksView.as_view(), name="books"),
    path("anime/", views.AnimeView.as_view(), name="naruto"),
    path("parser/", views.ParserAnimeView.as_view(), name="parser"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)