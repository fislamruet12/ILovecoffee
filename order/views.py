
from rest_framework import generics
from .serializer import DateSerializer, Userserializer,LoginSerializer,CoffeeSerializer,CancelSerializer,UpdateSerializer
from rest_framework import permissions
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login as django_login, logout as django_logout
from  .models import DropPost
from .datehandler import convertion
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail

def sentmail(self):
    subject = "Thank for your Ordering"
    from_email = settings.EMAIL_HOST_USER
    to_email = ['yebapeyub@youmails.online']
    message_body = "You have orderder "
    a=send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=message_body,
              fail_silently=False)
    HttpResponse(str(a))

def DaterangeView(request,owner_id,date1,date2):

    if request.method == 'GET':
        a=convertion(str(date1))
        b=convertion(str(date2))
        if a>b:
            temp=a
            a=b
            b=temp
        bt = DropPost.objects.filter(Q(owner_id=owner_id), Q(date__gte=a) & Q(date__lte=b))
        serializer=DateSerializer(bt,many=True)
        return JsonResponse(serializer.data,safe=False)

class CreateUserView(generics.CreateAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = Userserializer
    def post(self, request):
        serializer=Userserializer(data=request.data) # pass Query data from End user
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)




class LoginView(generics.CreateAPIView):

    # when login with User and password it will provide you json token

    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = LoginSerializer(data=request.data) # pass Query data from End user
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        # if token is not exists ,it will create token , if exists then it will return
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)

class SendOrderView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,) # for Testing purpose
    #permission_classes=(permissions.IsAuthenticated,)
    serializer_class = CoffeeSerializer
    def post(self, request):
        serializer = CoffeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data,status=400)

3
class UpdateOrCancelView(APIView): # update or Cancel order within 15 minutes
    permission_classes = (permissions.AllowAny,) # for testng perpose
    #permission_classes=(permissions.IsAuthenticated,)
    #serializer_class = UpdateOrCancelSerializer

    def post(self, request):    ### update order purpose
        serializer = UpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def put(self,request): #Order Cancel
        serializer = CancelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)







