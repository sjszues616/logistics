from django.db import models

# Create your models here.


class ArrivalPlan(models.Model):
    cabinet = models.IntegerField("柜号到港信息")
    sku = models.CharField("商品编码",max_length=64)
    productName = models.CharField("货物名称",max_length=64)
    cabinetLength = models.IntegerField("柜子长度/cm")
    cabinetWidth = models.IntegerField("柜子宽度/cm")
    cabinetHeight = models.IntegerField("柜子高度/cm")
    cabinetStyle = models.IntegerField("款式/cm")
    cabinetCount =models.IntegerField("箱数")
    onshowCount = models.IntegerField("仓库实际上架数量")
    solidity = models.IntegerField("体积/cm^3")
    solidityAll = models.IntegerField("总体积/cm^3")
    grossWeight = models.IntegerField("毛重/kg")
    grossWeightAll = models.IntegerField("总毛重/kg")
    orderInfo = models.TextField("预约信息",null=True,blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = "进港信息表"
        verbose_name_plural = verbose_name

