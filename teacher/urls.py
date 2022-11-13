from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.home,name='teacher-home'),
    path('my_class/',views.my_class,name='teach_class'),
    path('teach_attendance/',views.attendance,name='teach_att'),
    path('teach_marks/',views.marks,name='teach_marks'),
]