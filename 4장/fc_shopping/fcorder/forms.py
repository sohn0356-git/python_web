from django import forms
from .models import Fcorder
from fcproduct.models import Fcproduct
from fcuser.models import Fcuser
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):

    def __init__(self,request,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required' : '수량을 입력해주세요'
        }, label='수량'
    )
    fcproduct = forms.IntegerField(
        error_messages={
            'required' : '상품을 입력해주세요'
        }, label='상품', widget = forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        fcproduct = cleaned_data.get('fcproduct')

        print(self.request.session)
        fcuser = self.request.session.get('user')
        if quantity and fcproduct and fcuser:
            fcorder = Fcorder(quantity=quantity,fcproduct=Fcproduct.objects.get(pk=fcproduct),
            fcuser = Fcuser.objects.get(useremail=fcuser)
            )
            fcorder.save()
        else:
            self.product = fcproduct
            self.add_error('quantity', '값이 없습니다')
            self.add_error('fcproduct', '값이 없습니다')
        
