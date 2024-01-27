from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Member
from .forms import MemberForm

def hello(request):
  member_list= Member.objects.all().values()
  context ={       #visible
    'member_list':member_list
  }
  template = loader.get_template('hello.html')
  return HttpResponse(template.render(context,request))

def detail(request,id):
  mymember= Member.objects.get(id=id)
  template=loader.get_template('detail.html')
  context={
    'mymember':mymember
  }
  return HttpResponse(template.render(context,request))

def form(request):
  template = loader.get_template('form.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def image(request):
  template = loader.get_template('image.html')
  return HttpResponse(template.render())

@csrf_exempt
def newmember(request):
  if request.method =='POST':
    firstname = request.POST.get('firstname',)
    lastname = request.POST.get('lastname',)
    rollno = request.POST.get('rollno',)
    image = request.FILES['image']
    member=Member(firstname=firstname,lastname=lastname,rollno=rollno,image=image)
    member.save()
  template = loader.get_template('newmember.html')
  return HttpResponse(template.render())

def update(request,id):
  member=Member.objects.get(id=id)
  form = MemberForm(request.POST,instance=member)
  if form.is_valid():
    form.save()
    t1= loader.get_template('newmember.html')
    return HttpResponse(t1.render())
  return render(request,'update.html',{'form':form,'member':member})

@csrf_exempt
def delete(request,id):
  if request.method == 'POST':
    member =Member.objects.get(id=id)
    member.delete()
    t1= loader.get_template('hello.html')
    return HttpResponse(t1.render())
  return render(request,'delete.html')
  








