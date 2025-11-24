from django.urls import path
from .view import DashboardView, ToggleTaskDoneView

app_name = "dashboard"

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path("tasks/<int:pk>/toggle/", ToggleTaskDoneView.as_view(), name="task_toggle"),
]