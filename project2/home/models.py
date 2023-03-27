from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name= models.CharField(max_length=100)
    dep_deccription= models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec =models.CharField(max_length=255)
    dep_name =models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image =models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr. ' + self.doc_name + ' - (' + self.doc_spec + ')'


class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone= models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

class Signup(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Place=models.CharField(max_length=30)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)

    def __str__(self):
        return self.Name
