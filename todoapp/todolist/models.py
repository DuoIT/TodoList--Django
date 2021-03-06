from django.db import models
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ["Category"]
        verbose_name_plural = ["Categories"]

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%M-%D"))
    due_day = models.DateField(default=timezone.now().strftime("%Y-%M-%D"))
    category = models.ForeignKey(Category, default="general")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

