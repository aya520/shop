from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()


    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.product.title + '-' + str(self.id)
