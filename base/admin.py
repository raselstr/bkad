from django.contrib import admin
from .models import OPD, Menu, SubMenu, MenuAccess, Role, UserProfile, RolePermission

admin.site.register(OPD)
admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(MenuAccess)
admin.site.register(Role)
admin.site.register(RolePermission)
