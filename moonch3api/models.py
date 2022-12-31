
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.forms import SlugField
from ckeditor.fields import RichTextField
# Create your models here.
import uuid
from datetime import datetime,timedelta
from django.contrib.auth.models import AbstractUser ,AbstractBaseUser ,BaseUserManager ,PermissionsMixin

from django.conf import settings


class UserManager( BaseUserManager ):
    def create_user(self, email , password = None ):
        if not email :
            raise ValueError('Email is Required!')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self , email , password ) : # instance object inheritance just like abstract or interface in java
        if password is None :
            raise ValueError("Password Needed")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

# create user 
class User( AbstractBaseUser , PermissionsMixin ) :
    #id = models.UUIDField(primary_key=True , default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True , verbose_name='Email Address', )
    image = models.ImageField( upload_to ="user/" , null=True  , blank=True, default='defaults.png' , max_length=100)
    phone_number = models.CharField(max_length=10, unique=True, null=True, blank=True)
    password = models.CharField(max_length=100)
    #username = None
    is_active = models.BooleanField(default=True)
    is_staff  =  models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIED_FIELDS = ['username']
    objects = UserManager()


    def __str__(self):
        return self.email
    # UserApi._meta.get_field_by_name('email')[0]._unique=True

    class Meta:
        db_table = 'user'



      

class Note(models.Model):
    #host  = models.CharField(max_lengtg=100)
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length= 30)
    body  = models.TextField()
    images = models.ImageField( upload_to ="imagenote/" , null=True  , blank=True, default='defaults.png' , max_length=100)
    date  = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    creator   = models.ForeignKey(User, on_delete=models.CASCADE)
    #editor = models.ForeignKey(User, on_delete=models.CASCADE)
    likes  = models.ManyToManyField( User, related_name='title')
    unlikes  = models.ManyToManyField( User, related_name='titles')
    image   = models.ImageField(upload_to="images/" , null=True  , default='defaults.png', max_length=100  )
    particpent = models.ManyToManyField(User, related_name='particpent',blank=True)
    private   = models.BooleanField(default=False)

    class META:
        ordering = ['-title']

    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()

    def getPart(self) :
        return self.particpent 

    def __str__(self):
        return self.title


class Message(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    note    = models.ForeignKey(Note ,on_delete=models.CASCADE) #models.SET_NULL 
    message = models.TextField()
    images = models.ImageField( upload_to ="messimage/" , null=True  , blank=True, default='defaults.png' , max_length=100)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    #send_image = models.ImageField(null=True , blank=True, upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  
    class META:
        ordering = ['-title']


    def __str__(self):
        return self.message[0:50]


class Blog(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user    = models.ForeignKey(User , on_delete=models.CASCADE)
    header  = models.SlugField() # CharField(max_length=50)
    blog =    RichTextField()
    #blog    = models.TextField()
    likes   = models.ManyToManyField( User , related_name='header')
    created = models.DateTimeField(auto_now_add=True) 

    def total_like(self):
        return self.likes.count()

    def totalblog(self):
        if self.user :
            return f"{self.header } :> {chr(128125)} "

    def __str__(self):
        #t = self.totalblog()
        #form = "{}:{}".format(self.user , t)
        return self.header

# class Themes( models.Model ) :
#     id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
#     user  = models.ForeignKey(User , on_delete=models.CASCADE)
#     color = models.CharField(max_length= 50)
#     seted = models.DateTimeField(auto_now_add=True) 

# 
# class Event( models.Model ) :
#     id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
#     user  = models.ForeignKey(User , on_delete=models.CASCADE)
#     image   = models.ImageField(null=True , blank=True, upload_to="images/")
#     title = models.CharField(max_length= 100)
#     body  = models.TextField()


class MindSet( models.Model ) :
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user  = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    body  = models.TextField()
    created = models.DateTimeField(auto_now_add=True)



class Ip( models.Model ) :
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)


class Event(models.Model ) :
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    place = models.CharField(max_length=30) 
    desc = models.TextField()
    images = models.ImageField( upload_to ="eventimage/" , null=True  , blank=True, max_length=40)
    date = models.DateField()
    likes  = models.ManyToManyField( User, related_name='place')
    time = models.TimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.place

    def total_like(self) :
        return self.likes.count()
        

class UserDetail ( models.Model ) :
     # user info are store here after login 
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ip = models.CharField(max_length=20) # REMOTE_ADDR
    user_agent = models.CharField(max_length=50) # HTTP_USER_AGENT
    method = models.CharField(max_length=10) # request.method
    path  = models.CharField(max_length=30) # request.path
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return self.user_agent