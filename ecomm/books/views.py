from django.shortcuts import render
from .models import Book

def home(request):
    # Manejar el POST para agregar o quitar libros del carrito
    if request.method == 'POST':
        remove = request.POST.get('remove')
        book_id = request.POST.get('book')
        local_cart = request.session.get('cart', dict())
        
        if remove:
            local_cart.pop(book_id, None)  # Eliminar el libro del carrito si se solicita
        else:
            local_cart[book_id] = True  # Agregar el libro al carrito
        
        # Actualizar la sesión con el carrito modificado
        request.session['cart'] = local_cart

    # Obtener el carrito de la sesión, si no existe, crear uno vacío
    cart = request.session.get('cart', {})

    # Pasar el carrito al contexto para usarlo en el template
    context = {
        'books': Book.objects.all(),
        'cart': cart  # Añadir el carrito al contexto
    }
    return render(request, 'books/home.html', context)

def cart(request):
    local_cart = request.session.get('cart',dict())
    book_list = list(local_cart.keys())

    books_in_cart = Book.objects.filter(id__in=book_list) #two _


    return render(request, 'books/cart.html',{'books':books_in_cart})

def checkout(request):
    if request.method == "GET":
        local_cart = request.session.get('cart',dict())
        book_list = list(local_cart.keys())
        books_in_cart = Book.objects.filter(id__in=book_list) #two _
        return render(request, 'books/checkout.html',{'books':books_in_cart})
    else:
        message = "Thank you for your order!"
        request.session['cart'] = dict()
        return render(request, 'books/checkout.html',{'message':message})

                
    
    

               
    
    
    
    