from django.db import models

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
    path_media = "static/dist/assets/img/realisations/comparisons"
    titre = models.CharField(max_length=255)
    intro = models.TextField(max_length=1200)
    photo_avant = models.ImageField(upload_to=path_media)
    photo_apres = models.ImageField(upload_to=path_media)


class Presentation(models.Model):
    titre = models.CharField(max_length=255)
    intro = models.TextField(max_length=1200)
    content = models.TextField(max_length=8000)
    published = models.BooleanField()

class Evennement(models.Model):
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

class Site_ami(models.Model):
    sa_titre = models.CharField(max_length=255)
    sa_intro = models.TextField(max_length=1200)
    sa_logo_1 = models.CharField(max_length=255)
    sa_titre_1 = models.CharField(max_length=255)
    sa_intro_1 = models.TextField(max_length=1200)
    sa_link_1_1 = models.TextField(max_length=400)
    sa_link_1_2 = models.TextField(max_length=400)
    sa_link_1_3 = models.TextField(max_length=400)
    sa_logo_2 = models.CharField(max_length=255)
    sa_titre_2 = models.CharField(max_length=255)
    sa_intro_2 = models.TextField(max_length=1200)
    sa_link_2_1 = models.TextField(max_length=400)
    sa_link_2_2 = models.TextField(max_length=400)
    sa_link_2_3 = models.TextField(max_length=400)
    sa_logo_3 = models.CharField(max_length=255)
    sa_titre_3 = models.CharField(max_length=255)
    sa_intro_3 = models.TextField(max_length=1200)
    sa_link_3_1 = models.TextField(max_length=400)
    sa_link_3_2 = models.TextField(max_length=400)
    sa_link_3_3 = models.TextField(max_length=400)
    published = models.BooleanField()
