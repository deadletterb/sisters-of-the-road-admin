from django.contrib import admin

# Register your models here.
from .models import BarterEvent
from .models import BarterAccount


class BarterEventAdmin(admin.ModelAdmin):
	list_display = [
		'event_id',
		'customer_name',
		'event_type',
		'event_time',
		'transaction_amount',
		]
	
	list_filter = ['event_type', 'event_time']

	def event_id(self, obj):
		return obj.id


class BarterAccountAdmin(admin.ModelAdmin):
	list_display = ['customer_name', 'account_balance']
	fields = ['customer_name','balance','last_add','last_subtract']
	readonly_fields = ['last_add','last_subtract']
	
admin.site.site_header = 'Sisters of the Road Cafe Admin'
admin.site.index_title = 'Sisters of the Road Checkout Administration'
admin.site.register(BarterAccount, BarterAccountAdmin)
admin.site.register(BarterEvent, BarterEventAdmin) 