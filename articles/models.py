from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # *this tells django where to go when the new instance of this model is created:
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.id})
