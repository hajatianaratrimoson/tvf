from django.contrib import admin
from etvf.models import *

from tkinter.messagebox import IGNORE

from import_export.admin import ImportExportModelAdmin
from import_export import resources, widgets
from import_export.fields import Field
# Register your models here.
from django.contrib import admin
from import_export.widgets import ForeignKeyWidget
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User

admin.site.site_header = 'TVF'


# class MovieAdmin(admin.ModelAdmin)
# list_display = ('titre', 'date_sortie')
# search_fields = ('titre','date_sortie')
# list_filter = ('date_sortie',)
# class UserResource(resources.ModelResource):
#     # def after_import(self, dataset, result, using_transactions, dry_run, **kwargs):
#     #     redirect('/')
#
#     class Meta:
#         model = User
#         skip_unchanged = True
#         report_skipped = False
#
#
# class UserAdmin(admin.ModelAdmin):
#     def response_post_save_change(self, request, obj):
#         return redirect(Fi'/')


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        skip_unchanged = True
        report_skipped = False


class KristianaResource(resources.ModelResource):
    class Meta:
        model = Kristiana
        skip_unchanged = True
        report_skipped = False


@admin.register(Kristiana)
class KristianaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = KristianaResource


class SondageResource(resources.ModelResource):
    class Meta:
        model = Sondage
        skip_unchanged = True
        report_skipped = False


@admin.register(Sondage)
class SondageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SondageResource


class MpikambanaResource(resources.ModelResource):
    class Meta:
        model = Mpikambana
        skip_unchanged = True
        report_skipped = False


@admin.register(Mpikambana)
class MpikambanaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MpikambanaResource


class TossaafiResource(resources.ModelResource):
    class Meta:
        model = Tossaafi
        skip_unchanged = True
        report_skipped = False


@admin.register(Tossaafi)
class TossaafiAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TossaafiResource


class AdidyResource(resources.ModelResource):
    class Meta:
        model = Adidy
        skip_unchanged = True
        report_skipped = False


@admin.register(Adidy)
class AdidyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AdidyResource


class KitapoResource(resources.ModelResource):
    class Meta:
        model = Kitapo
        skip_unchanged = True
        report_skipped = False


@admin.register(Kitapo)
class KitapoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = KitapoResource


class ToeranaResource(resources.ModelResource):
    class Meta:
        model = Toerana
        skip_unchanged = True
        report_skipped = False


@admin.register(Toerana)
class ToeranaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ToeranaResource


class LaminasaResource(resources.ModelResource):
    class Meta:
        model = Laminasa
        skip_unchanged = True
        report_skipped = False


@admin.register(Laminasa)
class LaminasaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LaminasaResource
