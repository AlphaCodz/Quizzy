from django.urls import path
from .views import CreateQuiz

urlpatterns = [
    path("", CreateQuiz.as_view(), name="signup")
]
