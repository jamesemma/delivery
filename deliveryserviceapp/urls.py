from django.urls import path
from . import views

urlpatterns=[
	path('', views.home, name='home'),
	path('aboutus/', views.aboutus, name='aboutus'),
	path('track/', views.track, name='track'),
	path('trackerinfo/', views.trackerinfo, name='trackerinfo'),
	path('contact_us/', views.contact, name='contact_us')
]