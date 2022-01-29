from django.urls import path
from .views import  *


urlpatterns = [
    path("create", create, name="create"),
    path("categories", categories, name="categories"),
    path("update/<str:pk>", update, name="update"),
    path("delete/<str:pk>", delete, name="delete"),
]
