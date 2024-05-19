from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=123)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name





class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title