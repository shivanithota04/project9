from django.shortcuts import render
from django.views import View
# Create your views here.
from .models import Product


class DisplayView(View):
    def get(self, request):
        qs = Product.objects.all()
        con_dict = {"records": qs}
        return render(request, 'display.html', con_dict)


from django.shortcuts import render

# Create your views here.
