from .models import Product
from rest_framework.exceptions import NotFound, ValidationError

def get_Product_or_404(product_id):
    try:
        return Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise NotFound('Category not found')


def check_product_stock(product, quantity):
    if quantity > product.stock:
        raise ValidationError(f"Not enough stock for {product.name}. Available: {product.stock}, Requested: {quantity}")
    
def decrease_product_stock(product, quantity):
    if quantity > product.stock:
        raise ValidationError(f"Cannot decrase stock by {quantity}. Only {product.stock} items available ")
    
    product.stock -= quantity
    product.save()

ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/jpg', 'image/png', 'image/pjpeg']
ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png']

def validate_uploaded_file(file):
    import os
    
    # Dosya uzantısını al ve küçük harfe çevir
    file_ext = os.path.splitext(file.name)[1].lower()
    
    # Uzantı kontrolü
    if file_ext not in ALLOWED_EXTENSIONS:
        raise ValidationError(f'Unsupported file extension. Only JPG, JPEG and PNG files are allowed. Received: {file_ext}')
    
    # Content type kontrolü (varsa)
    if hasattr(file, 'content_type') and file.content_type:
        if file.content_type not in ALLOWED_IMAGE_TYPES:
            raise ValidationError(f'Unsupported file type. Only JPEG and PNG are allowed. Received: {file.content_type}')
    
    # Dosya boyutu kontrolü
    if file.size > 5 * 1024 * 1024:  # 5MB limit
        raise ValidationError('File size exceeds the limit of 5MB.')