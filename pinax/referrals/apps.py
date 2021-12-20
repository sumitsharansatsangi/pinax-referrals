import platform
from django.apps import AppConfig as BaseAppConfig
if platform.python_version() == "3.10.0":
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _

class AppConfig(BaseAppConfig):

    name = "pinax.referrals"
    verbose_name = _("Pinax Referrals")
