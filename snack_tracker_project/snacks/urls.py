from django.urls import path
from .views import SnackListView,HomePageView,SnackDetailView

urlpatterns = [
    path('',HomePageView.as_view() , name= 'home'),
    path('snacks-list',SnackListView.as_view() , name= 'snacks_list'),
    path('snack-detail/<int:pk>',SnackDetailView.as_view() , name= 'snack_detail'),
]