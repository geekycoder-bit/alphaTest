from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


CATEGORY_CHOICES = (
    ('Sh', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

SIZE_CHART = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)

class client_profile(models.Model):
    client_Name = models.CharField(max_length = 50)
    profile_Img = models.ImageField(upload_to = 'pic')
    des_Intro = models.TextField()
    client_Email = models.EmailField()
    # phone_Number_client = models.PhoneNumberField()
    jour_img1 = models.ImageField()
    jour_img2 = models.ImageField()
    jour_img3 = models.ImageField()
    # vlogs = models.VideoField()

    def __str__(self):
        return self.client_Name


class product(models.Model):
    product_name = models.CharField(max_length = 50)
    price = models.IntegerField()
    discount_percentage = models.FloatField(blank = True, null = True)
    category = models.CharField(max_length = 2, choices = CATEGORY_CHOICES)
    size = models.CharField(choices = SIZE_CHART, max_length = 2)
    product_img = models.ImageField(upload_to = 'pics')
    slugs = models.SlugField()

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.product_name

    def get_discount_price(self):
        discount_price = 0
        discount_price = (self.discount_percentage/100)*self.price
        return discount_price


