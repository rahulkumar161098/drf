from django.urls import path
from . import views


urlpatterns = [
    path('', views.HelloAuthView.as_view(), name="auth"),
    path('signup', views.UserView.as_view(), name="sign_up")
]
