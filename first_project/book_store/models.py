from django.db import models
# Create your models here.

  
class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, related_name="departments", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, related_name="employees", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductDescription(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Description for {self.product.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return self.name