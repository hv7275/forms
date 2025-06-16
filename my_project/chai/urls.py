from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chai_home'),
    path('<int:chai_id>', views.details, name='detail'),
]
