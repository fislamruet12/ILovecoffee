

from django.contrib import admin
from django.urls import path,include
from order import views,urls

from  django.conf.urls import url ,include
urlpatterns = [

   url('lovecoffee/',include('order.urls')),
   #url('sendmail/',views.sentmail), just checking purpose
   url('admin/', admin.site.urls),

]
