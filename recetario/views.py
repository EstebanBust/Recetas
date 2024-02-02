from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views import View
from .forms import RecipeForm
from .models import Recipe

# Create your views here.
def home (request):
    recipes = Recipe.objects.all()
    return render(request, 'recetas.html', {'recipes':recipes})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'  
    success_url = reverse_lazy('nombre_de_tu_vista_despues_del_registro')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    

class LoginView(View):
    template_name = 'signin.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Redirigir a la página que desees después del login
            return redirect('home')  # Ajusta esto con el nombre de tu vista de inicio
        return render(request, self.template_name, {'form': form})
    
def signout(request):
    logout(request)
    return redirect('home')

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio después de crear la receta
    else:
        form = RecipeForm()

    return render(request, 'recipe.html', {'form': form})