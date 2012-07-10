# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
   
    print post_list
    return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
    p=Post.objects.get(pk=id)
    q=p.body
    html=''
    
    for i in p.commentsss.all():  # the commentsss  here is in the model as a related name in the class Comment
        html+=str(i)
      
    return HttpResponse('<h1>'+str(p) +'</h1>'+ '<br/>' + str(q) +'<br/>' +html +'<br/>')
    
    
def post_search(request, term):
     p=Post.objects.filter(body__contains=term)
     html=''   #html page has been initialied to be an empty string
     for i in p:
         html+=str(i)
     return HttpResponse(html)
    

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
