from django.shortcuts import render

def index_admin(request):
    titulo = "Inicio"
    context = {
        "titulo": titulo
    }    
    return render(request, "index-admin.html", context)