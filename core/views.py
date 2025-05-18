# core/views.py (atau app mana pun)

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse

@login_required
def keepalive(request):
    return HttpResponse(status=204)


def test_email(request):
    try:
        send_mail(
            'Test Email Django',
            'Ini adalah email uji coba dari aplikasi Django Anda.',
            'your_email@gmail.com',  # From
            ['recipient@example.com'],  # To
            fail_silently=False,
        )
        return HttpResponse("Email berhasil dikirim!")
    except Exception as e:
        return HttpResponse(f"Gagal mengirim email: {e}")
