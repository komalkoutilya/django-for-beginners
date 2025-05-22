from django.urls import path
from .views import SignUpView
# specify urlpatterns here
urlpatterns=[
    path('signup/', SignUpView.as_view(),name="signup"),
]