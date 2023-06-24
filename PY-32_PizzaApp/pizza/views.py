from django.shortcuts import render
from .models import Pizza

#? from django.contrib.auth.decorators import login_required

#? @login_required(login_url='user_login')
def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'home.html', {'pizzas':pizzas})


# ----------------------------------------------
# Class Based Views (CBV)
# ----------------------------------------------
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    Order, OrderForm
)

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

# ----------------------------------------------
# FixView
# ----------------------------------------------
class FixView(LoginRequiredMixin):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order_list')
    #LoginRequiredMixin:
    login_url = 'user_login'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-id')
    

# ----------------------------------------------
# Views
# ----------------------------------------------
# List:
class OrderListView(FixView, ListView):
    template_name = 'pizza/order_list.html'
    context_object_name = 'orders'
    # ordering = ['-id'] #! get queryset içinde olağan super().get_queryset() fonksiyonunu bozduğumuz için ordering muhtemlen çalışmaz, o yüzden get_queryset içinde sıralama yaptık.


# Create:
class OrderCreateView(FixView, CreateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

    # Yeni kayıt sayfası için pizza bilgisi:
    def get_context_data(self, **kwargs):
        # Çıktıyı al:
        kwargs = super().get_context_data(**kwargs)
        # Çıktıya pizza bilgisi ekle:
        pizza_id = self.request.GET.get('pizza', 0)
        # kwargs['pizza'] = Pizza.objects.get(id=pizza_id)
        kwargs['pizza'] = Pizza.objects.filter(id=pizza_id).first()
        return kwargs
    
    def form_valid(self, form):
        # user_id olmadan kaydet ve objeyi oluştur:
        self.object = form.save(commit=False)
        # önce gelen bilgilerle objeyi oluşturup kaydetti, sonra user_id'yi ekle, tekrar kaydet (direk user_id'yi formdan alamıyoruz çünkü obje henüz oluşmadı):
        self.object.user_id = self.request.user.id
        # Objeye pizza_id ekle: (GET ile gelen veri)
        self.object.pizza_id = self.request.GET.get('pizza')
        self.object.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        # Mesaj göster:
        messages.success(request, 'Created.')
        return super().post(request, *args, **kwargs)

# Detail:
class OrderDetailView(FixView, DetailView):
    template_name = 'pizza/order_detail.html'
    context_object_name = 'order'


# Update:
class OrderUpdateView(FixView, UpdateView):
    template_name = 'pizza/order_form.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        # Mesaj göster:
        messages.success(request, 'Updated.')
        return super().post(request, *args, **kwargs)

# Delete:
class OrderDeleteView(FixView, DeleteView):
    
    # template dosyasına gitmeden direkt sil:
    def get(self, request, *args, **kwargs):
        messages.success(request, 'Order deleted successfully!')
        return self.delete(request, *args, **kwargs)
