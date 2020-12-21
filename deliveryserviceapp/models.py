from django.db import models

# Create your models here.

class UsersTracker(models.Model):
	CATEGORY= (

		('Air', 'Air'), 

		('Sea', 'Sea'), 

		('Rail', 'Rail'),

		('Road', 'Road'),

		)

	STATUS= (

		('Pending', 'Pending'), 

		('Out for delivery', 'Out for delivery'), 

		('Delivered', 'Delivered'),

		)


	Name= models.CharField(max_length=200, null=True, blank=True)
	phone= models.CharField(max_length=200, null=True, blank=True)
	email= models.CharField(max_length=200, null=True, blank=True)
	Tracking_id= models.CharField(max_length=200, null=True, blank=True)
	Deliveryaddress=models.CharField(max_length=700, null=True, blank=True)
	Deliverymethod= models.CharField(max_length=200, null=True, blank=True, choices=CATEGORY)
	Deliverystatus= models.CharField(max_length=200, null=True, blank=True, choices=STATUS)
	Currentlocation= models.CharField(max_length=600, null=True, blank=True)
	Deliverydescription= models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.Name
