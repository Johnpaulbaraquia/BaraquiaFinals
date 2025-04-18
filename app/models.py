from django.db import models
from django.urls import reverse

# Create your models here.

# class Customer(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     address = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    

#     def get_absolute_url(self):
#         return reverse('customer_detail', kwargs={'pk': self.pk})

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def get_absolute_url(self):
        return reverse('customer_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
   
    
    
# class Catergories(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     products = models.ManyToManyField('Product', related_name="categories")

#     def __str__(self):
#         return self.name

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('Product', related_name="categories")
    
    def __str__(self):
        return self.name

    
    
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
#     order_date = models.DateTimeField(auto_now_add=True)
#     stage = models.CharField( max_length=20, )
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     products = models.ManyToManyField(Product, through='OrderDetail', related_name="orders")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     delivery_date = models.DateField(null=True, blank=True)
    

#     def get_absolute_url(self):
#         return reverse('order_detail', kwargs={'pk': self.pk})

#     def __str__(self):
#         return f"Order {self.id} - {self.customer}"

# 
    from django.db import models

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('Product')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')],
        default='pending'
    )

    def __str__(self):
        return f"Order {self.id} - {self.customer}"

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_details")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        
        return f"Order {self.order.id} - {self.product.name}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False, blank=False, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order {self.order.id} - {self.product.name}"
    
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name="suppliers")
    def __str__(self):
        return self.name


    