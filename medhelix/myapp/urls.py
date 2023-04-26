from django.urls import path
from.import views



urlpatterns = [
   
    path('upload/', views.add, name='base'),
    path('search/', views.search_prescription, name='search'),
    path("register",views.RegistrationView.as_view(),name="register"),
    path("",views.LoginView.as_view(),name="signin"),
    path('home/', views.home, name='home'),
    path("",views.LoginView.as_view(),name="signout"),





]