from django.urls import path
from . import views


# underwriter views
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:id>/', views.get_game_by_id, name="Get Game")
]

