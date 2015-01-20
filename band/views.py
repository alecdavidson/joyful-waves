from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})
	
def bio(request):
	return render(request, 'bio.html', {})

def disc(request):
	return render(request, 'disc.html', {})
