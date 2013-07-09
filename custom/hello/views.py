from horizon import views

class IndexView(views.APIView):
    # A very simple class-based view...
    template_name = 'custom/hello/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context

class MsgView(IndexView):
    def get_data(self, request, context, *args, **kwargs):
        context["hello_msg"]="hello %s." % self.kwargs["msg"]

        from django.conf import settings
        context["keystone_url"] ='<a href="{0}">{0}</a><br />'.format(
                        getattr(settings,"OPENSTACK_KEYSTONE_URL" , None ),)
        return context

