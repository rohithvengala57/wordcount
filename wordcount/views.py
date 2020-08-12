from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
def home(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET["fulltext"]
    a=fulltext.split()
    c=Counter(a)
    h=sorted(c.items(),key=lambda x:x[1],reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count': h[0],'worddict':h})
def about(request):
	return render(request,'about.html')
