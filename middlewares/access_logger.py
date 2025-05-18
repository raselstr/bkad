import logging
from django.utils.deprecation import MiddlewareMixin
from user_agents import parse
from datetime import datetime, timedelta
from collections import defaultdict
from django.core.mail import send_mail
from django.conf import settings

# Logger untuk mencatat akses mencurigakan
logger = logging.getLogger("access_logger")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("access.log"),
        logging.StreamHandler()
    ]
)

# Penyimpanan sementara untuk mendeteksi anomali
access_count = defaultdict(list)
THRESHOLD = 20  # Maksimal 20 akses per menit dari IP yang sama

class AccessLoggerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        user_agent_str = request.META.get('HTTP_USER_AGENT', '')
        user_agent = parse(user_agent_str)

        ip_address = request.META.get('REMOTE_ADDR')
        if not ip_address:
            ip_address = 'unknown'

        method = request.method
        path = request.path
        now = datetime.now()

        # Bersihkan akses yang lebih dari 1 menit
        access_count[ip_address] = [
            timestamp for timestamp in access_count[ip_address]
            if now - timestamp < timedelta(minutes=1)
        ]
        access_count[ip_address].append(now)

        # Deteksi jumlah akses mencurigakan
        if len(access_count[ip_address]) > THRESHOLD:
            warning_message = (
                f"SUSPICIOUS ACCESS: IP: {ip_address}, Method: {method}, Path: {path}, "
                f"Device: {'PC' if user_agent.is_pc else 'Mobile'}, OS: {user_agent.os.family}, "
                f"Browser: {user_agent.browser.family}, Access Count: {len(access_count[ip_address])} in 1 minute"
            )
            logger.warning(warning_message)
            self.send_alert_email(warning_message)

        # Log akses normal
        log_message = (
            f"IP: {ip_address}, Method: {method}, Path: {path}, "
            f"Device: {'PC' if user_agent.is_pc else 'Mobile'}, OS: {user_agent.os.family}, Browser: {user_agent.browser.family}"
        )
        logger.info(log_message)

        return None

    def send_alert_email(self, message):
        try:
            send_mail(
                'Django Suspicious Access Alert',
                message,
                settings.EMAIL_HOST_USER,  # Akses email dari settings
                ['str.rasel83@gmail.com'],  # Email penerima
                fail_silently=False,
            )
            logger.info("Alert email sent successfully.")
        except Exception as e:
            logger.error(f"Failed to send alert email: {e}")
