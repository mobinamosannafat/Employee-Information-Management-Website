from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/',include('employees.urls')),
    path('accounts/',include('accounts.urls')),
    path('about/', views.about),
    path('',account_views.login_view,name="home"),
]


urlpatterns += staticfiles_urlpatterns()

#from django.conf.urls import url, include
#from django.contrib import admin
#from . import views
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from accounts import views as account_views

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#    url(r'^employees/', include('employees.urls')),
#    url(r'^accounts/', include('accounts.urls')),
#    url(r'^about/$', views.about),
#    url(r'^$', account_views.login_view,name="home"),
#]

#urlpatterns += staticfiles_urlpatterns()


