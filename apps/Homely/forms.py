from django.forms import ModelForm
from .models import *

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class NegocioForm(ModelForm):
    class Meta:
        model = Negocio
        fields = '__all__'

class ReseñaForm(ModelForm):
    class Meta:
        model = Reseña
        fields = '__all__'

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PromocionForm(ModelForm):
    class Meta:
        model = Promocion
        fields = '__all__'

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
