from django.db import models

# from shortuuidfield import ShortUUIDField
from accounts.models import Account


# Create your models here.
class Comment(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=60)
	body = models.TextField()
	post = models.ForeignKey(Account)

	class Meta:
		db_table = "comment"