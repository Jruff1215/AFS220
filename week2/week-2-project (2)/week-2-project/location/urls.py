from django.urls import path

from . import views

app_name = "location"

urlpatterns = [
    path('', views.show_all_locations),
    path('<str:categoryname>', views.show_category_locations)
]