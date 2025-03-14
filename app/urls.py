from django.urls import path
from .views import HomepageView, AboutpageView, ContactpageView
from .views import (
    CustomerListView,CustomerDetailView,CustomerCreateView,CustomerUpdateView,CustomerDeleteView,
    CategoryListView,CategoryDetailView,CategoryCreateView,CategoryUpdateView,CategoryDeleteView,
    ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView,
    OrderListView,OrderDetailView,OrderCreateView,OrderUpdateView,OrderDeleteView,OrderDetailListView,
    OrderDetailDetailView,OrderDetailCreateView,OrderDetailUpdateView,OrderDetailDeleteView,
)

urlpatterns = [
    
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('contact/', ContactpageView.as_view(), name='contact'),
    
    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('order/', OrderListView.as_view(), name='order'),    
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('order/', OrderListView.as_view(), name='order_list'),

    path('orderdetail/', OrderDetailListView.as_view(), name='orderdetail_list'),
    path('orderdetail/<int:pk>/', OrderDetailDetailView.as_view(), name='orderdetail_detail'),
    path('orderdetail/create/', OrderDetailCreateView.as_view(), name='orderdetail_create'),
    path('orderdetail/<int:pk>/edit/', OrderDetailUpdateView.as_view(), name='orderdetail_update'),
    path('orderdetail/<int:pk>/delete/', OrderDetailDeleteView.as_view(), name='orderdetail_delete'),

]