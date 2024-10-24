from django.urls import path
from bollywood import views

urlpatterns=[
    path('mlist',views.func1,name='p1'),
]