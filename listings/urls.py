from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property/<int:id>/', views.property_detail, name='property_detail'),
    path('property/add/', views.PropertyCreateView.as_view(), name='property_add'),
    path('property/<int:pk>/edit/', views.PropertyUpdateView.as_view(), name='property_edit'),
    path('property/<int:pk>/delete/', views.PropertyDeleteView.as_view(), name='property_delete'),
    path('user_properties/', views.user_properties, name='user_properties')
]
