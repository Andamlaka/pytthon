from django.contrib import admin
from .models import Company, Department, Employee, Product, ProductDescription, Student, Course

# Registering models
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(ProductDescription)
admin.site.register(Student)
admin.site.register(Course)
