from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import InventoryForm
from .models import Inventory

def index(request):
	form = InventoryForm(request.POST, request.FILES or None)
	if form.is_valid():
		form.save()
		form = InventoryForm()
	else:
		form = InventoryForm()

	inventory = Inventory.objects.all()
	context = {'form' : form, 'all_inventory' : inventory}
	return render(request, 'inventory/index.html',context)

def display(request, id):
	try:
	    item = Inventory.objects.get(pk=id)
	except Inventory.DoesNotExist:
	    item = None

	if item != None:
		print(item.image)
		context = {'item' : item}
		return render(request, 'inventory/display.html',context)
	else:
		return index(request)

	# item = Inventory.objects.get(pk=id)
	# if item.DoesNotExist:
	# 	print(item.image)
	# 	context = {'item' : item}
	# 	return render(request, 'inventory/display.html',context)
	# else:
	# 	return render(request, 'inventory/index.html',context)