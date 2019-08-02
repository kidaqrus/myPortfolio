import portApp.views

from django.urls import path




urlpatterns = [
    path('', portApp.views.home, name='home'),
]