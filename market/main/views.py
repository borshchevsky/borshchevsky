from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, UpdateView

from .forms import ProfileForm
from .models import Product, Profile


def index(request):
    turn_on_block = True
    greeting = 'Hello'
    return render(request, 'index.html', {
        'turn_on_block': turn_on_block,
        'greeting': greeting,
    })


class ProductListView(ListView):
    model = Product
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.GET.get('tag')
        if tag:
            return queryset.filter(tags__tag_name=tag)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        tag = self.request.GET.get('tag')
        data['tag'] = tag
        return data


class ProductDetailView(DetailView):
    model = Product


class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return super().get_queryset().get(username=self.request.user)


def update_profile(request):
    user = Profile.objects.get(username=request.user)
    user.first_name = request.POST.get('first_name')
    user.last_name = request.POST.get('last_name')
    user.email = request.POST.get('email')
    user.save()
    messages.success(request, "User profile has been updated.")
    return redirect('profile-update')
