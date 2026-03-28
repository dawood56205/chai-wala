from django.contrib import admin
from .models import *
# Register your models here.

class ChaiReviewInline(admin.TabularInline):
  model = chai_review
  extra = 2

class chaivarietyadmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'date_added')
  inlines = [ChaiReviewInline]

class storeadmin(admin.ModelAdmin):
  list_display = ('name', 'location')
  filter_horizontal = ['chai_varieties']

class chaicertificateadmin(admin.ModelAdmin):
  list_display = ('chai', 'certificate_number')

admin.site.register(CHAIVARIETY, chaivarietyadmin)
admin.site.register(stores, storeadmin )
admin.site.register(chai_certificate, chaicertificateadmin )

