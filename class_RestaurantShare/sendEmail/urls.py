from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.sendEmail), #http://localhost:8080/seneEmail/send/ 호출시 매칭
]
