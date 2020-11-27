from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profiles/', views.ProfileView.as_view())
]
