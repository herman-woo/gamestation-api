from django.urls import path
from . import views

app_name = 'Games'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.get_book, name="get book")
]