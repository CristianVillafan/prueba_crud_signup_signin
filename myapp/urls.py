from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('orders/', views.orders, name='orders'),
    path('create_order/', views.create_order, name='create_order'),
    path('orders/<int:id>/', views.order_detail, name='order_detail'),
    path('orders/<int:id>/edit', views.order_edit, name='order_edit'),
    path('orders/<int:id>/delete', views.order_delete, name='order_delete'),
    path('whoarewe/', views.whoarewe, name='whoarewe'),
    path('printing_course/', views.printing_course, name='printing_course'),
    path('maintenance_course/', views.maintenance_course, name='maintenance_course')
]
