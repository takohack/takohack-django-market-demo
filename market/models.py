from django.db import models

# Create your models here.

class Goods(models.Model):
    categories = (
        ('tech', "电子数码"),
        ('dianqi',"家用电器"),
        ('service',"技能服务"),
        ('cloths',"服饰鞋子"),
        ('life', "生活日用"),
        ('book',"图书"),
        ('other',"其他"),
    )

    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    price = models.FloatField(default=0)
    img = models.ImageField()
    cate = models.CharField(max_length=32, choices=categories, default="其他")
    describe = models.TextField()
    push_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"