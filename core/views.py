from django.shortcuts import render

# Create your views here.
def FilterView(request):
    return render(request, "form.html")
