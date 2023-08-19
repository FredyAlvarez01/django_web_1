from django.shortcuts import render, HttpResponse

html_base = """
<h1> mi web </h1>
<ul>
<li><a href = "/" >Portada</a></li>
<li><a href = "/about-me" >Acerca de </a></li>
<li><a href = "/portfolio" >Portafolio  </a></li>
<li><a href = "/contact" >Contacto  </a></li>

</ul>
"""
# Create your views here.

def home(request):
    
    return render(request, "core/home.html") 
        #HttpResponse(html_base+"<h1> mi web </h1><p>jhsgajsgdjahsd </p>")

def about(request):
    #return HttpResponse(html_base+"<h1> mi web </h1><h2>Acerca de: </h2> <p>Hola me llamo fredy alvarez y soy programador</p>")
     return render(request, "core/about.html") 
 

    # return HttpResponse(html_base+"<h1> portafolio </h1><h2>Acerca de: </h2> <p>productos electronicos para gamers</p>")

def contact(request):
    return render(request, "core/contact.html")
    #return HttpResponse(html_base+"<h1> Contacto </h1><h2>Acerca de: </h2> <p>empresa fundada en el 2018</p>")