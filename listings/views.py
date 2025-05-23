from django.shortcuts import render
from .models import Property
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Property
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'listings/property_list.html', {'properties': properties})

def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'listings/property_detail.html', {'property': property})

class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    fields = ['title', 'location', 'price', 'property_type', 'description', 'image']
    template_name = 'listings/property_form.html'
    success_url = reverse_lazy('property_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PropertyUpdateView(UpdateView):
    model = Property
    fields = ['title', 'location', 'price', 'property_type', 'description', 'image']
    template_name = 'listings/property_form.html'
    success_url = reverse_lazy('property_list')
    
    def test_func(self):
        property = self.get_object()
        return property.user == self.request.user

class PropertyDeleteView(DeleteView):
    model = Property
    template_name = 'listings/property_confirm_delete.html'
    success_url = reverse_lazy('property_list')
    def test_func(self):
        property = self.get_object()
        return property.user == self.request.user

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login after signup
    template_name = 'listings/signup.html'


@login_required
def user_properties(request):
    user_props = Property.objects.filter(user=request.user)
    return render(request, 'listings/user_properties.html', {'properties': user_props})