from django.db import models
from django.contrib.auth.models import User

class Coffee(models.Model):
    LATTE = 'latte'
    POUR_OVER = 'pour_over'
    DRIP_BREW = 'drip_brew'
    AMERICANO = 'americano'
    CAPPUCCINO = 'cappuccino'
    DRINK_TYPE_CHOICES = [
        (LATTE, 'Latte'),
        (POUR_OVER, 'Pour Over'),
        (DRIP_BREW, 'Drip Brew'),
        (AMERICANO, 'Americano'),
        (CAPPUCCINO, 'Cappuccino'),
    ]
    HOT = 'hot'
    ICED = 'iced'
    DRINK_TEMP_CHOICES = [
        (HOT, 'Hot'),
        (ICED, 'Iced'),
    ]
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    DRINK_SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]
    VANILLA = 'Vanilla'
    HAZELNUT = 'Hazelnut'
    CARAMEL = 'Caramel'
    WHITE_MOCHA = 'White Mocha'
    MOCHA = 'Mocha'
    TOFFEE = 'Toffee'
    BUTTERSCOTCH = 'Butterscotch'
    SF_VANILLA = 'Sugar Free Vanilla'
    SF_CARAMEL = 'Sugar Free Caramel'
    SF_MOCHA = 'Sugar Free Mocha'
    DRINK_FLAVOR_CHOICES = [
        (VANILLA, 'Vanilla'),
        (HAZELNUT, 'Hazelnut'),
        (CARAMEL, 'Caramel'),
        (WHITE_MOCHA, 'White Mocha'),
        (MOCHA, 'Mocha'),
        (TOFFEE, 'Toffee'),
        (BUTTERSCOTCH, 'Butterscotch'),
        (SF_VANILLA, 'Sugar Free Vanilla'),
        (SF_CARAMEL, 'Sugar Free Caramel'),
        (SF_MOCHA, 'Sugar Free Mocha'),
    ]

    drink_type = models.CharField(max_length=20, choices=DRINK_TYPE_CHOICES, default=LATTE)
    drink_temp = models.CharField(max_length=4, choices=DRINK_TEMP_CHOICES, default=HOT)
    drink_flavor = models.CharField(max_length=20, choices=DRINK_FLAVOR_CHOICES, default=VANILLA)
    drink_size = models.CharField(max_length=6, choices=DRINK_SIZE_CHOICES, default=MEDIUM)

    def get_price(self):
        if self.drink_size == self.SMALL:
            return 4.00
        elif self.drink_size == self.MEDIUM:
            return 5.00
        elif self.drink_size == self.LARGE:
            return 7.00
        else:
            return 0.00 #default price or handle error

    def __str__(self):
        return f"{self.get_drink_type_display()} {self.get_drink_size_display()} {self.get_drink_flavor_display()} {self.get_drink_temp_display()} - ${self.get_price():.2f}"

class Tea(models.Model):
    HOT = 'hot'
    ICED = 'iced'
    DRINK_TEMP_CHOICES = [
        (HOT, 'Hot'),
        (ICED, 'Iced'),
    ]
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    DRINK_SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]
    BLACK = 'Black'
    GREEN = 'Green'
    HERBAL = 'Herbal'
    ENGLISH_BREAKFAST = 'English Breakfast'
    ROOIBOS = 'Rooibos'
    OOLONG = 'Oolong'
    EARL_GREY = 'Earl Grey'
    MASALA_CHAI = 'Masala Chai'
    DRINK_TEA_CHOICES = [
        (BLACK, 'Black'),
        (GREEN, 'Green'),
        (HERBAL, 'Herbal'),
        (ENGLISH_BREAKFAST, 'English Breakfast'),
        (ROOIBOS, 'Rooibos'),
        (OOLONG, 'Oolong'),
        (EARL_GREY, 'Earl Grey'),
        (MASALA_CHAI, 'Masala Chai'),
    ]
    STRAWBERRY = 'Strawberry'
    PEACH = 'Peach'
    MANGO = 'Mango'
    LYCHEE = 'Lychee'
    VANILLA = 'Vanilla'
    RASPBERRY = 'Raspberry'
    PEPPERMINT = 'Peppermint'
    SIMPLE_SYRUP = 'Simple Syrup'
    DRINK_TEA_SYRUP_CHOICES = [
        (STRAWBERRY, 'Strawberry'),
        (PEACH, 'Peach'),
        (MANGO, 'Mango'),
        (LYCHEE, 'Lychee'),
        (VANILLA, 'Vanilla'),
        (RASPBERRY, 'Raspberry'),
        (PEPPERMINT, 'Peppermint'),
        (SIMPLE_SYRUP, 'Simple Syrup'),
    ]

    drink_temp = models.CharField(max_length=4, choices=DRINK_TEMP_CHOICES, default=HOT)
    drink_tea_type = models.CharField(max_length=20, choices=DRINK_TEA_CHOICES, default=BLACK)
    drink_tea_flavor = models.CharField(max_length=20, choices=DRINK_TEA_SYRUP_CHOICES, default=SIMPLE_SYRUP)
    drink_size = models.CharField(max_length=6, choices=DRINK_SIZE_CHOICES, default=MEDIUM)

    def __str__(self):
        return f"{self.get_drink_size_display()} {self.get_drink_tea_type_display()} {self.get_drink_temp_display()} {self.get_drink_tea_flavor_display()}"

class Kids(models.Model):
    HOT = 'hot'
    ICED = 'iced'
    DRINK_TEMP_CHOICES = [
        (HOT, 'Hot'),
        (ICED, 'Iced'),
    ]
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    DRINK_SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]
    MILK = 'milk'
    LEMONADE = 'lemonade'
    JUICE = 'juice'
    DRINK_KIDS_CHOICES = [
        (MILK, 'Milk'),
        (LEMONADE, 'Lemonade'),
        (JUICE, 'Juice'),
    ]
    CHOCOLATE = 'chocolate'
    STRAWBERRY = 'strawberry'
    MANGO = 'mango'
    RASPBERRY = 'raspberry'
    WATERMELON = 'watermelon'
    WHIPPED_CREAM = 'whipped cream'
    DRINK_KIDS_FLAVOR_CHOICES = [
        (CHOCOLATE, 'Chocolate'),
        (STRAWBERRY, 'Strawberry'),
        (MANGO, 'Mango'),
        (RASPBERRY, 'Raspberry'),
        (WATERMELON, 'Watermelon'),
        (WHIPPED_CREAM, 'Whipped Cream'),
    ]

    drink_temp = models.CharField(max_length=4, choices=DRINK_TEMP_CHOICES, default=ICED)
    drink_kids_choices = models.CharField(max_length=15, choices=DRINK_KIDS_CHOICES, default=JUICE)
    drink_kids_flavor_choices = models.CharField(max_length=20, choices=DRINK_KIDS_FLAVOR_CHOICES, default=STRAWBERRY)
    drink_size = models.CharField(max_length=6, choices=DRINK_SIZE_CHOICES, default=MEDIUM)

    def __str__(self):
        return f"{self.get_drink_size_display()} {self.get_drink_kids_choices_display()} {self.get_drink_temp_display()} {self.get_drink_kids_flavor_choices_display()}"

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} - {self.user.username}"
