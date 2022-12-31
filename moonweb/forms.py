
from django.forms import ModelForm
from django import forms
from moonch3api.models import Note,Message ,Blog ,User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
User = get_user_model()

class UserImageForm(ModelForm) :
    class Meta:
        model = User
        fields = ['image']
class NoteForm(ModelForm):
    title = forms.CharField(label='title')
    title.widget.attrs['placeholder'] = "Title"

    class Meta:
        model = Note
        fields = '__all__' #['title','body','image'] # hide creator and likes
        exclude =['likes' , 'unlikes', 'creator' , 'particpent' , 'images']

class AddNoteForm( ModelForm ) :
    image = forms.ImageField(label=('image'),required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta :
        model = Note 
        fields = ['image']
        
class ChatForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']

# class EditProfile(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','email']
        
class RegisterForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(label='Name') # label='text' place inside CF-method
    username.widget.attrs['placeholder'] = "☫ username ☫"
    email = forms.EmailField(label='Email') # label='text' place inside CF-method
    email.widget.attrs['placeholder'] = "☬ email ☬"
    password1 = forms.CharField(label='password',widget=forms.PasswordInput) # label='text' place inside CF-method
    password1.widget.attrs['placeholder'] = "☣ password ☣" # 9763
    password2 = None 
    #password2 = forms.CharField(label='',widget=forms.PasswordInput) # label='text' place inside CF-method
    #password2.widget.attrs['placeholder'] = "CONFIRM-PASSWORD"

    class Meta:
        model = User
        fields = ['username','email','password1'] # ,'password2'


class LoginUserForm(ModelForm):
    class Meta:
        #model = Register
        fields = ['username','password']

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__' #['title','body','image'] # hide creator and likes
        exclude =['user','likes']


