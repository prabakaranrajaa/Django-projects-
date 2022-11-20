from django.shortcuts import render, redirect
from crudApp.models import Student
from crudApp.forms import StudentFo


# Create your views here.
def viewall(request):
    student = Student.objects.all()
    return render(request, 'ind.html', {'s1': student})


def create_view(request):
    form = StudentFo()
    if request.method == 'POST':
        form = StudentFo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/run')
    return render(request, 'create.html', {'form': form})


def delete_view(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/run')


def update_view(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentFo(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/run')
    return render(request, 'update.html', {'studen': student})
