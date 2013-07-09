from django.utils.translation import ugettext_lazy as _

import horizon

from custom import dashboard


class Hello(horizon.Panel):
    name = _("Hello")
    slug = "hello"


dashboard.Custom.register(Hello)
