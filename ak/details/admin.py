from django.contrib import admin

from details.models import Detail
# Register your models here.
class DetailAdmin(admin.ModelAdmin):

	model = Detail

admin.site.register(Detail,DetailAdmin)