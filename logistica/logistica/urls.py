from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django import views

# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^home$', 'logistica.views.home', name='home'),
    #url(r'^about/', 'social.views.about', name='about'),
    #url(r'^dreams/', 'social.views.dream_info', name='dreams'),
    #url(r'^submit/', 'social.views.submit', name='submit'),
    #url(r'^dreamuser/(?P<usernamen>\w+)/$', 'social.views.dreamuser_info', name='dreamuser'),
    #url(r'^flock/', 'social.views.flock_info', name='flock'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^register/', 'social.views.register', name='register'),
    #url(r'^login/', 'social.views.user_login', name='login'),
    #url(r'^logout/$', 'social.views.user_logout', name='logout'),
    #url(r'^invalid_login/$', 'social.views.invalid_login', name='invalid_login'),
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
