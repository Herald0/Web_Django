from django.shortcuts import render
import json
from django.http import JsonResponse
from .forms import UserForm
from .models import User
from .models import Post, Like
from django.http import HttpResponse

data = 'Вход'


def save_form(request):

  x = request.POST
  form = UserForm(x)
  users = User.objects.all()
  if form.is_valid():
    for i in users:
      if i.name == x['name'] and i.surname == x['surname'] and \
      i.password == x['password'] and i.email == x['email'] and \
      i.age == int(x['age']) and i.gender == x['gender']:
        print('Пользователь уже существует')
        break
    else:
      form.save()

  else:
    print('Error: ', form.errors)


def home(request):
  global data
  if request.method == 'POST':
    print(request.POST)

    save_form(request)
    x = request.POST
    data = f"{x['surname']} {x['name']}"
      
  form = UserForm()
  return render(request, 'main/index.html', {'form': form, 'data': data})


def populartours(request):
  global data
  users = User.objects.all()
  user_id = 0
  
  posts = Post.objects.all()

  if request.method == 'POST':
    save_form(request)
    x = request.POST
    data = f"{x['surname']} {x['name']}"

    for i in users:
      if i.name == x['name'] and i.surname == x['surname'] and \
      i.password == x['password'] and i.email == x['email'] and \
      i.age == int(x['age']) and i.gender == x['gender']:
        user_id = i.id
        break
  
  form = UserForm()
  return render(request, 'main/populartours.html', 
              {'form': form, 'data': data, 'posts': posts, 'user_id': user_id})


def likePost(request):
  likes = Like.objects.all()
  x = request.GET
  
  if request.method == 'GET':
    for like in likes:
      
      if (like.post.id == int(request.GET['post_id'])) & (like.user.id == int(request.GET['user_id'])):
        if like.vote == -1:
          like.vote = 1
          like.save()
        break
    else:
      post_id = x['post_id']
      user_id = x['user_id']
      likedpost = Post.objects.get(pk=post_id)
      likeduser = User.objects.get(pk=user_id)
      m = Like(post=likedpost, user=likeduser, vote=1)
      m.save()

    likedpost = Post.objects.get(pk=x['post_id'])
    like_count = Like.objects.filter(vote=1, post=x['post_id']).count()
    dislike_count = Like.objects.filter(vote=-1, post=x['post_id']).count()
    likedpost.like_count = like_count
    likedpost.dislike_count = dislike_count
    likedpost.save()
    
    return JsonResponse({
      'like_count': like_count,
      'dislike_count': dislike_count
    })
  else:
    return HttpResponse("Request method is not a GET".encode('utf-8'))


def dislikePost(request):
  likes = Like.objects.all()
  x = request.GET

  if request.method == 'GET':
    for like in likes:
      if (like.post.id == int(x['post_id'])) & (like.user.id == int(x['user_id'])):
        if int(like.vote) == 1:
          like.vote = -1
          like.save()
        break
    else:
      post_id = x['post_id']
      user_id = x['user_id']
      likedpost = Post.objects.get(pk=post_id)
      likeduser = User.objects.get(pk=user_id)
      m = Like(post=likedpost, user=likeduser, vote=-1)
      m.save()

    likedpost = Post.objects.get(pk=x['post_id'])
    like_count = Like.objects.filter(vote=1, post=x['post_id']).count()
    dislike_count = Like.objects.filter(vote=-1, post=x['post_id']).count()
    likedpost.like_count = like_count
    likedpost.dislike_count = dislike_count
    likedpost.save()
    
    return JsonResponse({
      'like_count': like_count,
      'dislike_count': dislike_count
    })
  else:
    return HttpResponse("Request method is not a GET".encode('utf-8'))


def tourselect(request):
  global data

  if request.method == 'POST':
    save_form(request)
    x = request.POST
    data = f"{x['surname']} {x['name']}"
    
  return render(request, 'main/tourselect.html', {'data': data})

def about(request):
  global data

  if request.method == 'POST':
    save_form(request)
    x = request.POST
    data = f"{x['surname']} {x['name']}"
    
  return render(request, 'main/about.html', {'data': data})
