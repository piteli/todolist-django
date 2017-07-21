from django.shortcuts import render, render_to_response, redirect, HttpResponseRedirect, HttpResponse
from todolistapp.forms import ParentForm, UnknownForm, ChildForm, CheckForm
from todolistapp.models import Parent, Child
from django.contrib.messages import constants as messages
from django.views.decorators.csrf import csrf_exempt


#the function executes with the signup url to take the inputs
def todolist(request):
    if request.method == 'POST':  # if the form has been filled

        form = ParentForm(request.POST)

        trye = CheckForm(request.POST)

       # data = request.POST.copy()

        if request.POST.get('delete'):
            some_var = request.POST.getlist('items')

            Parent.objects.filter(id__in=some_var).delete()
            return HttpResponseRedirect('/users/todolist')


       # if 'delete' in request.POST:
        #    for item in formDelete.cleaned_data['checkDelete']:
        #        item.delete()
        #        return HttpResponseRedirect('/users/todolist')

        if form.is_valid():  # All the data is valid

            tdlistParent = request.POST.get('tdlistParent', '')
            all_users = Parent.objects.all()
    #    password = request.POST.get('password', '')
        # creating an user object containing all the data
        user_obj = Parent(tdlistParent=tdlistParent)
        # saving all the data in the current object into the database
        user_obj.save()
        return HttpResponseRedirect('/users/todolist')


        return render(request, 'user.html', {'form': form,'user_obj': user_obj,'all_users': all_users, 'trye':trye }) # Redirect after POST


    else:
        form = ParentForm()  # an unboundform
        trye = CheckForm()
        all_users = Parent.objects.all()

        return render(request, 'user.html', {'form': form,'all_users': all_users,'trye':trye})

#the function executes with the showdata url to display the list of registered users
def showdata(request):
    all_task = Child.objects.filter(complete=True)
    return render(request, 'showdata.html', {'all_task':all_task})

def delete(request,id):
    # post = Parent.objects.filter(pk=id).delete()

    if request.POST.get('delete'):
        Parent.objects.filter(id=request.POST.getlist('checkDelete')).delete()

        return HttpResponseRedirect('/users/todolist')

def subtodolist(request, id):

    i=0

    if request.method == 'POST':  # if the form has been filled

        child = ChildForm(request.POST)

        getParentName = Parent.objects.get(id= id)
        print(getParentName.tdlistParent)


        if child.is_valid():  # All the data is valid

            tdlistChild = request.POST.get('tdlistChild', '')
            parent_id_id = id
            # all_users = Child.objects.all(
            custom_users = Child.objects.filter(parent_id_id=id)
            #    password = request.POST.get('password', '')
            # creating an user object containing all the data
            user_obj = Child(tdlistChild=tdlistChild,parent_id_id=parent_id_id, complete=None)
            # saving all the data in the current object into the database
            user_obj.save()
            return HttpResponseRedirect('.')


            return render(request, 'child.html', {'child': child,'user_obj': user_obj,'custom_users': custom_users,'i':i ,'getParentName':getParentName}) # Redirect after POST

    else:
        child = ChildForm()  # an unboundform
        getParentName = Parent.objects.get(id= id)
        print(getParentName)
        custom_users = Child.objects.filter(parent_id_id=id, complete=None)

        return render(request, 'child.html', {'child': child,'custom_users': custom_users,'getParentName':getParentName})

@csrf_exempt
def hello(request):

    if request.method == 'POST':

        amik = request.POST.get('value')
        t = Child.objects.get(id=amik)
        t.complete = 1
        t.save() 

        return HttpResponse(amik);

    else:
        return HttpResponse('amik');


'''
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            do_something_with(form.cleaned_data)
            return redirect("create_user_success")
    else:
        form = UserCreationForm()

    return render_to_response("signup/test.html", {'form': form})

    '''
