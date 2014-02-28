from django.conf.urls import patterns, include, url
from wepl.views import home, about_us, interiors_pmc, projects, corporate, hospitality, promotions_gifting
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from wepl import settings
from django.views.generic.base import TemplateView
from views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'wepl.views.home', name='home'),
	url(r'^about-us/$', about_us),
	url(r'^corporate/', corporate),
	url(r'^interiors-pmc/', interiors_pmc),
	url(r'^projects/', projects),
	url(r'^hospitality/', hospitality),
	url(r'^promotions-gifting/', promotions_gifting),
	
	url(r'^modalhosp/send/$', sendmailhosp),
	url(r'^modalhosp/thankyoumodal/$', TemplateView.as_view(template_name='thankyoumodal.html'), name='thankyoumodal'),
	url(r'^modalhosp/$', TemplateView.as_view(template_name='modalhosp.html'), name='modalhosp'),
	
	url(r'^modalpmc/send/$', sendmailpmc),
	url(r'^modalpmc/thankyoumodal/$', TemplateView.as_view(template_name='thankyoumodal.html'), name='thankyoumodal'),
	url(r'^modalpmc/$', TemplateView.as_view(template_name='modalpmc.html'), name='modalpmc'),
	
	url(r'^modalgift/send/$', sendmailgift),
	url(r'^modalgift/thankyoumodal/$', TemplateView.as_view(template_name='thankyoumodal.html'), name='thankyoumodal'),
	url(r'^modalgift/$', TemplateView.as_view(template_name='modalgift.html'), name='modalgift'),
	
	url(r'^contact/send/$', sendmail),
	url(r'^contact/thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
	url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
	
	url(r'^careers/send/$', sendmailresume),
	url(r'^careers/thankyou/$', TemplateView.as_view(template_name='thankyou.html'), name='thankyou'),
	url(r'^careers/$', TemplateView.as_view(template_name='careers.html'), name='careers'),
	)

urlpatterns += staticfiles_urlpatterns()

