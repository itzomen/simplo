from django.urls import path
from .views import  *


urlpatterns = [
    path("", create, name="create"),
    path("", categories, name="categories"),
    path("<str:pk>/", update, name="update"),
    path("<str:pk>/", delete, name="delete"),
]
