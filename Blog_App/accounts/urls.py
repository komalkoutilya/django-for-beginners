from django.urls import path
from .views import SignUpView

# specify url-patterns here
urlpatterns=[
    path("signup/",SignUpView.as_view(),name="signup"),
]