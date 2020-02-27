from django import forms
from .models import Fcorder

from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
    quantity = forms.IntegerField(
        error_messages={
            'required' : '수량을 입력해주세요'
        }, label='수량'
    )
    fcproduct = forms.IntegerField(
        error_messages={
            'required' : '상품설명을 입력해주세요'
        }, label='상품설명', widget = forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        fcproduct = cleaned_data.get('fcproduct')
