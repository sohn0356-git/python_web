from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from fcuser.decorator import login_required
from django.utils.decorators import method_decorator
from .models import Fcorder
from django.db import transaction
from fcproduct.models import Fcproduct
from fcuser.models import Fcuser
# Create your views here.

@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'
    
    def form_valid(self,form):
        prod = Fcproduct.objects.get(pk=form.data.get('fcproduct'))
        with transaction.atomic():
            fcorder = Fcorder(quantity=form.data.get('quantity'),fcproduct = prod,
            fcuser = Fcuser.objects.get(useremail=Fcuser.objects.get(useremail = self.request.session.get('user')))
            )
            fcorder.save()
            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/'+str(int(form.data.get('fcproduct'))))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request' : self.request
        })
        return kw

@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    model = Fcorder
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Fcorder.objects.filter(fcuser__useremail = self.request.session.get('user'))
        return queryset
