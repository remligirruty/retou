from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as myloginview

urlpatterns = [
    url(r'^$', myloginview.login, {'template_name':'login.html'}, name='login'),
    url(r'^admin/', include(admin.site.urls)),
]
