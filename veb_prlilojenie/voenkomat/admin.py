from django.contrib import admin
from .models import Conscript, MedicalInfo, DraftCampaign

@admin.register(Conscript)
class ConscriptAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'birth_date', 'status', 'phone')
    search_fields = ('last_name', 'first_name', 'middle_name')
    list_filter = ('status', 'gender')

@admin.register(MedicalInfo)
class MedicalInfoAdmin(admin.ModelAdmin):
    list_display = ('conscript', 'fitness_category')
    search_fields = ('conscript__last_name', 'conscript__first_name')

@admin.register(DraftCampaign)
class DraftCampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    filter_horizontal = ('conscripts',)