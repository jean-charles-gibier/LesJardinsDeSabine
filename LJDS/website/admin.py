from django.contrib import admin
from website.models import Comparaison, Presentation, Evenement, Site_ami

# Register your models here.
admin.site.register(Comparaison)
admin.site.register(Presentation)
admin.site.register(Evenement)
admin.site.register(Site_ami)
