

from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	book_name = models.CharField(max_length=50)
	book_author =  models.CharField(max_length=50)
	year = models.CharField(max_length=15)
	description =  models.CharField(max_length=500)
	score =  models.CharField(max_length=15)
	publisher =  models.CharField(max_length=100)
	

	def __str__(self):
		return(f"{self.book_name}, {self.book_author}, {self.year}")
