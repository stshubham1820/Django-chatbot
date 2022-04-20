from django.shortcuts import render
from .models import form
# Create your views here.
def index(request):
    if request.method=='POST':
        print('POST')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        review = request.POST.get('review')
        obj = form.objects.create(Name=name,Email=email,Subject=subject,Review=review)
        obj.save()   
    return render(request,'index.html')