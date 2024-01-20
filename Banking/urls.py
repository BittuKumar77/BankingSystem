from django.urls import path
from .views import home, transfer

urlpatterns = [
    path('', home, name='home'),
    path('transfer/', transfer, name='transfer'),
]