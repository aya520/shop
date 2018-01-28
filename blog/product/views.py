from django.shortcuts import render
def product(request):
    '''
    Render the product page
    '''
    return render(request, 'product/product.html')

def a(request):
    '''
    Render the a page
    '''
    return render(request, 'product/a.html')

def b(request):
    '''
    Render the b page
    '''
    return render(request, 'product/b.html')

def c(request):
    '''
    Render the c page
    '''
    return render(request, 'product/c.html')

def d(request):
    '''
    Render the d page
    '''
    return render(request, 'product/d.html')

