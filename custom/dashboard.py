from django.utils.translation import ugettext_lazy as _

import horizon


class Custom(horizon.Dashboard):
    name = _("Custom")
    slug = "custom"
    panels = ('hello' , 'tables' )  # Add your panels here.
    default_panel = 'hello'  # Specify the slug of the dashboard's default panel.


horizon.register(Custom)
