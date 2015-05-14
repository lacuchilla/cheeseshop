from django.conf.urls import include, url
from django.contrib import admin

#urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
#]
urlpatterns = [
    #url(r'^$', 'cheeseshop.views.home', name='home'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^orders/', include('orders.urls', namespace="orders")),
    url(r'^admin/', include(admin.site.urls)),
]
