from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Fcproduct
from fcuser.decorator import login_required, admin_required
from django.utils.decorators import method_decorator
from .forms import RegisterForm
from fcorder.forms import RegisterForm as OrderForm
# Create your views here.

class ProductList(ListView):
    model = Fcproduct
    template_name = 'product.html'
    context_object_name = 'product_list'

@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        
        fcproduct = Fcproduct(name=form.data.get('name'), price=form.data.get('price'),description=form.data.get('description')
            , stock=form.data.get('stock'))
        fcproduct.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Fcproduct.objects.all()
    context_object_name = 'product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context