
from django.db import models
from django.urls import reverse
from django.db.models import Avg, Count


class ProductManger(models.Manager):

    def averageReview(self):
        reviews =  super(ProductManger, self).filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews =  super(ProductManger, self).filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count