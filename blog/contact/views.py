from django.shortcuts import render

# Create your views here.

def contact(request):
    '''
    Render the contact page
    '''
    if request.method == 'GET':
        return render(request, 'contact/contact.html')
    # POST
    if request.method == 'POST':
        context = {'result':'表單送出成功，我們將會與您聯絡。'}
        return render(request, 'contact/contact.html', context)
    