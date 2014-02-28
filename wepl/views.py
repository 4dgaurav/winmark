from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from models import EmailForm
from models import EmailFormResume
from models import EmailFormGift
from models import EmailFormHosp
from models import EmailFormPMC

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')	

def about_us(request):
    return render(request, 'about-us.html')		
	
def corporate(request):
    return render(request, 'corporate.html')	
	
def interiors_pmc(request):
    return render(request, 'interiors-pmc.html')
	
def projects(request):
    return render(request, 'projects.html')
	
def hospitality(request):
    return render(request, 'hospitality.html')	
	
def promotions_gifting(request):
    return render(request, 'promotions-gifting.html')
	

def sendmail(request):
      if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
			  firstname = form.cleaned_data['firstname']
			  lastname = form.cleaned_data['lastname']
			  email = form.cleaned_data['email']
			  subject = form.cleaned_data['subject']
			  botcheck = form.cleaned_data['botcheck']
			  message = form.cleaned_data['message']
			  area = form.cleaned_data['area']
			  if botcheck :
				try:
				  fullemail = firstname + " " + lastname + " " + "<" + email + ">"
				  send_mail(subject, message, fullemail, ['4d.gaurav@gmail.com'])
				  return HttpResponseRedirect('/contact/thankyou/')
				except:
				  return HttpResponseRedirect('/contact/')
        else:
          return HttpResponseRedirect('/contact/')
      else:
        return HttpResponseRedirect('/contact/')
		

def sendmailgift(request):
      if request.method == 'POST':
        form = EmailFormGift(request.POST)
        if form.is_valid():
			  firstname = form.cleaned_data['firstname']
			  lastname = form.cleaned_data['lastname']
			  email = form.cleaned_data['email']
			  subject = form.cleaned_data['subject']
			  botcheck = form.cleaned_data['botcheck']
			  message = form.cleaned_data['message']
			  area = form.cleaned_data['area']
			  if botcheck :
				try:
				  fullemail = firstname + " " + lastname + " " + "<" + email + ">"
				  send_mail(subject, message, fullemail, ['4d.gaurav@gmail.com'])
				  return HttpResponseRedirect('/modalgift/thankyoumodal/')
				except:
				  return HttpResponseRedirect('/modalgift/')
        else:
          return HttpResponseRedirect('/modalgift/')
      else:
        return HttpResponseRedirect('/modalgift/')
		
		
def sendmailhosp(request):
      if request.method == 'POST':
        form = EmailFormHosp(request.POST)
        if form.is_valid():
			  firstname = form.cleaned_data['firstname']
			  lastname = form.cleaned_data['lastname']
			  email = form.cleaned_data['email']
			  subject = form.cleaned_data['subject']
			  botcheck = form.cleaned_data['botcheck']
			  message = form.cleaned_data['message']
			  area = form.cleaned_data['area']
			  if botcheck :
				try:
				  fullemail = firstname + " " + lastname + " " + "<" + email + ">"
				  send_mail(subject, message, fullemail, ['4d.gaurav@gmail.com'])
				  return HttpResponseRedirect('/modalhosp/thankyoumodal/')
				except:
				  return HttpResponseRedirect('/modalhosp/')
        else:
          return HttpResponseRedirect('/modalhosp/')
      else:
        return HttpResponseRedirect('/modalhosp/')
		
		
def sendmailpmc(request):
      if request.method == 'POST':
        form = EmailFormPMC(request.POST)
        if form.is_valid():
			  firstname = form.cleaned_data['firstname']
			  lastname = form.cleaned_data['lastname']
			  email = form.cleaned_data['email']
			  subject = form.cleaned_data['subject']
			  botcheck = form.cleaned_data['botcheck']
			  message = form.cleaned_data['message']
			  area = form.cleaned_data['area']
			  if botcheck :
				try:
				  fullemail = firstname + " " + lastname + " " + "<" + email + ">"
				  send_mail(subject, message, fullemail, ['4d.gaurav@gmail.com'])
				  return HttpResponseRedirect('/modalpmc/thankyoumodal/')
				except:
				  return HttpResponseRedirect('/modalpmc/')
        else:
          return HttpResponseRedirect('/modalpmc/')
      else:
        return HttpResponseRedirect('/modalpmc/')

		
def sendmailresume(request):
      if request.method == 'POST':
        form = EmailFormResume(request.POST, request.FILES)
        if form.is_valid():
			  firstname = form.cleaned_data['firstname']
			  lastname = form.cleaned_data['lastname']
			  email = form.cleaned_data['email']
			  subject = form.cleaned_data['subject']
			  botcheck = form.cleaned_data['botcheck']
			  message = form.cleaned_data['message']
			  attachment = request.FILES['attachment']
			  if botcheck :
				try:
				  fullemail = firstname + " " + lastname + " " + "<" + email + ">"
				  mail = EmailMessage(subject, message, fullemail, ['4d.gaurav@gmail.com'])
				  mail.attach(attachment.name, attachment.read(), attachment.content_type)
				  mail.send()
				  return HttpResponseRedirect('/careers/thankyou/')
				except:
				  return HttpResponseRedirect('/careers/')
        else:
          return HttpResponseRedirect('/careers/')
      else:
        return HttpResponseRedirect('/careers/')