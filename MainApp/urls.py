from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='MyAcad-home'),
    path('login_view/', views.my_login_view,name='login_view'),
    path('application/', views.application_view,name='application'),
    path('prospectus/', views.prospectus,name='prospectus'),
    path('terms/', views.terms,name='terms'),
]