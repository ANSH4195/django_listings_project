from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact


def register(request):
    if request.method == "POST":
        # Getting form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check if username exists
            # For this we need a User model which Django has by default
            # We got it in at the top (3rd line)
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username tooked')
                return redirect('register')
            else:
                # Check if email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email existence')
                    return redirect('register')
                else:
                    # Create user
                    user = User.objects.create_user(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password
                    )
                    # Auto login after registration
                    # user.save()
                    # auth.login(request, user)
                    # messages.success(request, 'You logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Registered, now log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords no match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Who you?')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You log out")

    return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)
