from django.conf.urls import patterns, include, url
import members.views as members_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'psone_manager.views.home', name='home'),

    (r'^search/$', members_views.MemberSearch.as_view()),

)
