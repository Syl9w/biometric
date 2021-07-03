from django.urls import path
from . import views
urlpatterns = [
    path('', views.work_with_iin, name="work_with_iin" ),
    path("<str:iin>/", views.find_person, name="find_person"),
]