from django.conf import settings
from django.core.cache import cache
from django.contrib.admin import widgets    
from django.shortcuts import get_object_or_404 
from django.db import models
from django import forms

class EmailFormResume(forms.Form):
	  firstname = forms.CharField(max_length=255)
	  lastname = forms.CharField(max_length=255)
	  email = forms.EmailField()
	  subject = forms.CharField(max_length=255)
	  botcheck = forms.BooleanField(required=True)
	  message = forms.CharField()
	  attachment = forms.Field(label='Resume', widget = forms.FileInput,    required = True )
	  
class EmailForm(forms.Form):
	  firstname = forms.CharField(max_length=255)
	  lastname = forms.CharField(max_length=255)
	  email = forms.EmailField()
	  subject = forms.CharField(max_length=255)
	  botcheck = forms.BooleanField(required=True)
	  message = forms.CharField()
	  area = forms.CharField()
	  
	  
class EmailFormHosp(forms.Form):
	  firstname = forms.CharField(max_length=255)
	  lastname = forms.CharField(max_length=255)
	  email = forms.EmailField()
	  subject = forms.CharField(max_length=255)
	  botcheck = forms.BooleanField(required=True)
	  message = forms.CharField()
	  area = forms.CharField()
	  
	  
class EmailFormGift(forms.Form):
	  firstname = forms.CharField(max_length=255)
	  lastname = forms.CharField(max_length=255)
	  email = forms.EmailField()
	  subject = forms.CharField(max_length=255)
	  botcheck = forms.BooleanField(required=True)
	  message = forms.CharField()
	  area = forms.CharField()
	  
class EmailFormPMC(forms.Form):
	  firstname = forms.CharField(max_length=255)
	  lastname = forms.CharField(max_length=255)
	  email = forms.EmailField()
	  subject = forms.CharField(max_length=255)
	  botcheck = forms.BooleanField(required=True)
	  message = forms.CharField()
	  area = forms.CharField()