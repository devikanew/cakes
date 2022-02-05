from django.urls import path
from . import views
app_name="cakeapp"
urlpatterns = [
    path('', views.allCake, name='allCake'),
    path('towns/', views.towns, name='towns'),
    path('cities/', views.cities, name='cities'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('logout/', views.logout, name='logout'),

]