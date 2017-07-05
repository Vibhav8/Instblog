#Views handles the request and returns the response
from urllib import quote_plus # for shareable links
from django.contrib import messages #flash the successful msg
from django.http import HttpResponse, HttpResponseRedirect # HttpResponseRedirect:it redirects to the detail page after updating or creating a post
from django.shortcuts import render, get_object_or_404 , redirect 
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.

def post_create(request):
	form =PostForm(request.POST or None, request.FILES or None) # request.FILES or None:for images
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		#message success
		
		return HttpResponseRedirect(instance.get_absolute_url()) #redirects to detail page
	context={
		"form": form,
	}
	return render(request, "post_form.html", context) 

def post_detail(request,slug=None): #in url.py it is taking two arguments request and id hence here also we have to pass two
	instance = get_object_or_404(Post, slug =slug)
	share_string = quote_plus(instance.content)
	context = {
			"instance":instance,
			"title": instance.title,    #inside context we declare variables which can be used in html files
			"share_string" : share_string,
	}



	return render(request,"post_detail.html",context)

def post_list(request):
	queryset_list = Post.objects.all().order_by("-timestamp") # order_by("-timestamp") : to order posts in increasing timestamp
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var ="page"
	page = request.GET.get("page_request_var")

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"title":"Instblog",
		"object_list": queryset,
		"page_request_var" : page_request_var,
	}
	return render(request, "post_list.html",context)




    

    
def post_update(request,slug = None):
	instance = get_object_or_404(Post, slug =slug)
	form =PostForm(request.POST or None,request.FILES or None,instance = instance )
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		# message success
		
		return HttpResponseRedirect(instance.get_absolute_url()) #redirects to detail page

	context = {
			"instance":instance,
			"title": instance.title,   
			 #inside context we declare variables which can be used in html files
			"form":form,
	}

	return render(request,"post_form.html",context)



def post_delete(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Succesfully deleted")
	return redirect("posts:list")

