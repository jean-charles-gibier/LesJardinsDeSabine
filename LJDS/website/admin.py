from django.contrib import admin
from website.models import Comparaison, Presentation, Evennement, Site_ami

# Register your models here.
admin.site.register(Comparaison)
admin.site.register(Presentation)
admin.site.register(Evennement)
admin.site.register(Site_ami)
