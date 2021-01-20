from django.db import models

# Create your models here.
class product(models.Model):
	product_id = models.AutoField
	product_name = models.CharField(max_length = 50)
	catagory = models.CharField(max_length = 50, default="")
	subcatagory = models.CharField(max_length = 50, default="")
	price = models.IntegerField(default=0)
	decription = models.CharField(max_length = 300)
	pub_date = models.DateField()
	image = models.ImageField(upload_to = "store/img", default="")
	stock = models.IntegerField(default=0)
	
	def __str__(self):
		return self.product_name
	

	