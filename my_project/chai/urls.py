from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chai_home'),
    path('<int:chai_id>', views.details, name='detail'),
    path('chai_store/', views.chai_store, name='chai_store'),
]
