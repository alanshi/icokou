from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'icokou.views.home', name='home'),
    #url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'recommendSystem.views.views.Index'),
    (r'^recommendSystem/', include('recommendSystem.urls', namespace='recommendSystem', app_name='recommendSystem')),
    (r'^food/', include('food.urls', namespace='food', app_name='food')),
    (r'^passport/', include('passport.urls', namespace='passport', app_name='passport')),
    
)

if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )