
from order import views
from  django.conf.urls import url ,include
urlpatterns = [

   url('sendmail/',views.sentmail),
   url('register/',views.CreateUserView.as_view()),
   url('login/',views.LoginView.as_view()),
   url('logout/',views.LogoutView.as_view()),
   url('order/',views.SendOrderView.as_view()),
   url('update/',views.UpdateOrCancelView.as_view()),
   url(r'^posts/(?P<owner_id>\d+)/(?P<date1>[-\w]+)/(?P<date2>[-\w]+)/$', views.DaterangeView, name='post'),
   #  url format with post :   http://127.0.0.1:8000/lovecoffee/posts/1/2019-01-11/2019-01-14/
   #                           http://127.0.0.1:8000/lovecoffee/posts/owner_id/date1/date2/


]
