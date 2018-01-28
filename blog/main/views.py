from django.shortcuts import render

def main(request):
    '''
    Render the main page
    '''
    return render(request, 'main/main.html')

def latestnews(request):
    '''
    Render the latestnews page
    '''
    return render(request, 'main/latestnews.html')

def discount(request):
    '''
    Render the discount page
    '''
    return render(request, 'main/discount.html')

def recommend(request):
    '''
    Render the recommend page
    '''
    return render(request, 'main/recommend.html')

def explain(request):
    '''
    Render the explain page
    '''
    return render(request, 'main/explain.html')
