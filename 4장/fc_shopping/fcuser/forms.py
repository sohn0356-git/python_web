from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
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
    re_password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        useremail = cleaned_data.get('useremail')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', "비밀번호가 서로 다릅니다")
                self.add_error('re_password', "비밀번호가 서로 다릅니다")
            else:
                fcuser = Fcuser(useremail=useremail, password=make_password(password))
                fcuser.save()
    

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