from django.shortcuts import render, HttpResponse, redirect

from apps.login_registration.models import User
from .models import Message, Comment


# Create your views here.
def index(request):
    if 'userid' in request.session:
        user = User.objects.get(id=request.session['userid'])
        context={
            'user_name': user.first_name,
            'user_id': user.id,
            'all_messages': Message.objects.all(),
        }
        return render(request, 'wall/index.html', context)
    return redirect('/')

def post_message(request):
    if request.method == "POST":
        if len(request.POST['message'])>0:
            user = User.objects.get(id=request.session['userid'])
            Message.objects.create(content=request.POST['message'], posted_by=user)
    return redirect('/wall')
    


def post_comment(request):
    if request.method == "POST":
        if len(request.POST['comment'])>0:
            user = User.objects.get(id=request.session['userid'])
            message = Message.objects.get(id=request.POST['message_id'])
            Comment.objects.create(content=request.POST['comment'], posted_by=user, on_message=message)
    return redirect('/wall')

def delete_comment(request):
    if request.method == "POST":
        Comment.objects.get(id=request.POST['comment_id']).delete()
    return redirect('/wall')



