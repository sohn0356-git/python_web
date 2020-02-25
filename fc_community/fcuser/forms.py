from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="사용자이름")
    password = forms.CharField(widget = forms.PasswordInput, label="비밀번호")