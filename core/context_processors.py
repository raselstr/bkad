from datetime import datetime

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
