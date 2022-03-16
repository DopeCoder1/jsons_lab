from django.urls import path
from .views import info
urlpatterns = [
    path('', info.as_view(), name="info"),
]