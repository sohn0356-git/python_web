from django.db import models

# Create your models here.

class Fcuser(models.Model):
    useremail = models.EmailField(verbose_name="이메일")
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    level = models.CharField(max_length=8, verbose_name="등급", 
    choices= (
    ('admin','관리자'),
    ('user','사용자')
    ))
    register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")


    def __str__(self):
        return self.useremail
    class Meta:
        db_table = 'fc_user'
        verbose_name = "사용자"
        verbose_name_plural = "사용자"