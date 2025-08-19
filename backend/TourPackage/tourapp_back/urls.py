from django.urls import path
from . import views
from .views import BannerListAPIView

urlpatterns = [
    path('packages/', views.package_list, name='packages-list'),
    path('packages/<int:pk>/', views.package_detail, name='package-detail'),
    path('enquiries/', views.enquiry_create, name='enquiry-create'),
    path('banners/', BannerListAPIView.as_view(), name='banner-list'),
]
