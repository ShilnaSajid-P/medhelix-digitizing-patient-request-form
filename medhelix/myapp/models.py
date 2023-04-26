# from django.db import models

# # Create your models here.

# class Userr(models.Model):
#     image=models.ImageField(upload_to="images")
#     serial_no=models.CharField(max_length=50)
#     date = models.DateField(null=True, blank=True)

    
#     def __str__(self):
#         return f"CapturedImage {self.pk}"


from django.db import models

class Userr(models.Model):
    image = models.ImageField()
    serial_no=models.CharField(max_length=50, default='')
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"CapturedImage {self.pk}"
