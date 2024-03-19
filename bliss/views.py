from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm , RegisterForm, Uploadinput
from marque_feature.models import marquee_feature_1,marquee_feature_2,marquee_feature_3
from home_card.models import home_card_1, home_card_2, home_card_3, home_card_4, home_card_5,home_card_6, book_card_1,book_card_2, book_card_3, book_card_4, book_card_5,sport_card_1,sport_card_2, sport_card_3, sport_card_4, sport_card_5
from main_videos.models import news_video, blogs_video, sports_video
from user.models import Post , Comment, Story , Userdetails
from search.models import Search



def register(request):
    books_image = marquee_feature_1.objects.all()
    magazines_image=marquee_feature_2.objects.all()
    books_image_2=marquee_feature_3.objects.all()
    try:
        if request.method == "POST":
            name = request.POST.get('FullName')
            email = request.POST.get('UserName')
            password = request.POST.get('PassWord1')
            if User.objects.filter(username=name).exists():
                form = RegisterForm()
                return render(request, "register.html" ,{'show' : True,'form2' : form,'books_image':books_image,'magazines_image':magazines_image,'books_image_2':books_image_2})
            elif User.objects.filter(email=email).exists():
                form = RegisterForm()
                return render(request, "register.html" ,{'show' : True,'form2' : form,'books_image':books_image,'magazines_image':magazines_image,'books_image_2':books_image_2})
            else:
                user = User.objects.create_user(username=email, email=email, password = password)
                user.first_name = name
                user.save()
                auth_login(request, user)
                return redirect("home")
        else:
            form = RegisterForm()
    except:
        pass        
    return render(request, "register.html" , {'form2' : form ,'books_image':books_image,'magazines_image':magazines_image,'books_image_2':books_image_2})

def loginpage(request):
    books_image = marquee_feature_1.objects.all()
    magazines_image=marquee_feature_2.objects.all()
    books_image_2=marquee_feature_3.objects.all()
    try:
        if request.method =='POST':
            email=request.POST.get('UserName')
            password=request.POST.get('PassWord')
            user = authenticate(username=email, password = password)
            print(user)
            if user is not None:
                auth_login(request, user)
                return redirect("home")
            else:
                form = LoginForm()
                return render(request, "login.html", {'show' : True,'form1' : form,'books_image':books_image,'magazines_image':magazines_image,'books_image_2':books_image_2})
        else:
            form = LoginForm()
    except:
        pass    
    return render(request, "login.html", {'form1' : form ,'books_image':books_image,'magazines_image':magazines_image,'books_image_2':books_image_2})

@login_required(login_url='login')
def home(request):
    Posts1 = Post.objects.order_by("-created_at")[0::2]
    Posts2 = Post.objects.order_by("-created_at")[1::2]
    story = Story.objects.order_by("-created_at")   
    Postform = Uploadinput()
    postcomment = Comment.objects.all()
    Userdetail = Userdetails.objects.all()
    if 'postupload_submit' in request.POST:
        if request.method == "POST":
            content = request.POST.get("Textinput")
            imgvid = request.FILES.get("imgVidfield")
            en = Post(content=content,image=imgvid)
            en.user = request.user
            en.save()
            return redirect("/home")
    if "deletepost" in request.POST:    
        if request.method == "POST" :    
            post_id = request.POST.get("deletepost")
            post = Post.objects.filter(id=post_id).first()
            if post and post.user == request.user:
                post.delete()
                return redirect("/home")


    if 'commentform_submit' in request.POST:
        if request.method == "POST":
            post_id_C = request.POST.get("commentform_submit")
            post_C = Post.objects.filter(id=post_id_C).first()
            if post_C:
                comment = request.POST.get("commentvalue")
            
                # Create a new Comment object and associate it with the post and user
                cn = Comment(text=comment, user=request.user, post=post_C)
                cn.save()  # Save the new comment to the database
            
                return redirect("/home")
        return redirect("/home")    
    if "storyfieldsubmit" in request.POST:
        if request.method == "POST":
            contenttext = request.POST.get("storytextcontent")
            contentbackground = request.POST.get("storybackground") 
            contentfstyle = request.POST.get("storyfontstyle")
            storyfile = request.FILES.get("storyfilecontent")
            print(storyfile)
            sn = Story(contenttext= contenttext, contentbackground = contentbackground, contentfstyle= contentfstyle , storyfile = storyfile)
            sn.user = request.user
            sn.save()
            return redirect("/home")
    return render(request, "home.html" ,{'user': request.user, "Uploadform" : Postform, "post1": Posts1,"post2": Posts2, "comment": postcomment , "story": story, "Userdetail":Userdetail,})

def logging_out(request):
    logout(request)
    return redirect('/')

def myprofile_lg(request):
    Posts = Post.objects.order_by("-created_at")   
    Postform = Uploadinput()
    Userdetail = Userdetails.objects.all()

    if 'postupload_submit' in request.POST:
        if request.method == "POST":
            content = request.POST.get("Textinput")
            imgvid = request.FILES.get("imgVidfield")
            en = Post(content=content,image=imgvid)
            en.user = request.user
            en.save()
            return redirect("/myprofile-lg")
    if "deletepost" in request.POST:    
        if request.method == "POST" :    
            post_id = request.POST.get("deletepost")
            post = Post.objects.filter(id=post_id).first()
            if post and post.user == request.user:
                post.delete()
                return redirect("/myprofile-lg")  
               
    return render(request, "myprofile-login.html", {"Uploadform" : Postform,"post": Posts,"Userdetail":Userdetail,})
def search(request):
    search_content = Search.objects.all()
    popularsearch = Search.objects.all()[0::2]
    data= {
        "searchdata": search_content,
        "popularsearch":popularsearch
        }    
    print(len(data))    
    return render(request, "search.html" , data)
def blogs(request):
    videoen = blogs_video.objects.all()
    entry1 = home_card_1.objects.all()
    entry2 = home_card_2.objects.all()
    entry3 = home_card_3.objects.all()
    entry4 = home_card_4.objects.all()
    entry5 = home_card_5.objects.all()
    entry6 = home_card_5.objects.all()
    data={'entry1':entry1, 'entry2':entry2, 'entry3':entry3, 'entry4':entry4,'entry5':entry5,'entry6':entry6 ,'videos': videoen}
    return render(request, "blogs.html", data)


def news(request):
    videoen = news_video.objects.all()
    entry1 = book_card_1.objects.all()
    entry2 = book_card_2.objects.all()
    entry3 = book_card_3.objects.all()
    entry4 = book_card_4.objects.all()
    entry5 = book_card_5.objects.all()
    data={'entry1':entry1, 'entry2':entry2, 'entry3':entry3, 'entry4':entry4,'entry5':entry5,'videos': videoen}

    return render(request, "news.html", data)
def sports(request):
    videoen = sports_video.objects.all()
    entry1 = sport_card_1.objects.all()
    entry2 = sport_card_2.objects.all()
    entry3 = sport_card_3.objects.all()
    entry4 = sport_card_4.objects.all()
    entry5 = sport_card_5.objects.all()
    data={'entry1':entry1, 'entry2':entry2, 'entry3':entry3, 'entry4':entry4,'entry5':entry5,'videos': videoen}
    return render(request, "sports.html", data)


def content(request):
    return render(request, "content.html")

def content0(request):
    return render(request, "content0.html")


def eventform(request):
    return render(request , "eventForm.html")



 