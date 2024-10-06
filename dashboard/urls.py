from django.urls import path
from . import views
from .views import user_logout
from .views import add_product

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>', views.staff_detail, name='dashboard-staff-detail'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.product_delete, 
         name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, 
         name='dashboard-product-update'),
    path('order/', views.order, name='dashboard-order'),
    path('logout/', user_logout, name='user-logout'),
    path('add-product/', add_product, name='add_product'),
]