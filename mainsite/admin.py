from django.contrib import admin
from .models import *

# Register your models here.


class ContactFormAdmin(admin.ModelAdmin):
    list_filter = ('status', 'subject')
    list_display = ('user_name', 'email', 'subject', 'status')


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'value', 'contact_type',)
    list_editable = ('title', 'value', 'contact_type',)


class OptionsAdmin(admin.ModelAdmin):
    list_display = ('main_title',)

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'amount', 'updated_at')
    list_filter = ('category', 'amount',)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'finish_date','duration')


admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Options, OptionsAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Portfolio)
