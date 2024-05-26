from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import CustomUserForm
from .models import CustomUser


class BirthdayListView(ListView):
    model = CustomUser
    template_name = 'home.html'


class BirthdayCreateView(View):
    def get(self, request):
        form = CustomUserForm()
        return render(request, 'add_birthday.html', {'form': form})

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            CustomUser.objects.create(**form.cleaned_data)
            return redirect('home')
        else:
            return redirect('add_birthday')
