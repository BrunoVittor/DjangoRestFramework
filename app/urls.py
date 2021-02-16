from django.urls import path
from app.views import TodoListAndCreate, TodoDetailChangeAndDelete


urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>', TodoDetailChangeAndDelete.as_view()),
]
