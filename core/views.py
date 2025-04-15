# core/views.py (atau app mana pun)

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def keepalive(request):
    return HttpResponse(status=204)
