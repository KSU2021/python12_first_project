
from django.db import models
from product.models import Product
from django.contrib.auth import get_user_model


User = get_user_model()

STATUS_CHOICES = (
    ('open', 'Открытый'),
    ('in_progress', 'В обработке'),
    ('canceled', 'Отмененный'),
    ('finished', 'Завершенный')
)

class Order(models.Model):
    total_sum = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT,
                             related_name='orders')
    status = models.CharField(max_length=20,
                              choices = STATUS_CHOICES)
    products = models.ManyToManyField(Product,
                                      through='OrderItem')

    class Meta:
        db_table = 'order'

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              on_delete=models.RESTRICT,
                              related_name='items')
    product = models.ForeignKey(Product,
                                on_delete=models.RESTRICT,
                                related_name='order_items')
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        db_table = 'order_items'
    #class Meta для того, чтобы задать параметры общие, не касающиеся какого-то конкретного поля



