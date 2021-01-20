from .  import views
from django.urls import path,include

urlpatterns = [
	path('',views.main),
	path('About',views.about),
	path('Contact',views.contact),
	path('productview/<int:myid>',views.productview),
	path('login',views.login),
	path('Grocery',views.productview),
	path('cart',views.cart),	
]
