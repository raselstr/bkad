# your_project/middleware.py
from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import logout
from django.urls import resolve
from django.template.loader import render_to_string


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URL names that do not require login
        exempt_urls = [
            'login',  # Name of your login URL
            'logout',  # Name of your logout URL
            'register',
            'password_reset',
            'admin:index',  # Admin index URL
            # Add other exempt URLs here
        ]
        
        # Allow access to exempt URLs without login
        if not request.user.is_authenticated:
            current_url_name = resolve(request.path_info).url_name
            if current_url_name not in exempt_urls:
                return redirect(settings.LOGIN_URL)
        
        response = self.get_response(request)
        return response

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        try:
            last_activity_str = request.session['last_activity']
            last_activity = datetime.strptime(last_activity_str, '%Y-%m-%d %H:%M:%S.%f')
            now = datetime.now()
            expiry = last_activity + timedelta(seconds=settings.SESSION_COOKIE_AGE)

            if now > expiry:
                logout(request)
                return redirect('login')  # Ganti dengan URL halaman login Anda
        except KeyError:
            pass

        request.session['last_activity'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        return self.get_response(request)

class SessionPingInjectorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if (
            request.user.is_authenticated and
            response.get('Content-Type', '').startswith('text/html') and
            response.status_code == 200
        ):
            try:
                content = response.content.decode('utf-8')
                ping_html = render_to_string('partials/session_ping.html')
                if '</body>' in content:
                    content = content.replace('</body>', ping_html + '</body>')
                    response.content = content.encode('utf-8')
            except:
                pass

        return response

