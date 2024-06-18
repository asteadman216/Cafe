# views.py

from django.shortcuts import render, get_object_or_404, redirect, render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import Coffee, Tea, Kids
from .forms import CoffeeForm, TeaForm, KidsForm

def home(request):
    return render(request, 'home.html')

def coffee_list(request):
    coffees = Coffee.objects.all()
    context = {
        'coffees': coffees,
    }
    return render(request, 'catalog/coffee_list.html', context)

def tea_list(request):
    teas = Tea.objects.all()
    context = {
        'teas': teas,
    }
    return render(request, 'catalog/tea_list.html', context)

def kids_list(request):
    kids = Kids.objects.all()
    context = {
        'kids': kids,
    }
    return render(request, 'catalog/kids_list.html', context)

def add_coffee(request):
    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coffee_list')
    else:
        form = CoffeeForm()
    return render(request, 'add_coffee.html', {'form': form})

def add_tea(request):
    if request.method == 'POST':
        form = TeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tea_list')
    else:
        form = TeaForm()
    return render(request, 'add_tea.html', {'form': form})

def add_kids(request):
    if request.method == 'POST':
        form = KidsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kids_list')
    else:
        form = KidsForm()
    return render(request, 'add_kids.html', {'form': form})

def coffee_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'catalog/coffee_detail.html', {'coffee': coffee})

def tea_detail(request, pk):
    tea = get_object_or_404(Tea, pk=pk)
    return render(request, 'catalog/tea_detail.html', {'tea': tea})

def kids_detail(request, pk):
    kids = get_object_or_404(Kids, pk=pk)
    return render(request, 'catalog/kids_detail.html', {'kids': kids})

class CoffeeDetailView(DetailView):
    model = Coffee
    template_name = 'catalog/coffee_detail.html'  # Specify the template for rendering the detail view
    context_object_name = 'coffee'  # Optionally specify the name of the context variable in the template

class TeaDetailView(DetailView):
    model = Coffee
    template_name = 'catalog/tea_detail.html'  # Specify the template for rendering the detail view
    context_object_name = 'tea'  # Optionally specify the name of the context variable in the template

class KidsDetailView(DetailView):
    model = Coffee
    template_name = 'catalog/kids_detail.html'  # Specify the template for rendering the detail view
    context_object_name = 'kids'  # Optionally specify the name of the context variable in the template

class CoffeeListView(ListView):
    model = Coffee
    template_name = 'catalog/coffee_list.html'  # Specify the template for rendering the list
    context_object_name = 'coffees'  # Specify the context variable name to use in the template (optional)
    paginate_by = 10  # Number of objects to display per page (optional)

    # You can add more queryset customization if needed
    def get_queryset(self):
        return Coffee.objects.all()  # Example: Retrieve all Tea objects
class TeaListView(ListView):
    model = Tea
    template_name = 'catalog/tea_list.html'  # Specify the template for rendering the list
    context_object_name = 'teas'  # Specify the context variable name to use in the template (optional)
    paginate_by = 10  # Number of objects to display per page (optional)

    # You can add more queryset customization if needed
    def get_queryset(self):
        return Tea.objects.all()  # Example: Retrieve all Tea objects

class KidsListView(ListView):
    model = Tea
    template_name = 'catalog/kids_list.html'  # Specify the template for rendering the list
    context_object_name = 'kids'  # Specify the context variable name to use in the template (optional)
    paginate_by = 10  # Number of objects to display per page (optional)

    # You can add more queryset customization if needed
    def get_queryset(self):
        return Kids.objects.all()  # Example: Retrieve all Tea objects

class CoffeeCreateView(CreateView):
    model = Coffee
    template_name = 'catalog/add_coffee.html'  # Specify the template for rendering the create form
    fields = '__all__'  # Or specify the fields you want to include in the form explicitly

    def form_valid(self, form):
        # Optional: Customize form validation or processing logic before saving
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('coffee_list')  # Redirect to coffee list after successfully creating a coffee

class TeaCreateView(CreateView):
    model = Coffee
    template_name = 'catalog/add_tea.html'  # Specify the template for rendering the create form
    fields = '__all__'  # Or specify the fields you want to include in the form explicitly

    def form_valid(self, form):
        # Optional: Customize form validation or processing logic before saving
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tea_list')  # Redirect to coffee list after successfully creating a coffee

class KidsCreateView(CreateView):
    model = Coffee
    template_name = 'catalog/add_kids.html'  # Specify the template for rendering the create form
    fields = '__all__'  # Or specify the fields you want to include in the form explicitly

    def form_valid(self, form):
        # Optional: Customize form validation or processing logic before saving
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('kids_list')  # Redirect to coffee list after successfully creating a coffee
class CoffeeDeleteView(DeleteView):
    model = Coffee
    template_name = 'catalog/delete_coffee.html'
    success_url = reverse_lazy('coffee_list')  # Redirect to coffee list after deletion

    def get_object(self, queryset=None):
        # Get the Coffee object based on the URL parameter 'pk'
        return get_object_or_404(Coffee, pk=self.kwargs['pk'])

class TeaDeleteView(DeleteView):
    model = Tea
    template_name = 'catalog/delete_tea.html'
    success_url = reverse_lazy('tea_list')  # Redirect to coffee list after deletion

    def get_object(self, queryset=None):
        # Get the Coffee object based on the URL parameter 'pk'
        return get_object_or_404(Tea, pk=self.kwargs['pk'])

class KidsDeleteView(DeleteView):
    model = Coffee
    template_name = 'catalog/delete_kids.html'
    success_url = reverse_lazy('kids_list')  # Redirect to coffee list after deletion

    def get_object(self, queryset=None):
        # Get the Coffee object based on the URL parameter 'pk'
        return get_object_or_404(Kids, pk=self.kwargs['pk'])

class CoffeeUpdateView(UpdateView):
    model = Coffee
    form_class = CoffeeForm  # Specify the form class for editing Coffee
    template_name = 'catalog/update_coffee.html'
    success_url = reverse_lazy('coffee_list')  # Redirect to coffee list after update

    def get_object(self, queryset=None):
        # Get the Coffee object based on the URL parameter 'pk'
        return get_object_or_404(Coffee, pk=self.kwargs['pk'])

class TeaUpdateView(UpdateView):
    model = Tea
    form_class = TeaForm  # Specify the form class for editing Coffee
    template_name = 'catalog/update_tea.html'
    success_url = reverse_lazy('tea_list')  # Redirect to coffee list after update

    def get_object(self, queryset=None):
        # Get the Coffee object based on the URL parameter 'pk'
        return get_object_or_404(Tea, pk=self.kwargs['pk'])

class KidsUpdateView(UpdateView):
    model = Kids
    form_class = KidsForm  # Specify the form class for editing Coffee
    template_name = 'catalog/update_kids.html'
    success_url = reverse_lazy('kids_list')  # Redirect to coffee list after update

    def get_object(self, queryset=None):
        # Get the Coffee object based on the URL parameter 'pk'
        return get_object_or_404(Kids, pk=self.kwargs['pk'])