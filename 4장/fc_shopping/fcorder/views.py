from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from .models import Fcorder
# Create your views here.


class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'
    
    def form_invalid(self, form):
        return redirect('/product/'+str(form.fcproduct))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request' : self.request
        })
        return kw

class OrderList(ListView):
    model = Fcorder
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Fcorder.objects.filter(fcuser__useremail = self.request.session.get('user'))
        return queryset