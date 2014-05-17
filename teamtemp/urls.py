from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

from teamtemp.views import home, admin, submit, reset

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), 
        name='about'),
    url(r'^admin/([0-9a-zA-Z]{8})$', admin),
    url(r'^([0-9a-zA-Z]{8})$', submit),
    url(r'^reset/([0-9a-zA-Z]{8})$', reset),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
