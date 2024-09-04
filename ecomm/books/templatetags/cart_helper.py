from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(book, session):
    cart = session.get('cart')
    if str(book.id) in cart.keys():
        return True
    return False

@register.filter(name='sum_of_cart')
def sum_of_cart(books, session):
    cart = session.get('cart', {})
    total_cart = 0
    for book in books:
        if str(book.id) in cart:  # Solo sumar los libros que están en el carrito
            total_cart += book.price
    return "{:.2f}".format(total_cart)  # Retornar el total formateado con 2 decimales
