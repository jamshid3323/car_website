from django.urls import path
from .views import HomePageView, MessageView

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('message/', MessageView.as_view(), name='message'),
]