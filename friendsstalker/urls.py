from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_view),
    url(r'^signup$' , views.signup),
    url(r'^welcome$', views.welcome,	  ),
    url(r'^signout$', views.logout 	  ),
    url(r'^change$', views.change_view 	  ),
]
