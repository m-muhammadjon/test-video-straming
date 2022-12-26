from django.urls import path
from stream import views

app_name = 'stream'

urlpatterns = [
    path('', views.home, name='home'),
    path('stream/<str:uid>/', views.stream, name='stream'),
]
