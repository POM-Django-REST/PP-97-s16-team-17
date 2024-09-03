from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

@login_required(login_url='/login/')
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order created successfully!')
            return redirect('order_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = OrderForm()

    return render(request, 'order_form.html', {'form': form})

@login_required(login_url='/login/')
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated successfully!')
            return redirect('order_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = OrderForm(instance=order)

    return render(request, 'order_form.html', {'form': form})

@login_required(login_url='/login/')
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order deleted successfully!')
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})