from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from rest_framework.exceptions import ValidationError
from products.services import check_product_stock
from django.db import transaction
from addresses.services import get_user_address_or_404
from payments.services import create_payment
from coupons.services import get_valid_coupon_or_none, apply_coupon_discount, increment_coupon_usage

@transaction.atomic
def create_order_from_card(user, card, delivery_address_id, billing_address_id, card_data, coupon_code=None):
    cardItem = card.items.select_related("product").all()
    if not cardItem:
        raise ValidationError({'error':'Your card is empty'})
        
    delivery_address = get_user_address_or_404(user, delivery_address_id)
    billing_address = get_user_address_or_404(user, billing_address_id)

    coupon = get_valid_coupon_or_none(coupon_code)

    order = Order.objects.create(
        user=user, 
        delivery_address=delivery_address, 
        billing_address=billing_address,
        coupon = coupon,
    )

    for item in cardItem:
        check_product_stock(item.product, item.quantity)

        OrderItem.objects.create(
            order = order,
            product = item.product,
            quantity = item.quantity,
            price = item.product.price
        )

    order.calculate_total()

    paymentResult = create_payment(user, order, card_data)

    card.items.all().delete()

    return order, paymentResult