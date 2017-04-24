from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
    "input":Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def input(request):
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def destroy(request, id):
    request.session['id'] = id
    info = Course.objects.get(id = request.session['id'])
    context = {
    'name':info.name,
    'description':info.description
    }
    return render(request, 'courses_app/destroy.html', context)

def delete(request):
    course_id = request.session['id']
    if request.method == 'POST':
        if request.POST['destroy'] == 'yes':
            Course.objects.filter(id = course_id).delete()
            return redirect ('/')
        if request.POST['destroy'] == 'no':
            return redirect('/')

# def delete(request):
