from django.urls import path
from django.views.generic import TemplateView
from website.views import GlobalLJDSView, do_send_mail


urlpatterns = [
    path('', GlobalLJDSView.as_view(template_name='LJDS/index.html'), name='index'),
    path('avant_apres', TemplateView.as_view(template_name='LJDS/comparison.html'), name='comparison'),
    path('contact_me', do_send_mail, name='send_mail')
]