from django.utils.translation import ugettext_lazy as _

import horizon

from custom import dashboard


class Tables(horizon.Panel):
    name = _("Tables")
    slug = "tables"


dashboard.Custom.register(Tables)
