from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import ToDo

def todo_list(request):
	todos = ToDo.objects.all()
	print(todos)

	context = { 
			'todo_list':todos
	}
	return render(request, 'todo/todo_list.html', context)

# CRUD - create, retrieve, update, delete, list

def todo_detail(request, id):

	todo = ToDo.objects.get(id=id)

	context = {

		'todo': todo
	}

	return render(request, 'todo/todo_detail.html', context)


def todo_create(request):

	form = ToDoForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)

		form.save()
		return(redirect('/'))

		new_todo = ToDo.objects.create(name=name, due_date=due_date)
	context = {'form': form.as_p}
	return render(request, 'todo/todo_create.html', context)


def todo_update(request, id):
	todo = ToDo.objects.get(id=id)
	
	form = ToDoForm(request.POST or None, instance=todo)

	if form.is_valid():

		form.save()
		return(redirect('/'))

	context = {'form': form.as_p}
	return render(request, 'todo/todo_update.html', context)


def todo_delete(request, id):

	todo = ToDo.objects.get(id=id)

	todo.delete()

	return(redirect('/'))
