from django.shortcuts import render,redirect
from .models import Group

# Create your views here.


def group_list(request):
    groups = Group.objects.all()
    return render(request,'home.html',context={'groups':groups})    
    




def add_group(request):
    if request.method == 'POST':
        data = request.POST
        group = Group(
            name = data['name'],
            room = data['room']
        )
        group.save()
        return redirect('groups')
    return render(request,'create_group.html')



def group_details(request,pk):
    group = Group.objects.get(id=pk)
    return render(request,'group_info.html',{'group':group})



def update_group(request,pk):
    group = Group.objects.get(id=pk)
    if request.method == 'POST':
        data = request.POST
        group.name = data['name'],
        group.room = data['room']
        group.save()
        return redirect('groups')
    return render(request,'update_group.html',context={'group':group})



def delete_group(request,pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('groups')
    return render(request,'delete_group.html',context={'group':group})
        

        
def students_in_group(reques):
    pass

# --------------------------student--------------------------

def add_studetn(request):
    pass

def select_for_student(request):
    pass


def student_list(request):
    pass

def student_details(request,pk):
    pass

def update_student(request,pk):
    pass

def delete_student(request):
    pass


def contrains_for_students(request):
    pass


