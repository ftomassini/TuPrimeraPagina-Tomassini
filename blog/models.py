from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Editorial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la editorial")
    country = models.CharField(max_length=50, verbose_name="País de origen")
    founded_year = models.IntegerField(verbose_name="Año de fundación")

    def __str__(self):
        return self.name