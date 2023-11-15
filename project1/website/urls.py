from django.urls import path
from . import views

urlpatterns = [
    path('brainware/', views.brainware, name='brainware'),
    path('hardware/', views.hardware, name='hardware'),
    path('software/', views.software, name='software'),
    path('utama/', views.utama, name='utama'),
   
]

