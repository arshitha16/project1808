from django.conf.urls import include,url
from mycontacts import views
urlpatterns=[
        url(r'mail.*',views.mail,name='mail'),
        url(r'number.*',views.number,name='number'),
        ]
