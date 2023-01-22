from django.db import models


class Users(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    home_page = models.URLField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):

    user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE)
    parent = models.ForeignKey('Comments', null=True, blank=True, on_delete=models.CASCADE)
    parent_first_level = models.ForeignKey('Comments', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    text = models.TextField(blank=False)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text[:25]}'

