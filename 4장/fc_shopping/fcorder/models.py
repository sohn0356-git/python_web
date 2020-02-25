from django.db import models
from fcuser.models import Fcuser
from fcproduct.models import Fcproduct
# Create your models here.

class Fcorder(models.Model):
    fcuser = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name = "사용자")
    product = models.ForeignKey('fcproduct.Fcproduct',on_delete=models.CASCADE, verbose_name = "상품")
    quantity = models.IntegerField(verbose_name="수량")
    register_dttm = models.DateField(auto_now_add=True, verbose_name="등록날짜")

    class Meta:
        db_table = 'fc_order'
        verbose_name = "주문"
        verbose_name_plural = "주문"