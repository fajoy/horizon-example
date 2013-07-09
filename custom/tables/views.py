from horizon import tables
class IndexTable(tables.DataTable):
    class Meta:
        name = "Table Example"
    _id = tables.Column("id")
    _msg = tables.Column("msg" ,
                        verbose_name="hello_msg" ,
                        link="horizon:custom:hello:hello_msg" ,)

    def get_object_id(self, datum):
        return datum["id"]
    def get_object_display(self, datum):
        return datum["id"]

class IndexView(tables.DataTableView):
    table_class = IndexTable
    template_name = 'custom/tables/index.html'
    def get_data(self):
        data = [{"id":0,"msg":"test",}
                ,{"id":1,"msg":"test1" ,}]
        return  data


from horizon import workflows,forms
from django.utils.translation import ugettext_lazy as _

class MyAction(workflows.Action):
    f1 = forms.Field(label=("Field1"),
                     required=False,
                     help_text="Hello help text", )
    def handle(self, request, data):
        return True

    class Meta:
        name = "MyAction"

class Step(workflows.Step):
    action_class = MyAction
    contributes = ("f1",)

    def contribute(self, data, context):
        request = self.workflow.request
        context ['msg'] = data.get("f1", "")
        return context



class Workflow(workflows.Workflow):
    slug = "workflow"
    name = "MyDataWorkFlow"
    finalize_button_name = "Save"
    success_message = 'success_message"%s".'
    failure_message = 'failure_message "%s".'
    success_url = "horizon:custom:tables:data"
    default_steps = (Step,)
    def format_status_message(self, message):
        return message % self.context.get('id', 'unknown')

    def handle(self, request, context):
        import uuid
        new_id = str(uuid.uuid1())
        msg= context.get("msg", "")
        if not request.session.has_key("mydata"):
            request.session["mydata"] = {}
        data=request.session["mydata"]
        data[new_id] = {"id":new_id,"msg":msg ,}
        return True

class WorkflowView(workflows.WorkflowView):
    workflow_class = Workflow

    def get_initial(self):
        initial = super(WorkflowView, self).get_initial()
        return initial

class BtnCreate(tables.LinkAction):
    name = "create"
    verbose_name = "Create"
    url = "horizon:custom:tables:create"
    classes = ("ajax-modal", "btn-create")

from django import shortcuts
class BtnDelete(tables.BatchAction):
    name = "delete"
    action_present = "Delete"
    action_past = "Delete of"
    data_type_singular = "item"
    data_type_plural = "data"
    classes = ('btn-danger', 'btn-terminate')

    def __init__(self):
        super(BtnDelete, self).__init__()

    def allowed(self, request, datum=None):
        return True

    def action(self, request, obj_id):
        request.session.get("mydata",{})
        del request.session["mydata"][obj_id]
        return shortcuts.redirect(self.get_success_url(request))

    def get_success_url(self, request=None):
        return request.get_full_path()

class DataTable(tables.DataTable):
    class Meta:
        name = "Data Example"
        table_actions = ( BtnCreate , BtnDelete )

    _id = tables.Column("id")
    _msg = tables.Column("msg" ,
                        verbose_name="hello_msg" ,
                        link="horizon:custom:hello:hello_msg" ,)

    def get_time(datum):
        import time,datetime
        return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    time = tables.Column(get_time ,
                        verbose_name="Time" ,)

    def get_object_id(self, datum):
        return datum["id"]
    def get_object_display(self, datum):
        return datum["msg"]

class DataView(IndexView):
    table_class = DataTable
    def get_data(self):
        data=self.request.session.get("mydata",{})
        return  data.values()
