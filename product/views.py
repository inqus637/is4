from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from product.models import Product
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_id','name', 'trader_name','price','mtz','sell14','sell7','ost','road','summ']

def product_list(request, template_name='product/product_list.html'):
    product = Product.objects.all()
    data = {}
    data['object_list'] = product
    return render(request, template_name, data)

def product_create(request, template_name='product/product_form_new.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product:product_list')
    return render(request, template_name, {'form':form})

def product_update(request, pk, template_name='product/product_form_edit.html'):
    product= get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product:product_list')
    return render(request, template_name, {'form':form})

def product_delete(request, pk, template_name='product/product_confirm_delete.html'):
    product= get_object_or_404(Product, pk=pk)    
    if request.method=='POST':
        product.delete()
        return redirect('product:product_list')
    return render(request, template_name, {'object':product})

def index_view(request):
    return render(request, 'product/123.html')


