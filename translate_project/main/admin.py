from django.contrib import admin
from . import models
from .models import Availability, Projects, Activities, Translations, Checks, Mistakes, Replacement


# Register your models here.
@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('user', 'startTime', 'endTime')
    search_fields = ('user',)
    ordering = ('-pk',)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('projectName',)
    search_fields = ('projectName',)
    ordering = ('-pk',)


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('project', 'activityName')
    search_fields = ('activityName',)
    ordering = ('-pk',)


@admin.register(Translations)
class TranslationsAdmin(admin.ModelAdmin):
    list_display = ('activity', 'user', 'textVolume', 'completionPercentage')
    search_fields = ('activity', 'user',)
    ordering = ('-pk',)

@admin.register(Checks)
class ChecksAdmin(admin.ModelAdmin):
    list_display = ('translation', 'checkResult')
    search_fields = ('translation',)
    ordering = ('-pk',)

@admin.register(Mistakes)
class MistakesAdmin(admin.ModelAdmin):
    list_display = ('translation', 'mistakeDescription')
    search_fields = ('translation',)
    ordering = ('-pk',)

@admin.register(Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('translation', 'replacementDate')
    search_fields = ('translation',)
    ordering = ('-pk',)