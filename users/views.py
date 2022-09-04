from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket
from django.contrib.auth.decorators import login_required



def login(request):
    """Вход логин"""
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

            if user and user.is_active:
                auth.login(request, user)

    else:
        form = UserLoginForm()

    context = {'form':form}
    return render(request, 'users/login.html', context)


def register(request):
    """регистрация"""
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    """Профиль"""
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)

    total_quantity = sum(basket.quantity for basket in baskets)
    total_sum = sum(basket.sum() for basket in baskets)

    context = {'form': form,
               'baskets': baskets,
               'total_quantity': total_quantity,
               'total_sum': total_sum,
               }
    return  render(request, 'users/profile.html', context)



def logout(request):
    """Выход пользователя"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))