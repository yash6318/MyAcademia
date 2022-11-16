from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='stud-home'),
    path('stud_attendance/',views.attendance,name='stud_att'),
    path('stud_marks/',views.marks,name='stud_marks'),
    path('stud_subjects/',views.subj,name='stud_subj'),
]