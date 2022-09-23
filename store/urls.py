from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import Login, Register


urlpatterns = [
	path('login/', Login.as_view(), name='login'),
	path('logout/', LogoutView.as_view(next_page='store'), name='logout'),
	path('register/', Register.as_view(), name='register'),

	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('info/<int:id>', views.info, name="info"),

	path('update_item/', views.update_item, name="update_item"),
	path('process_order/', views.process_order, name="process_order"),

]
