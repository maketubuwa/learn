from django.contrib import admin
from west.models import Character,Contact,Tag
# Register your models here.

class TagInline(admin.TabularInline):
	model=Tag
		
class ContactAdmin(admin.ModelAdmin):
	inlines=[TagInline]# Inline
	list_display=('name','age','email')#list
	search_fields=('name',)
	fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )
admin.site.register(Contact,ContactAdmin)
admin.site.register([Character])