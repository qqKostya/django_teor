from django.urls import path

from .views import IndexView, DetailView, AnswerView

app_name = "riddles"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:riddle_id>/", DetailView.as_view(), name="detail"),
    path("<int:riddle_id>/answer/", AnswerView.as_view(), name="answer"),
]
