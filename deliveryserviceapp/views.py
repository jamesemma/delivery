from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages
from django.http import HttpResponse
from .models import *

from django.conf import settings

from .forms import ContactForm

# Create your views here.

def home(request):
	context={}
	return render(request, 'deliveryserviceapp/home.html', context)

def track(request):
	context={}
	return render(request, 'deliveryserviceapp/track.html', context)

def trackerinfo(request):

	if request.method == 'POST':
		Trackingid= request.POST['trackingid']
		Trackinginfos= UsersTracker.objects.filter(Tracking_id=Trackingid)

	else:
		return redirect('/')

	context={
			'Trackinginfos': Trackinginfos,
		}

	return render(request, 'deliveryserviceapp/trackerinfo.html', context)

def aboutus(request):
	return render(request, 'deliveryserviceapp/aboutus.html')


def contact(request):

	form= ContactForm()
	if request.method=='POST':
		form= ContactForm(request.POST)

		if form.is_valid():
			#send message
			name= form.cleaned_data['name']

			email= form.cleaned_data['email']

			message= form.cleaned_data['message']

			send_mail('Web contact',
				message,
				email,
				['delivery10@protonmail.com']

				)


			messages.success(request, 'Thanks for contacting us, we will get back to you soon.')

		else:
			form= ContactForm()
	
	context={'form':form}

	return render(request, 'deliveryserviceapp/contactus.html', context)





	
	



