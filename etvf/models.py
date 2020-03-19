from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver


# user = models.OneToOneField(User, on_delete=models.CASCADE)


class Kristiana(models.Model):
    kody_kristiana = models.CharField(max_length=6, unique=True)
    anarana_kristiana = models.CharField(max_length=50, null=False, blank=False)
    fanampiny_kristiana = models.CharField(max_length=50, null=False, blank=False)
    finday_kristiana = models.CharField(max_length=25, null=True, blank=True)
    mailaka_kristiana = models.EmailField(null=True, blank=True)
    asa = models.CharField(max_length=250, null=True, blank=True)
    daty_nandraisana = models.DateField(null=True, blank=True)
    sary_kristiana = models.ImageField(upload_to="photos/user", null=True, blank=True)
    vola_vina = models.IntegerField(default=0, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    mpandray = models.BooleanField()
    maty = models.BooleanField()

    def __str__(self):
        return u"{0}-{1}-{2}".format(self.anarana_kristiana, self.kody_kristiana, self.fanampiny_kristiana)


class Sondage(models.Model):
    kristiana = models.OneToOneField(Kristiana, on_delete=models.CASCADE, null=True, blank=True)
    mamaky_boky = models.BooleanField()
    mahay_mivavaka = models.BooleanField()

    def __str__(self):
        return u"{0}".format(self.mamaky_boky)


class Toerana(models.Model):
    anarana_toerana = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return u"{0}".format(self.anarana_toerana)


class Mpikambana(models.Model):
    kristiana = models.ForeignKey('Kristiana', null=True, blank=True)
    tossaafi = models.ForeignKey('Tossaafi', null=True, blank=True)
    toerana = models.ForeignKey('Toerana', null=True, blank=True)
    daty_nahampikambana = models.DateField(null=True, blank=True)

    def __str__(self):
        return u"{0}-{1}-{2}".format(self.kristiana, self.tossaafi, self.toerana)


class Tossaafi(models.Model):
    kody_tossaafi = models.CharField(max_length=10, unique=True)
    anarana_tossaafi = models.CharField(max_length=50, null=True, blank=True)
    daty_nipoirany = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return u"{0}-{1}".format(self.anarana_tossaafi, self.daty_nipoirany)


class Adidy(models.Model):
    kristiana = models.ForeignKey('Kristiana', null=True, blank=True)
    toby_voalohany = models.CharField(max_length=250, null=True, blank=True)
    toby_faharoa = models.CharField(max_length=250, null=True, blank=True)
    rosia_adidy = models.CharField(max_length=25, unique=True)
    daty_nandoavana_adidy = models.DateField(null=True, blank=True)
    daty_adidy_1 = models.DateField(null=False, blank=False)
    daty_adidy_2 = models.DateField(null=True, blank=True)
    vola_adidy = models.IntegerField(default=0, null=False, blank=False)
    totaly_adidy = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return u"{0}-{1}".format(self.rosia_adidy, self.vola_adidy)


class Kitapo(models.Model):
    kristiana = models.ForeignKey('Kristiana', null=True, blank=True)
    toby_voalohany = models.CharField(max_length=250, null=True, blank=True)
    toby_faharoa = models.CharField(max_length=250, null=True, blank=True)
    rosia_kitapo = models.CharField(max_length=25, unique=True)
    daty_nandoavana_kitapo = models.DateField(null=True, blank=True)
    daty_kitapo_1 = models.DateField(null=False, blank=False)
    daty_kitapo_2 = models.DateField(null=True, blank=True)
    vola_kitapo = models.IntegerField(default=0, null=False, blank=False)
    totaly_vola = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return u"{0}-{1}".format(self.rosia_kitapo, self.vola_kitapo)


class Budget(models.Model):
    laminasa = models.ForeignKey('Laminasa', null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)


class Laminasa(models.Model):
    tossaafi = models.ForeignKey('Tossaafi', null=True, blank=True)
    daty_laminasa = models.DateTimeField(blank=False, null=False)
    asa = models.CharField(max_length=250, null=False, blank=False)
    toerana = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return u"{0}".format(self.daty_laminasa)
