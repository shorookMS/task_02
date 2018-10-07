from django.shortcuts import render
# Create your views here.
def order(request):
	context ={ "msg":"Hello World!"}
	return render(request, 'restaurants_page.html',context)