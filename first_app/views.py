from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content':"Hello I'm form firstapp!"}
    return render(request, 'index.html', context=my_dict)
