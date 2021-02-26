from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import BadHeaderError, send_mail
from website.models import Comparaison, Presentation, Evenement, Site_ami
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
import os

class GlobalLJDSView(TemplateView):
    template_path = 'LJDS/index.html'

    def get_context_data(self, **kwargs):
        context = super(GlobalLJDSView, self).get_context_data(**kwargs)
# A refactorer

        comparaison1= Comparaison.objects.filter(position="1")
        if len(comparaison1) > 0:
            context['comparaison1'] = comparaison1[0]

        comparaison2= Comparaison.objects.filter(position="2")
        if len(comparaison2) > 0:
            context['comparaison2'] = comparaison2[0]

        comparaison3= Comparaison.objects.filter(position="3")
        if len(comparaison3) > 0:
            context['comparaison3'] = comparaison3[0]

        comparaison4= Comparaison.objects.filter(position="4")
        if len(comparaison4) > 0:
            context['comparaison4'] = comparaison4[0]

        comparaison5= Comparaison.objects.filter(position="5")
        if len(comparaison5) > 0:
            context['comparaison5'] = comparaison5[0]

        comparaison6= Comparaison.objects.filter(position="6")
        if len(comparaison6) > 0:
            context['comparaison6'] = comparaison6[0]

        presentation= Presentation.objects.filter(published=True)
        if len(presentation) > 0:
            context['presentation'] = presentation[0]

        evenements = Evenement.objects.all()
        if len(evenements) > 0:
            context['evenements'] = evenements[0]

        sites_amis = Site_ami.objects.all()
        if len(sites_amis) > 0:
            context['sites_amis'] = sites_amis[0]

        return context

@never_cache
@csrf_protect
def do_send_mail(request):
    if request.method =='POST':
#        pprint.pprint(request.POST)
        email = request.POST['email']
        message =  request.POST['message']
        name =  request.POST['name']
        phone = request.POST['phone']
        destinataire = os.environ.get('EMAIL_DESTINATAIRE')

        send_mail(
            'Contact envoyé depuis lescouleursdesabine.fr',
            """
Bonjour,
Un visteur a rempli le formulaire de contact avec les informations suivantes :

Email': {}
Message': 
 -------------------
{}
 -------------------
Nom: {}
Telephone: {}

Bonne réception !
Votre Serveur WEB.
            """.format(email, message, name, phone),
            'slescouleursdesabine@gmail.com',
            [destinataire],
            fail_silently=False,
            )
        return HttpResponse()
