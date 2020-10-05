from django import forms
from .models import Inventory


class InventoryForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = ['name','description','price','image']

		widgets = {
			'name' : forms.TextInput(attrs={"placeholder":"Name", "onfocus":"this.value = '';","onblur":"if (this.value=='') this.value = this.defaultValue","required":""}),
			'description' : forms.TextInput(attrs={"placeholder":"Email", "onfocus":"this.value = '';","onblur":"if (this.value=='') this.value = this.defaultValue","required":""}),
			'price' : forms.NumberInput(attrs={"placeholder":"Price","onfocus":"this.value = '';","onblur":"if (this.value=='') this.value = this.defaultValue","required":""}),
			
		}