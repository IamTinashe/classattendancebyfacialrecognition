from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from mysite.core import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^admin/$', core_views.admin, name='admin'),
    url(r'^panel/$', core_views.panel, name='panel'),
    url(r'^start/$', core_views.start, name='start'),
    url(r'^end/$', core_views.end, name='end'),
    url(r'^add_department/$', core_views.add_department, name='add_department'),
    url(r'^add_room/$', core_views.add_room, name='add_room'),
    url(r'^add_course/$', core_views.add_course, name='add_course'),
    url(r'^add_student/$', core_views.add_student, name='add_student'),
    url(r'^add_lecture/$', core_views.add_lecture, name='add_lecture'),
]
