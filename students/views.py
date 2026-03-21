from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentModel
from .forms import BaseForm


# Create your views here.

def read(request):
    query = request.GET.get('q', '')
    if query:
        students = StudentModel.objects.filter(
            Q(name__icontains=query) | Q(course__icontains=query)
        )
    else:
        students = StudentModel.objects.all()

    return render(request, 'home.html', {'students': students, 'query': query})


# def read(request):
#     info = StudentModel.objects.all()
#     info1 = StudentModel.objects.filter(age__gt=20, course='python', name__icontains='ali')
#     last_5_students = StudentModel.objects.order_by('-created_at')[:5]
#     return render(request, 'home.html', {'students': info})


def create(request):
    if request.method == 'POST':
        form = BaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = BaseForm()
    return render(request, 'create/create_info.html', {'form': form})


def update(request, pk):
    check = get_object_or_404(StudentModel, pk=pk)
    if request.method == 'POST':
        form = BaseForm(request.POST, instance=check)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = BaseForm(instance=check)
    return render(request, 'create/create_info.html', {'form': form})


def delete(request, pk):
    check = get_object_or_404(StudentModel, pk=pk)
    check.delete()
    return redirect('home-page')
