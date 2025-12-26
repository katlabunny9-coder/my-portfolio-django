from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.resume_view, name='resume'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_page, name='about'),
    path('resume/', views.resume_view, name='resume'),
]
