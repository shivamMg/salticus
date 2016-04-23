from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import UserCreationForm


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'users/signup.html', {
        'form': form,}
    )


def account(request):
    return render(request, 'users/account.html')
