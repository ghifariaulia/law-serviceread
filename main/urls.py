from django.urls import path

from main.views import UserRead

app_name = 'main'

urlpatterns = [
    path('read/<str:npm>/', UserRead.as_view())
]
