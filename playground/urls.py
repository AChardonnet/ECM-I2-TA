from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "character/<str:id_character>/", views.character_detail, name="character_detail"
    ),
    path(
        "character/<str:id_character>/?<str:message>",
        views.character_detail,
        name="character_detail_mes",
    ),
]
