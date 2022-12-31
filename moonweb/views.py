
from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect ,JsonResponse
from django.utils.timesince import timesince, timeuntil
from moonch3 import settings
# Create your views here.
from moonch3api.models import Blog, Note,Message , Event ,User, UserDetail
from .forms import NoteForm , RegisterForm ,LoginUserForm , ChatForm  , BlogForm ,AddNoteForm , UserImageForm
from django.views.generic import CreateView ,ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy ,reverse
from django.contrib.auth import authenticate ,login, logout 
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib import messages #send info to user
import re, random , os , sys ,socket
#import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User

#User = get_user_model()

def dashboard(request):
    
    #user = User.objects.filter(is_superuser=False).count()
    u = User.objects.filter(is_superuser=False).count()
    blog = Blog.objects.count()
    event= Event.objects.count()
    ac = Note.objects.count()

    con = {
        'users' : u,
        'blog': blog,
        'event': event,
        'note' : ac,

    }
    return render(request , 'moonweb/dashboard.html' , con)

def insertUserDetail(request) :
    if request.user.is_authenticated:
        r_addr = request.META['REMOTE_ADDR']
        addr = socket.gethostbyname(socket.gethostname())
        agent = request.META['HTTP_USER_AGENT']
        method = request.method
        path = request.path
        user = request.user
        UserDetail.objects.create(
            user=user,
            ip=addr ,
            user_agent=agent ,
            method=method,
            path=path,
        )
    else:
        r_addr = request.META['REMOTE_ADDR']
        agent = request.META['HTTP_USER_AGENT']
        method = request.method
        path = request.path
        user = request.user



def Home( request ) :
    print( request.META['REMOTE_ADDR'] )

    addr = socket.gethostbyname(socket.gethostname())
    print(addr)
    
    context = {

    }
    return render( request , 'moonweb/home.html' , context ) 


@login_required(login_url='login')
def sayhi(request):
    button = False # button delete display
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    title  = Note.objects.filter(title__icontains=q).order_by('-date')
    for check in title:
        if check.creator == request.user :
            button = True
    #listthem = Note.objects.all().order_by('-id')
    if request.method == 'POST':
        data = request.POST.getlist('sel-delete')
        print(data)

        for datas in data :
            Note.objects.filter(id=datas , creator=request.user).delete()
        if len(data) <= 0:
            messages.info(request , "Please Selected,it's Empty! ")    
        return redirect('/hom')
    context = {'listem': title , 'query' : q , 'but' : button}
    return render(request ,'moonweb/stayhome.html', context)


def kamra(request, id):
    try:
        listth = Note.objects.get(id=id)
        if listth.private == True:
            return render(request , 'moonweb/error.html')
    except Exception:
        return HttpResponse('no way')

    mess = Message.objects.all()       
    partici = listth.particpent.all()
    messages_note = listth.message_set.all().order_by('-created') #child object
    
    likesme = get_object_or_404( Note , id=id)
    likescount = likesme.total_likes()
    unlikesme = get_object_or_404( Note , id=id)
    unlikescount = unlikesme.total_unlikes()

    form = ChatForm()
    user = request.user.id
    note_id = listth.id
    if request.method == 'POST':
        if request.POST.get('act') == '▶' :
            mess = request.POST.get('message')
            if mess.strip() == ''.rstrip():
                return HttpResponseRedirect(reverse('kamra', args=[str(id)]) )
                #messages.info(request , "Message cannot be Empty ")
                #return HttpResponse('Sorry!')
            else:
                form = Message.objects.create(
                    note = listth,
                    message = mess,
                    user = request.user
                )
                listth.particpent.add(request.user)
            

        if request.POST.get('act') == 'delete':
            delme = request.POST.get('delme')
            messagedel = Message.objects.get(id=delme)
            if request.user != messagedel.user:
                messages.info(request , "No way you can delete this bro ")
                return HttpResponse('Sorry')
            messagedel.delete()
            messages.info(request , "Message Deleted ")


        if request.POST.get('act') == 'Update':
            #messagedel = Message.objects.get(id=id)
            #messagedel.delete()
            Message.objects.filter(id=request.POST.get('getme')).update(message=request.POST.get('message'))
            
            #form = NoteForm(request.POST, instance=getid)
            #if form.is_valid():
            #    form.save()
                # return redirect('/')
            messages.info(request , "update")

    kam = {
        'par' : partici,
        'mess': mess,
        'form' : form,
        'listth': listth,
        'message' : messages_note,
        'like' : likescount,
        'unlike' : unlikescount,
        }
    return render(request , 'moonweb/kamra.html',kam)


@login_required(login_url='login')
def create(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST  ) # , request.FILES
        if form.is_valid():
            # title = request.POST.get('title')
            # body = request.POST.get('body')
            # image = request.FILES.get('image')
            # private = True if(request.POST.get('private') == 'on')  else False

            # addNote = Note.objects.create(
            #     title=title,
            #     body=body ,
            #     image= image,
            #     private=private,
            #     creator=request.user
            # )
            # addNote.save()
            note = form.save(commit=False) #try add new room
            note.creator = request.user
            note.save()
            return redirect('/hom')

    context = {'form': form}
    return render(request , 'moonweb/create.html', context )

@login_required(login_url='login')
def edit(request,id):
    getid = Note.objects.get(id=id)
    form = NoteForm(instance=getid)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=getid)
        if form.is_valid():  # if you upload with file better not to uses this 
            #image_path = chimage.path
            #if os.path.exists(image_path):
            #    os.remove(image_path)
            note = form.save(commit=False)
            note.save() # files upload uses request.FILES.get()
            return HttpResponseRedirect(reverse('kamra', args=[str(id)]) )
            #return redirect('/hom')
    context = {'form': form}
    return render(request , 'moonweb/update.html', context)




def editmessage(request , id ) :
    delmess = Message.objects.get(id=id)
    idnote = delmess.note.id
    if request.POST.get('act') == 'Update':
            #messagedel = Message.objects.get(id=id)
            #messagedel.delete()
        Message.objects.filter(id=request.POST.get('getme')).update(message=request.POST.get('message'))
            #form = NoteForm(request.POST, instance=getid)
            #if form.is_valid():
            #    form.save()
                # return redirect('/')
        #messages.info(request , "update")
        return HttpResponseRedirect(reverse('kamra', args=[str(idnote)]) )
    context = {
        'mes' : delmess,
        'id' : idnote,
    }
    return render(request, 'moonweb/editmessage.html', context)

def deleteMessage(request , id) :

    delmess = Message.objects.get(id=id)

    idnote = delmess.note.id

    print(idnote)

    if request.POST.get('act') == 'delete':
        delme = request.POST.get('delme')
        messagedel = Message.objects.get(id=delme)
        if request.user != messagedel.user:
            messages.info(request , "No way you can delete this bro ")
            return HttpResponse('Sorry,you cannot modify an unauthorize ')
        messagedel.delete()
        #messages.info(request , "Message Deleted")
        return HttpResponseRedirect(reverse('kamra', args=[str(idnote)]) )
        
    
    context = {

        'mes' : delmess,
        'id' : idnote,
        

    }
    return render(request, 'moonweb/deletemess.html', context)




def addnotePhoto ( request , id ) :
    getid = Note.objects.get(id=id)
    note_image = getid.image
    form =AddNoteForm(instance=getid)
    if request.method == 'POST':
        form = AddNoteForm(request.POST, request.FILES , instance=getid)
        if form.is_valid() :
            image_path = note_image.path
            if os.path.exists(image_path):
                os.remove(image_path)
            
            form.save()
            return HttpResponseRedirect(reverse('kamra', args=[str(id)]) )

    
    context = {
        'form' : form ,
        'note' : getid,
    }
    return render(request , 'moonweb/addnotephoto.html' , context )



def noteSetting ( request , id =None ) :
    getid = Note.objects.get(id=id)
    partici = getid.particpent.all()
    
    context = {
        'form' : getid ,
        'part' : partici,
    }
    return render(request , 'moonweb/notesetting.html' , context )



def deleteNote(request,id):
    delme = Note.objects.get(id=id)
    if request.method == 'POST':
        delme.delete()
        return redirect('/')

    form  = {'del': delme}
    return render(request , 'moonweb/delete.html', form)

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('email')
                messages.success(request, 'Account Create')
                return redirect('login')

            else:
                check = form.errors.as_data()
                for ch in check :
                    # if ( ch == 'password2') :
                    #     data = form.errors.as_data().get(ch)
                    #     for datach in data:
                    #         messages.error(request , datach)
                        #messages.error(request,  "Try at least 2 character 2 number 2 symbol and 2 Capital ")
                    if (ch == 'email') :
                        # data = form.errors.as_data().get(ch)
                        messages.error(request , "Enter a valid email address." )

                    if (ch == 'username') :
                        messages.error(request , "Name is Already Exist!" )

                #messages.error(request,  form.errors )
                # if form.errors == 'password2':
                #     messages.error(request , " okoko")
                   
                # else:
                #     

        context = {'register': form}
        return render(request , 'moonweb/register.html' , context)

#if  user.is_anonymous()


def loginMe(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request , email=username, password=password)
            if user is not None:
                login(request ,user)
                insertUserDetail(request)
                return redirect('/hom')
            else:
                messages.error(request , ' ㈯  email & pass is incorrect ❌')

        context = {}
        return render(request , 'moonweb/login.html' , context)

def logoutMe(request):
    logout(request)
    return redirect('login')

def profile(request):
    user = User.objects.get(email=request.user.email)

    form = {
        'name' : 'name',
        'email' : 'Email'
    }
    rom = user.message_set.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        email    = request.POST.get('email')
        if(username == user.username):
            messages.error(request , 'Your username is still the same')
        else:
            #user = User.objects.get(username=u)
            user.username = username
            user.email = email
            user.save()
            messages.error(request , 'Profile has been Updated')
                # usr = User.objects.get(username='your username')
                # usr.set_password('raw password')
                # usr.save()

        #User.objectsx.update()
    context = {
        'det' : request.user,
        #'user' : user,
        'form' : form,  
    }
    return render(request ,'moonweb/profile.html', context)

def viewProfile(request ) -> None :
    user = User.objects.get(email=request.user.email)
    user_image = user.image
    form   = UserImageForm()
    if request.method == 'POST':
        print('okokokko')
        form = UserImageForm(request.POST, request.FILES , instance=user)
        if form.is_valid() :
            image_path = user_image.path
            if os.path.exists(image_path):
                os.remove(image_path)
            
            form.save()
            return redirect('/myprofile')


    context = {
        'user':user,
        'form' : form,
    }
    return render(request ,'moonweb/viewprofile.html', context)


def deactivateUser(request) :
    data = {}
    user = User.objects.get(email=request.user.email)
    print(request.user.username)
    if request.method == 'POST':
        check = request.POST.get('username')
        if check == request.user.username :
            user.delete()
            logout(request)
            return redirect('login')

        elif check != request.user.username :
            messages.info(request ,
            chr(9828) + ' Please provide your username'
            )
            

        elif check.strip() == '' :
            messages.info(request,
            '[-] Field cannot be empty'

            )

    template = 'moonweb/deactivateuser.html'
    return render(request , template , data )


class UserAuthen(ListView):
    model = User
    template_name = 'moonweb/viewprofile.html'

    def get(self , request , id=None , *arg , **kwargs ) :
        user = User.objects.get(id=id)
        context = {
            'user' : user,
        }
        return render(request , self.template_name , context)

    def delete(self, request , id ):
        if request.user.is_authenticated :
            return redirect('/')
        
        user = User.objects.get(id=id)

        return user

        
        





def detail(request,tle):
    tle.lower()
    #bio = Note.objects.get(title=tle.replace('-',' '))
    bio = Note.objects.get(id=tle)
    #print(bio.body, bio.title)
    text = Note.objects.filter(title=bio.title.replace('-',' '))
    ch = Note.objects.all()
    uni = [i for i in range(10018,10059)]
    style = random.choice(uni)
    group = bio.particpent.all()
    print(group)

    #ch = get_object_or_404( Note , title=tle)
    context = {
            'bio' : bio,
            'detail' : text,  #text.title().replace('-',' ')
            'ch' : ch,
            'uni':  chr(style),
            'group' :  group,
        }
    return render(request, 'moonweb/detail.html', context)





def about(request ):
    text = {
        'header' : 'Welcome To my Website',
        'founder' : 'Founder by Trsh',
        'detail'  : 'This Know as socail media website which help you communicate with each other and also you can view other blog & create block  which help other ',
        'more' : 'Read More ' ,
        'top' : 'Back to Top' ,
    }
    context = {
        'about' : text,
    }
    return render(request ,'moonweb/about.html' , context)

def editMessage(request , id ):
    return render(request , )

def Like(request , pk):
    like = get_object_or_404(Note , id=request.POST.get('like') )
    if like.likes.filter(id=request.user.id).exists() :
        like.likes.remove(request.user )
    else: like.likes.add(request.user)
    return HttpResponseRedirect(reverse('kamra', args=[str(pk)]) )


def unLike(request , pk):
    unlike = get_object_or_404(Note , id=request.POST.get('unlike') )
    unlike.unlikes.add(request.user)
    return HttpResponseRedirect(reverse('base:kamra', args=[str(pk)]) )

def addBlog(request):
    blog = BlogForm()
    if request.method == 'POST':
        blog = BlogForm( request.POST )
        if blog.is_valid():
            note = blog.save(commit=False) #try add new room
            note.user = request.user
            note.save()
            return redirect('setting')
        else:
            messages.error(request, blog.errors)
    context = {
        'formblog' : blog ,
    }
    return render(request , 'moonweb/blog.html' , context)

def editBlog(request,id):
    getid = Blog.objects.get(id=id)
    form = BlogForm(instance=getid)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=getid)
        if form.is_valid():
            form.save()
            #id = getid.header
            return HttpResponseRedirect(reverse('view-blog', args=[str(id)]) )
            #return redirect('/')
    context = {'formblog': form}
    return render(request , 'moonweb/updateblog.html', context)



def viewBlog(request , pk):
    blogg = Blog.objects.get(id=pk)  
    # pk.lower()
    # bio = Note.objects.get(title=tle.replace('-',' '))
    # #print(bio.body, bio.title)
    # text = Note.objects.filter(title=tle.replace('-',' '))
    # ch = Note.objects.all()
    # blog = Blog.objects.get(header=pk )
    #text = Blog.objects.filter(header=pk.replace('-',' ')).first()

    # let non-user view the blog with in 2 minute 

    # if pk is not str:
    #     blog = Blog.objects.get(id=int(pk))

    # ch = re.match(r"[-+]?\d+(\.0*)?$", pk) is not None
    if request.method == 'POST':
        blog = get_object_or_404(Blog , id=request.POST.get('likeblog') )
        if blog.likes.filter(id=request.user.id).exists() :
            blog.likes.remove(request.user )
        else: blog.likes.add(request.user)
        return HttpResponseRedirect(reverse('view-blog', args=[str(pk)]) )
    
    # #likesme = None
    # try:
    #     if ch == True:
    #         blog = Blog.objects.get(id=pk)
               
    #     else:
    #         blog = Blog.objects.get(header=pk)
    # except Blog.MultipleObjectsReturned:
    #     blog = Blog.objects.filter(header=pk)[0]

    # if ch == False:
    #     likesme = get_object_or_404( Blog , header=pk)
    likescount = blogg.total_like()

    ok = request.META.get('HTTP_X_FORWARDED_FOR')
    print(ok)

    oko = request.META.get('REMOTE_ADDR')

    print(oko)

    # if blog.header != pk :
    #     return HttpResponse("okokoko")

    # if request.user != blog.user :
    #     return HttpResponse('no blog view')
    con = {
        'blog' : blogg,
        'like' : likescount ,
        # 'text' : text ,
    }
    return render(request , 'moonweb/viewblog.html' , con )


# def LikeBlog(request , pk):
#     getput = request.POST.get('likeblog')
#     like = get_object_or_404(Blog , id= getput )
#     like.likes.add(request.user)
#     return HttpResponseRedirect(reverse('base:view-blog', args=[str(pk)]) ) # return back to the same path


def LikeBlog(request , pk):
    # listth = Blog.objects.get(id=pk)
    # print(listth)
    post = get_object_or_404(Blog, id=request.POST.get('likeblog'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    print(post)
    like = get_object_or_404( Blog , id=request.POST.get('likeblog') )
    like.likes.add(request.user)
    return HttpResponseRedirect(reverse('view-blog', args=[str(pk)]) )

def Setting(request):
    blogs = Blog.objects.all()
    #blog_page = Paginator(blogs, 3)
    # for ch in blog:
    #     blog = ch.header.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\'|`~-= _+"}).strip().replace(' ' ,'')

    #blog.header.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\'|`~-= _+"}).strip().replace(' ' ,'')
    page = request.GET.get('page', 1 )

    paginator = Paginator(blogs, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(5)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'set' : 'Setting',
        'blog' : blogs,
        'users' : users,
        
    }
    return render(request , 'moonweb/setting.html' , context )

def Private(request):
    mess = Note.objects.all()  
    context = {
        'set' : 'Private-Chat is Visible Here',
        'mess' : mess,
    }
    return render(request , 'moonweb/priv.html' , context )



def viewPrivate(request, id):
    listth = Note.objects.get(id=id)
    if listth.private == False :
        return render(request , 'moonweb/error.html')
        # return HttpResponse('no way')
    

    if request.user != listth.creator :
        return render(request ,'moonweb/error.html')

    partici = listth.particpent.all()
    messages_note = listth.message_set.all().order_by('-created') #child object


    if request.method == 'POST':
        if request.POST.get('act') == 'Send' :
            form = Message.objects.create(
                note = listth,
                message = request.POST.get('message'),
                user = request.user
            )
            listth.particpent.add(request.user)
    
    context = {
        'listth' : listth,
        'mess' : messages_note ,
        'par' : partici,
        
    }
    return render(request , 'moonweb/viewprivatechat.html', context )
# class base view
# class CreateUser(CreateView):
#     form_class = RegisterForm
#     form = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'template/base/register.html'


# class LoginView(CreateView):
#     form_class = LoginUserForm
#     form = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'template/base/login.html'


#     # def post(self, request):
#     #     username = request.POST['username']
#     #     password = request.POST['password']
#     #     user = authenticate(username=username, password=password)

#     #     if user is not None:
#     #         if user.is_active:
#     #             login(request, user)

#     #             return HttpResponseRedirect('/form')
#     #         else:
#     #             return HttpResponse("Inactive user.")
#     #     else:
#     #         return HttpResponseRedirect(settings.LOGIN_URL)
#     #     return render(request, "index.html")

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect(settings.LOGOUT_URL)





def listBlog(request) :
    blog = Blog.objects.all().order_by('-id')
    template = 'moonweb/listblog.html'
    context = {}
    context['blog'] = blog
    return render(
        request,
        template ,
        context
    )

def contactus( request ) :
    from django.core.mail import send_mail
    from django.core.mail import EmailMultiAlternatives
    from django.template.loader import get_template
    from django.conf import settings
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    def check(email):
        if(re.fullmatch(regex, email)):
            return True
        else:
            return False

    if request.method == 'POST':
        contact = request.POST.get('contactus')
        if check(contact) :
            htmly = get_template('email/index.html')
            d = { 'username': request.user.username }
            subject, from_email, to = 'welcome', contact, settings.EMAIL_HOST_USER
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        else:
            messages.error(request, 'Email invalid')

        return redirect('/')
    return redirect('home')


def deactivate( request ) :
    if request.method == 'POST' :
        email = request.POST.get('youremail')
        if email == request.user.email :
            User.objects.get(email=email,username=request.user.username).delete()
            logout(request)
            return redirect('signin')
        elif email == ' '.rstrip() :
            messages.error(request , 'Field Cannot Be Empty')
            return redirect('setting')

        else:
            messages.error(request , 'That is not your Email')
            return redirect('setting')
    else :
        messages.error(request , 'unable to deactivate your account')
        return redirect('profile')



