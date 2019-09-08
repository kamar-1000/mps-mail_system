from django.shortcuts import render,redirect
from .models import Sentmail
from account.models import Profile
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Inbox,Notification,Sentmail
from .forms import CreatemailForm
from django.shortcuts import render
import json
from django.contrib import messages
from django.core import serializers
# Create your views here.
def home(req):
	return render(req,"mail/home.html")

@login_required(login_url="/account/login")
def inbox(req):
	inbox=Inbox.objects.filter(profile__user__username=req.user).order_by('-id')
	return render(req,"mail/inbox.html",{'inbox':inbox})

def delete_inbox(req,id):
    Inbox.objects.get(id=id).delete()
    messages.error(req,"Item Successfully deleted from Inbox")
    return redirect("/home/inbox")

def delete_starred(req,id):
    Inbox.objects.filter(id=id).update(starred=False)
    messages.error(req,"Successfully remove from starred")
    return redirect("/home/inbox")

def save_starred(req,id):
    Inbox.objects.filter(id=id).update(starred=True)
    messages.success(req,"Successfully added in starred")
    return redirect("/home/inbox")

def starred(req):
    starred=Inbox.objects.filter(profile__user__username=req.user,starred=True).order_by("-id")
    return render(req,"mail/starred.html",{"starred":starred})

def delete_sent_mail(req,id):
    Sentmail.objects.filter(id=id).delete()
    messages.success(req,"Item Successfully deleted..!")
    return redirect("/home/sentmail")

def notification(req):
	if not req.user.is_authenticated:
		return HttpResponse("not_authenticated")
	check=req.GET.get("check",False)
	try:
	    if check:
	        noti=Notification.objects.filter(profile__user__username=req.user).order_by('-id')
	        keep=Notification.objects.filter(profile__user__username=req.user).order_by('-id')
	        for n in keep[5:]:
	            n.delete()
	        Notification.objects.filter(profile__user__username=req.user).update(check=True)

	    else:noti=Notification.objects.filter(profile__user__username=req.user).order_by('-id')
	    data={}
	    count=0
	    for n in noti:
	        temp={}
	        temp["check"]=n.check
	        temp["name"]=n.from_user.user.username
	        temp["pic"]=json.dumps(str(n.from_user.pic))
	        temp["email"]=n.from_user.user.email
	        temp["mail_id"]=n.mail_id
	        data["noti{}".format(count)]=temp
	        count+=1
	except Exception as e:return HttpResponse(e)
	if data=={}:
		return HttpResponse("{}")
	return JsonResponse(data)

@login_required(login_url="/account/login")
def inbox_view(req,id):
	inbox_view=Inbox.objects.get(id=id)
	return render(req,"mail/inbox_view.html",{"inbox_view":inbox_view})

@login_required(login_url="/account/login")
def sentmail(req):
	sentmail=Sentmail.objects.filter(profile__user__username=req.user).order_by('-id')
	return render(req,"mail/sentmail.html",{"sentmail":sentmail})

@login_required(login_url="/account/login")
def sentmail_view(req,id):
	sentmail_view=Sentmail.objects.get(id=id)
	return render(req,"mail/sentmail_view.html",{"sentmail_view":sentmail_view})

@login_required(login_url="/account/login")
def create(req):
	form=CreatemailForm()
	if req.method=='POST':
		form=CreatemailForm(req.POST,req.FILES)
		if form.is_valid():
			to_user=None
			to_email=req.POST['to_email']
			try:
				to_user=Profile.objects.get(user__email=to_email)
			except:messages.error(req,"Receipent email address not found")
			if to_user is not None:
				f=form.save(commit=False)
				from_user=Profile.objects.get(user__username=req.user.username)
				f.profile=from_user
				f.to_user=to_user
				f.save()
				inbox=Inbox.objects.create(profile=to_user,from_user=from_user,sub=form.cleaned_data['sub'],msg=form.cleaned_data['msg'],attach=form.cleaned_data['attach'])
				Notification.objects.create(mail_id=inbox.id,profile=to_user,from_user=from_user,check=False)
				messages.success(req,"mail successfully sent to {}".format(to_email))
				return redirect('/home/sentmail')
	return render(req,"mail/create.html",{"form":form})
