from django.urls import path

from .views.sign_up.sign_up import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
