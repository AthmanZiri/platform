<<<<<<< HEAD
from django.conf.urls import url, include
=======
from django.conf.urls import url
>>>>>>> 6530ec01b4f0dd6191f3bf80c32cb89c860de185
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^accounts/', include('users.urls')),
    url(r'^milestones/', include('milestones.urls')),
=======
>>>>>>> 6530ec01b4f0dd6191f3bf80c32cb89c860de185
]

admin.site.site_title = 'Mentor001 Adminstration'
admin.site.site_header = 'Mentor001 Adminstration'
