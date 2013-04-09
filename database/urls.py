from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'database.views.home', name='home'),
    # url(r'^database/', include('database.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r"^$", RedirectView.as_view(url="accounts/")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^questions/", include("questions.urls")),
    url(r"^accounts/", include("accounts.urls")),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
