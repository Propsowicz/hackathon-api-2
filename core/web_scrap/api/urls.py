
from django.urls import path
from .views import WebScraperAPI

urlpatterns = [
    path('post/', WebScraperAPI.as_view()),
    path('test/', WebScraperAPI.as_view()),
    
]
