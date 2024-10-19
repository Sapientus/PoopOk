from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, ProfileForm


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(
                request,
                'users/register_done.html', {'new_user': new_user}
            )
        else:
            # If the form is not valid, render the form again with errors
            return render(
                request,
                'users/register.html', {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
        return render(
            request,
            'users/register.html',
            {'user_form': user_form}
        )


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = ProfileForm(instance=request.user, data=request.POST, files=request.FILES)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Updated was successful')
            return redirect('blog:post_list')
        else:
            messages.error(request, 'Something went wrong')
    else:
        user_form = ProfileForm(instance=request.user)
        return render(
            request,
            'users/edit.html',
            {
                'user_form': user_form,
            }
        )
