from django.urls import path
from market import views

urlpatterns = [
    path('', views.index),
    path('add/',views.add),
    path('personal/',views.personal),
    path('need/',views.need),
    path('detail/<int:id>/', views.detail),
    path('delete/<int:id>/', views.delete),
    path('other/',views.other),
    path('book/',views.book),
    path('life/',views.life),
    path('cloths/',views.cloths),
    path('service/',views.service),
    path('dianqi/',views.dianqi),
    path('tech/',views.tech),
]
