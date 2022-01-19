from django.urls import path
from .views import LoginUser, RegisterUser, LogoutView

urlpatterns = [
    path("sign_up/", RegisterUser.as_view(), name="register"),
    path("sign_in/", LoginUser.as_view(), name="login"),
    path("sign_out/<slug:admin_name>", LogoutView.as_view(), name="logout"),
]
