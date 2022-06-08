from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView

from .models import Category, Product
from .forms import CategoryForm

# ------------- CATEGORÍAS ------------------------------------------------


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category/list.html'
    login_url = '/login/'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = "Ha ocurrido un error"

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['create_url'] = reverse_lazy('erp:category_create')
        context['entity'] = 'Categorías'
        return context

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')
    login_url = '/login/'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()  #Es lo mismo que escribir form = CategoryForm(request.POST)
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'

            #data = Category.objects.get (pk=request.POST['id']).toJSON()
        except Exception as e:
            data ['error'] = e
        
        return JsonResponse(data)

        # form = CategoryForm(request.POST)

        # if form.is_valid():
        #     form.save()
        #     return HttpResponseRedirect(self.success_url)
        

        # self.object = None
        # context = self.get_context_data(**kwargs)
        # context['form'] = form
        # return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar Categoría'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorías'
        context['action'] = 'add'
        return context

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()  #Es lo mismo que escribir form = CategoryForm(request.POST)
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'

            #data = Category.objects.get (pk=request.POST['id']).toJSON()
        except Exception as e:
            data ['error'] = e
        
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Categoría'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorías'
        context['action'] = 'edit'
        return context

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/delete.html'
    success_url = reverse_lazy('erp:category_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data ['error'] = e
        
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Categoría'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorías'
        return context

class CategoryFormView(FormView):
    form_class = CategoryForm
    template_name = "category/create.html"
    success_url = reverse_lazy("erp:category_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Categoría'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorías'
        context['action'] = 'add'
        return context

# ------------- PRODUCTOS ------------------------------------------------

class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        return context

# ------------- DASHBOARD ------------------------------------------------

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = "Panel de Administración"

        return context