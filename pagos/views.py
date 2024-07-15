from django.shortcuts import render

# Create your views here.
def pago(request):
    return render(request, 'users/pagos/pago.html')