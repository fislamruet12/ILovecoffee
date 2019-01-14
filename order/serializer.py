from rest_framework import serializers
from django.contrib.auth.models import User
from django.core import exceptions
from .models import DropPost
from django.conf import  settings
from .datehandler import getMinute
import requests
from django.core.mail import send_mail
from order import backeneds
class Userserializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True) # prevent to showing the password field in json
    def validate(self, data):
        username=data.get("username","")
        email = data.get("email", "")
        password = data.get("password", "")
        firstname=data.get("first_name","")
        lastname=data.get("last_name","")
        user=User.objects.filter(email=email).order_by('id').first()
        if user:
            raise exceptions.ValidationError(user.email +" is already exists try another")
        else:
            user=User.objects.create(username=username,first_name=firstname,last_name=lastname,email=email)
            user.set_password(password)
            user.save()
            return user
    class Meta:
        model=User
        fields = ('id','username','first_name','last_name','email','password')



class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ('email', 'password')

    password = serializers.CharField()
    email=serializers.CharField()

    def validate(self, data):
        email=data.get("email","")
        password = data.get("password", "")

        if email and password:
            user = backeneds.authenticate(username=email, password=password)
             # authenticate the user using email address
            if user:
                data["user"] = user
            else:
                msg = "Unable to login with given credentials."
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise exceptions.ValidationError(msg)
        return data




class CoffeeSerializer(serializers.ModelSerializer):


    class Meta:
        model=DropPost
        fields = ('id','coffeename','coffeeamount','place','owner')

    coffeename=serializers.CharField()
    coffeeamount=serializers.IntegerField()

    def validate(self, data):
        email=data.get("email","yebapeyub@youmails.online")
        coffeename=data.get("coffeename","")
        coffeeamount=data.get("coffeeamount","")
        owner=data.get("owner","")
        pnt=""
        if coffeename:
            x=1
        else:
            raise exceptions.ValidationError("Coffeename field is required")
        if coffeeamount:
            x=1
        else:
            raise exceptions.ValidationError("number of Coffee field is required")
        if coffeename and coffeeamount:
            res = requests.get('https://ipinfo.io/')
            if res:
                locdata = res.json()
                # generrate the user's ip address related all information like city,longitude,latidude, etc in json format
                location = locdata['loc'].split(',')
                latitude = location[0]
                longitude = location[1]
                pnt = 'POINT(' + str(latitude) + ' , ' + str(longitude) + ')'
            else:
                raise exceptions.ValidationError("Ensure yout internet connection")

        cofi=DropPost.objects.create(coffeename=coffeename,coffeeamount=coffeeamount,place=pnt, owner=owner)
        cofi.save()

        """
        subject="Thank for your Ordering"
        from_email=settings.EMAIL_HOST_USER
        to_email=['yebapeyub@youmails.online']
        message_body="You have orderder "+ str(cofi.coffeename)+" and the amount of coffee is  "+str(cofi.coffeeamount)
        send_mail(subject=subject,from_email=from_email,recipient_list=to_email,message=message_body,fail_silently=False)
        """
        return cofi



class UpdateSerializer(serializers.Serializer):

    id=serializers.IntegerField()
    coffeeamount=serializers.IntegerField()
    owner=serializers.IntegerField()
    def validate(self, data):
        id=data.get("id","")
        coffeeamount=data.get("coffeeamount","")
        owner=data.get("owner","")
        if coffeeamount:
            Indivorder=DropPost.objects.all()
            for indi in Indivorder:
                if indi.id==id:
                    if 15>getMinute(indi.date):
                        indi.coffeeamount=coffeeamount
                        #indi.delete()
                        indi.save()
                        data["indi"]=indi
                        #raise exceptions.ValidationError(indi.date)
                    else:
                        raise exceptions.ValidationError("Sorry times UP ")
        else:
            raise exceptions.ValidationError("Numnber of cup's field is required")

        return data

class CancelSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    def validate(self, data):
        id=data.get("id","")
        if id:
            Indivorder=DropPost.objects.all()
            for indi in Indivorder:
                if indi.id==id:
                    if 15>getMinute(indi.date):
                        indi.delete()
                    else:
                        raise exceptions.ValidationError("Sorry times UP ")
        else:
            raise exceptions.ValidationError("id field is required")

        return data


class DateSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    coffeename=serializers.CharField()
    coffeeamount=serializers.IntegerField()
    place=serializers.CharField()
    date=serializers.DateTimeField()
    owner_id=serializers.IntegerField()

