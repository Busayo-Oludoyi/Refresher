from django.shortcuts import render

# Create your function to access views here.
def index(request):
    return render(request, 'index.html')
    