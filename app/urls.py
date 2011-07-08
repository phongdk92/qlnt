from django.conf.urls.defaults import patterns, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from app.models import User

urlpatterns = patterns('',
    # Add, remove, change personal information
    url(r'user/$', ListView.as_view(
			queryset=User.objects.all(),
			context_object_name='user_list',
			template_name='app/user/index.html')),
     url('organization/delete/(\d+)$', 'app.views.organization_delete'),
     url('schooladmin/add/$', 'app.views.school_admin_add'),
     url('list_org/$', 'app.views.list_org'),
     url(r'^change_password/$', 'app.views.change_password'),
     url(r'^change_password_done/$', 'app.views.change_password_done'),
)
