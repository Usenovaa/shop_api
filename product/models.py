from django.db import models
from slugify import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=30, primary_key=True, blank=True, unique=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, primary_key=True, blank=True, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Comment(models.Model):
    body = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.body


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='liked')
    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.product}Liked by{self.author.name}'


class Favorite(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorite'
    )
    favorite = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='favorite'
    )
    is_favorite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.favorite} favorite by {self.author.name}'


class Rating(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ratings'
    )
    rating = models.PositiveSmallIntegerField()
    post = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='ratings'
    )

    def __str__(self) -> str:
        return f'{self.rating} -> {self.post}'

from django.db import models


class Order(models.Model):
    author = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    statuses = [
        ('D', 'Delivered'),
        ('ND', 'Not Delivered')
    ]
    status = models.CharField(max_length=2, choices=statuses)
    amount = models.PositiveIntegerField()
    payments = [
        ('Card', 'Card'),
        ('Cash', 'Cash'),
    ]
    payment = models.CharField(max_length=4, choices=payments)
    created_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField()

    def __str__(self):
        return f'Product ID: {self.pk}'
