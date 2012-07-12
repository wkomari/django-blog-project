# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 
from django.shortcuts import render_to_response

def post_list(request):
    post_list = Post.objects.all()
    
    my_context = Context({'posts':post_list})   # this means put the postlist info into a dictionary called posts
    return render_to_response ('blog/post_list.html', my_context)
    

def post_detail(request, id, showComments=True):
    p=Post.objects.get(pk=id)
    #q=p.body
    #html=''
    
    	    
    for i in p.commentsss.all():  # the commentsss  here is in the model as a related name in the class Comment
      #html+=str(i)
      my_context = Context({'post':p,'comments':p.commentsss.all()})
    
    return render_to_response ('blog/post_detail.html', my_context)  
 

   
def post_search(request, term=True):
     p=Post.objects.filter(body__contains=term)
         
     my_context = Context({'posts':p,'term':term})
     return render_to_response ('blog/post_search.html', my_context)
    


def home(request):
     return render_to_response('blog/base.html',{})
 
