from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique book instances

class Coffee(models.Model):
    """model representing type of drink"""
    LATTE = 'latte'
    POUR_OVER = 'pour_over'
    DRIP_BREW = 'drip_brew'
    AMERICANO = 'americano'
    CAPUCCINO = 'capuccino'
    DRINK_TYPE_CHOICES = [
        (LATTE, 'Latte'),
        (POUR_OVER, 'Pour Over'),
        (DRIP_BREW, 'Drip Brew'),
        (AMERICANO, 'Americano'),
        (CAPUCCINO, 'Capuccino'),
    ]
    """Model representing a temp of drink."""
    HOT = 'hot'
    ICED = 'iced'
    DRINK_TEMP_CHOICES = [
        (HOT, 'Hot'),
        (ICED, 'Iced'),
    ]

    # Drink size choices
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    DRINK_SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),

    ]

    # Drink flavor choices
    VANILLA = 'Vanilla'
    HAZELNUT = 'Hazelnut'
    CARAMEL = 'Caramel'
    WHITE_MOCHA = 'White Mocha'
    MOCHA = 'Mocha'
    TOFFEE = 'Toffee'
    BUTTERSCOTCH = 'Butter Scotch'
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
        (BUTTERSCOTCH, 'Butter Scotch'),
        (SF_VANILLA, 'Sugar Free Vanilla'),
        (SF_CARAMEL, 'Sugar Free Caramel'),
        (SF_MOCHA, 'Sugar Free Mocha'),
    ]

    drink_type = models.CharField(
        max_length=20,
        choices=DRINK_TYPE_CHOICES,
        default=LATTE,
    )
    drink_temp = models.CharField(
        max_length=4,
        choices=DRINK_TEMP_CHOICES,
        default=HOT,
    )

    drink_flavor = models.CharField(
        max_length=20,
        choices=DRINK_FLAVOR_CHOICES,
        default=VANILLA,
    )

    drink_size = models.CharField(
        max_length=6,
        choices=DRINK_SIZE_CHOICES,
        default=MEDIUM,
    )

    def __str__(self):
        return f"{self.get_drink_type_display()} {self.get_drink_size_display()} {self.get_drink_flavor_display()} ({self.get_drink_temp_display()})"

class Tea(models.Model):
    # Drink temperature cohices
    HOT = 'hot'
    ICED = 'iced'
    DRINK_TEMP_CHOICES = [
        (HOT, 'Hot'),
        (ICED, 'Iced'),
    ]

    # Drink size choices
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    DRINK_SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]

    # Tea choices
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

    # Flavor syrup options for teas
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

    drink_temp = models.CharField(
        max_length=4,
        choices=DRINK_TEMP_CHOICES,
        default=HOT,
    )

    drink_tea_type = models.CharField(
        max_length=20,
        choices=DRINK_TEA_CHOICES,
        default=BLACK,
    )

    drink_tea_flavor = models.CharField(
        max_length=20,
        choices=DRINK_TEA_SYRUP_CHOICES,
        default=SIMPLE_SYRUP,
    )

    drink_size = models.CharField(
        max_length=6,
        choices=DRINK_SIZE_CHOICES,
        default=MEDIUM,
    )

    def __str__(self):
        return f"{self.get_drink_size_display()} {self.get_drink_tea_type_display()} {self.get_drink_temp_display()} {self.get_drink_tea_flavor_display()}"

class Kids(models.Model):
    # Drink temperature choices
    HOT = 'hot'
    ICED = 'iced'
    DRINK_TEMP_CHOICES = [
        (HOT, 'Hot'),
        (ICED, 'Iced'),
    ]

    # Drink size choices
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    DRINK_SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]

    # Drink choices
    MILK = 'milk'
    LEMONADE = 'lemonade'
    JUICE = 'juice'
    DRINK_KIDS_CHOICES = [
        (MILK, 'Milk'),
        (LEMONADE, 'Lemonade'),
        (JUICE, 'Juice'),
    ]

    # Flavor additions for kids drinks
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
        (RASPBERRY, 'Rapsberry'),
        (WATERMELON, 'Watermelon'),
        (WHIPPED_CREAM, 'Whipped Cream'),
    ]

    drink_temp = models.CharField(
        max_length=4,
        choices=DRINK_TEMP_CHOICES,
        default=ICED,
    )

    drink_kids_choices = models.CharField(
        max_length=15,
        choices=DRINK_KIDS_CHOICES,
        default=JUICE,
    )

    drink_kids_flavor_choices = models.CharField(
        max_length=20,
        choices=DRINK_KIDS_FLAVOR_CHOICES,
        default=STRAWBERRY,
    )

    drink_size = models.CharField(
        max_length=6,
        choices=DRINK_SIZE_CHOICES,
        default=MEDIUM,
    )


    def __str__(self):
        return f"{self.get_drink_size_display()} {self.get_drink_kids_choices_display()} {self.get_drink_temp_display()} {self.get_drink_kids_favor_choices_display()}"