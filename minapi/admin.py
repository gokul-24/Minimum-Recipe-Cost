from django.contrib import admin
from .models import *
# Register your models here.
class StoresAdmin(admin.ModelAdmin):
    fields=['name',('flour','discount_flour'),('rice','discount_rice'),('eggs','discount_eggs'),('sugar','discount_sugar'),('salt','discount_salt'),('vegetables','discount_vegetables')]
    exclude = ('after_discount_flour','after_discount_rice','after_eggs','after_discount_sugar','after_discount_salt','after_discount_vegetalbes',)
admin.site.register(Stores,StoresAdmin)

admin.site.register(Recipe)