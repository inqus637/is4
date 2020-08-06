from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    trader_name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    mtz= models.PositiveIntegerField()
    sell14 = models.PositiveIntegerField()
    sell7 = models.PositiveIntegerField()
    ost = models.PositiveIntegerField()
    road = models.PositiveIntegerField()
    summ = models.PositiveIntegerField(default=0)

    #def save(self, *args, **kwargs):
        #if (self.summ==0):
            #self.summ = self.price + self.mtz
        #super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_edit', kwargs={'pk': self.pk})
