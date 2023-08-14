from django.urls import path
from . import views
from .views import GeneratePdf

urlpatterns = [
    path('', views.laptops, name='laptops'),
    path('laptops/', views.laptops, name='laptops'),
    path('test/', views.test, name='test'),
    path('add-laptop/', views.add_laptop, name='add_laptop'),
    path('service-request/', views.service_request, name='service_request'),
    path('laptops/details/<int:id>', views.details, name='details'),
    path('service-request/details/<int:id>', views.service_details, name='service_details'),
    path('pdf/', GeneratePdf.as_view()), 
]