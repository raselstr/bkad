from datetime import datetime
from base.models import Menu, SubMenu, RolePermission, MenuAccess

def global_year_context(request):
    current_year = datetime.now().year

    # Ambil dari query string (kalau ada)
    selected_year = request.GET.get("year")

    if selected_year:
        try:
            selected_year = int(selected_year)
            request.session["selected_year"] = selected_year
        except ValueError:
            selected_year = request.session.get("selected_year", current_year)
    else:
        # Kalau tidak ada di URL, ambil dari session
        selected_year = request.session.get("selected_year", current_year)

    year_list = range(current_year - 5, current_year + 1)

    return {
        "year_list": year_list,
        "current_year": selected_year,
    }



def role_menus(request):
    if request.user.is_authenticated:
        # Mengambil role yang dimiliki pengguna
        user_roles = MenuAccess.objects.filter(user=request.user).values_list('role', flat=True)
        
        # Mengambil menu dan submenu yang diizinkan berdasarkan role
        permissions = RolePermission.objects.filter(role__in=user_roles, can_view=True).select_related('menu', 'submenu')

        # Mengelompokkan menu dan submenu
        menu_dict = {}
        for perm in permissions:
            menu_name = perm.menu.nama
            menu_icon = perm.menu.ikon
            submenu_name = perm.submenu.nama if perm.submenu else None
            submenu_url = perm.submenu.url if perm.submenu else None
            # submenu_icon = perm.submenu.icon if perm.submenu else None

            if menu_name not in menu_dict:
                menu_dict[menu_name] = {
                    'menu_name': menu_name,
                    'menu_icon': menu_icon,
                    'submenus': []
                }

            if submenu_name:
                menu_dict[menu_name]['submenus'].append({
                    'name': submenu_name,
                    'url': submenu_url,
                    # 'icon': submenu_icon
                })

        # Konversi ke daftar agar mudah diproses di template
        menus = list(menu_dict.values())
        return {'role_menus': menus}

    return {'role_menus': []}



def global_context(request):
    """Menggabungkan semua fungsi context dalam satu context processor."""
    context = {}

    # Gabungkan hasil dari setiap fungsi
    context.update(global_year_context(request))
    context.update(role_menus(request))

    return context