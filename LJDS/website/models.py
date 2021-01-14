from django.db import models
import datetime
class Comparaison(models.Model):
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    FOURTH = '4'
    FIFTH = '5'
    SIXTH = '6'
    OTHER = '-1'

    PLACEMENT_CHOICES = [
        (FIRST  , 'Premier'),
        (SECOND , 'Second'),
        (THIRD  , 'Troisieme'),
        (FOURTH , 'Quatrieme'),
        (FIFTH  , 'Cinquieme'),
        (SIXTH  , 'Sixieme'),
        (OTHER , 'Invisible'),
    ]
    position = models.CharField(
        max_length=2,
        choices=PLACEMENT_CHOICES,
        default=FIRST,
    )
    #TODO determiner dynamiquement static localisarion
    path_media = "static/dist/assets/img/realisations/comparisons"
    titre = models.CharField(max_length=255)
    titre_thumb = models.CharField(max_length=255)
    intro = models.TextField(max_length=1200)
    redactionnel = models.TextField(max_length=8000)
    intro_thumb = models.TextField(max_length=1200)
    photo_avant = models.ImageField(upload_to=path_media)
    photo_apres = models.ImageField(upload_to=path_media)
    photo_thumb = models.ImageField(upload_to=path_media)
    date = models.DateField(auto_now_add = True)


class Presentation(models.Model):
    titre = models.CharField(max_length=255)
    intro = models.TextField(max_length=1200)
    content = models.TextField(max_length=8000)
    published = models.BooleanField()
    date = models.DateField(auto_now_add = True)

class Evenement(models.Model):
    titre = models.CharField(max_length=255)
    intro = models.TextField(max_length=1200)
    logo_1 = models.CharField(max_length=255)
    titre_1 = models.CharField(max_length=255)
    intro_1 = models.TextField(max_length=1200)
    logo_2 = models.CharField(max_length=255)
    titre_2 = models.CharField(max_length=255)
    intro_2 = models.TextField(max_length=1200)
    logo_3 = models.CharField(max_length=255)
    titre_3 = models.CharField(max_length=255)
    intro_3 = models.TextField(max_length=1200)
    published = models.BooleanField()
    date = models.DateField(auto_now_add = True)

class Site_ami(models.Model):
    #TODO determiner dynamiquement static localisarion
    path_media = "static/dist/assets/img/realisations/comparisons"

    sa_titre = models.CharField(max_length=255)
    sa_intro = models.TextField(max_length=1200)

    sa_photo_1 = models.ImageField(upload_to=path_media)
    sa_logo_1 = models.CharField(max_length=255)
    sa_titre_1 = models.CharField(max_length=255)
    sa_intro_1 = models.TextField(max_length=1200)
    sa_link_1_1 = models.TextField(max_length=400)
    sa_link_1_2 = models.TextField(max_length=400)
    sa_link_1_3 = models.TextField(max_length=400)

    sa_photo_2 = models.ImageField(upload_to=path_media)
    sa_logo_2 = models.CharField(max_length=255)
    sa_titre_2 = models.CharField(max_length=255)
    sa_intro_2 = models.TextField(max_length=1200)
    sa_link_2_1 = models.TextField(max_length=400)
    sa_link_2_2 = models.TextField(max_length=400)
    sa_link_2_3 = models.TextField(max_length=400)

    sa_photo_3 = models.ImageField(upload_to=path_media)
    sa_logo_3 = models.CharField(max_length=255)
    sa_titre_3 = models.CharField(max_length=255)
    sa_intro_3 = models.TextField(max_length=1200)
    sa_link_3_1 = models.TextField(max_length=400)
    sa_link_3_2 = models.TextField(max_length=400)
    sa_link_3_3 = models.TextField(max_length=400)
    published = models.BooleanField()
