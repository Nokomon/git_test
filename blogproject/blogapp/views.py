from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Photo

# Create your views here.
def home(request):
    contents = Post.objects.all()
    return render(request, 'home.html', {"post_list": contents})

def detail(request, num):
    post = Post.objects.get(id=num)
    return render(request, 'detail.html', {'result': post})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.user = request.user
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/blog/post/' + str(post.id))

def update(request, num):
	post = Post.objects.get(id = num)
	if request.method == "POST":
		post.title = request.POST["title"]
		post.body = request.POST["body"]
		post.save()
		return redirect('/post/' + str(num))
	return render(request, "update.html", {"result" : post})

def delete(request, num):
    post = Post.objects.get(id=num)
    post.delete()
    return redirect('/')

def album(request):
    photo = Photo.objects.all()
    return render(request, 'album.html', {"result": photo})