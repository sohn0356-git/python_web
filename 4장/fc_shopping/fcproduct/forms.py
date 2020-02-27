from django import forms
from .models import Fcproduct
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required' : '상품명을 입력해주세요'
        }, max_length = 64, label='상품명'
    )
    price = forms.IntegerField(
        error_messages={
            'required' : '상품가격을 입력해주세요'
        }, label='상품가격'
    )
    description = forms.CharField(
        error_messages={
            'required' : '상품설명을 입력해주세요'
        }, label='상품설명'
    )
    stock = forms.IntegerField(
        error_messages={
            'required' : '재고를 입력해주세요'
        }, label='재고'
    )
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        stock = cleaned_data.get('stock')

        if name and price and description and stock:
            fcproduct = Fcproduct(name=name, price=price,description=description
            , stock=stock)
            fcproduct.save()
    

class LoginForm(forms.Form):
    useremail = forms.EmailField(
        error_messages={
            'required' : '이메일을 입력해주세요'
        }, max_length = 64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        useremail = cleaned_data.get('useremail')
        password = cleaned_data.get('password')

        if useremail and password:
            try:
                fcuser = Fcuser.objects.get(useremail=useremail)
            except Fcuser.DoesNotExist:
                self.add_error('useremail', "해당 아이디가 없습니다")
                return
            if not check_password(password, fcuser.password):
                self.add_error('password', "비밀번호가 틀렸습니다")
            else:
                self.useremail = fcuser.useremail