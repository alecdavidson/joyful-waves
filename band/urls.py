from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

	url(r'^$', 'band.views.home', name='home'),
	url(r'^bio/', 'band.views.bio', name='bio'),
        url(r'^disc/', 'band.views.disc', name='disc'),
    # Examples:
    # url(r'^$', 'helloworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
