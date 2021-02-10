from django.shortcuts import redirect, render, get_object_or_404

from .form import UserForm, TaskForm
from .models import Task, User


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                print(request)
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {'users': users})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect("/")


def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    tasks = Task.objects.filter(user=user_id)
    return render(request, "user_detail.html", {'user': user, "tasks": tasks})


def update_task(request, user_id, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = not task.status
    task.save()

    return redirect(f"/user/{user_id}")


def delete_task(request, user_id, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect(f"/user/{user_id}")


def create_task(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                print(request)
                form.save()
                return redirect(f'/user/{user_id}')
            except:
                pass
    else:
        form = TaskForm()
        form.fields['user'].initial = user_id
    return render(request, 'task_create.html', {'form': form, "user": user})
