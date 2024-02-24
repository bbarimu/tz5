from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length = 50,
        verbose_name = 'название категории'
    )

    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(
        max_length = 20,
        verbose_name = 'имя'
    )
    surname = models.CharField(
        max_length = 25,
        verbose_name = 'фамилия'
    )
    sex = models.BooleanField(
        choices = (
            (True, 'Мужской'),
            (False, 'Женский')
        ),
        verbose_name = 'пол'
    )
    date_of_birth = models.DateField(
        null = True,
        blank = True,
        verbose_name = 'дата рождения'
    )

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Post(models.Model):
    title = models.CharField(
        max_length = 100,
        verbose_name = 'название поста'
    )
    content = models.TextField(
        max_length = 1000,
        verbose_name = 'текст'
    )
    category = models.ForeignKey(
        Category, on_delete = models.PROTECT
    )
    author = models.ForeignKey(
        Author, on_delete = models.PROTECT  
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )

    def __str__(self):
        return f"{self.title}, {self.pk}"