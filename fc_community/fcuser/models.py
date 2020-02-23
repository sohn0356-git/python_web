from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length = 32,
                                verbose_name = '사용자명')
    password = models.CharField(max_length= 64,
                                verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')

    def __str__(self):              #username으로 화면에 띄우고 싶을 때
        return self.username
    class Meta:
        db_table = 'fastcampus_fcuser'  #table_name을 직접 설정하고 싶을 때
        verbose_name = 'fastcampus user'    #복수형이 들어감
        #verbose_name_plural = 'fastcampus user'    #그냥 들어감
