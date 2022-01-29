from django.urls import path
from .views import  *


urlpatterns = [
    path("register", registerUser, name="register"),
    path("login", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('logout', LogoutView.as_view(), name='logout'),
]
