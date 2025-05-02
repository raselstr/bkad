from django.contrib import admin
from .models import OPD, Menu, SubMenu, MenuAccess, Role, UserProfile, RolePermission

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','nama')  # kolom yang tampil di list
    list_filter = ('nama',)  # filter berdasarkan nama
    ordering = ('-id',)  # urutan berdasarkan id
    list_per_page = 10  # jumlah item per halaman
    list_display_links = ('id', 'nama')  # kolom yang bisa diklik untuk edit
    
admin.site.register(OPD)
admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(MenuAccess)
admin.site.register(Role, RoleAdmin)
admin.site.register(RolePermission)
