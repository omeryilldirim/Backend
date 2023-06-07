from django.contrib import admin
from .models import Product, Review
from django.contrib.admin.options import ModelAdmin

# WYSIWYG (what you see is what you get)

# https://djangopackages.org/grids/g/wysiwyg/
# https://django-ckeditor.readthedocs.io/en/latest/

admin.site.site_title = 'Backend Development'
admin.site.site_header = 'Ömer YILDIRIM'
admin.site.index_title = 'My Index Page'
admin.site.site_url = 'https://www.linkedin.com/in/omeryilldirim/'


# ------------------ Inline ------------------
class ReviewInline(admin.TabularInline):  # Alternatif: StackedInline (farklı görünüm aynı iş)
    model = Review # Model
    extra = 1 # Yeni review ekleme için ekstra boş alan
    classes = ['collapse'] # Görüntüleme tipi (default: tanımsız)


# ------------------ Product ------------------

class ProductModelAdmin(ModelAdmin):
    # görüntülenecek alanlar:
    list_display = ['id','name', 'description', 'is_in_stock',]
    # değiştirilebilecek alanlar:
    list_editable = ('is_in_stock',)
    # Kayda gitmek için linkleme:
    list_display_links = ['name', 'id']
    # filtreleme: 
    list_filter = ['is_in_stock', 'create_date', 'update_date']
    # arama yapılacak alanlar:
    search_fields = ['name', 'id']
    # sıralama:
    ordering = ['id']
    #sayfa başına kayıt sayısı:
    list_per_page = 20
    # Otomatik kaıyıt oluştur:
    prepopulated_fields = {'slug' : ['name']}
    # Tarihe göre filtreleme başlığı:
    date_hierarchy = 'create_date'
    # Form liste görüntüleme
    # fields = (
    #     ('name', 'is_in_stock'),
    #     ('slug'),
    #     ('description')
    # )
    # Detaylı form liste görüntüleme
    fieldsets = (
        ('General Settings', {
            "classes": ("wide",),
            "fields": (
                ('name', "is_in_stock"),
                "slug"
            ),
        }),
        ('Optional Settings', {
            "classes": ("collapse",),
            "fields": ("description",),
            'description': "You can use this section for optionals settings"
        }),
    )    

    inlines = [ReviewInline]

    def set_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f'{count} adet "Stokta Var" olarak işaretlendi.')
    
    def set_out_stock(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f'{count} adet "Stokta Yok" olarak işaretlendi.')

    actions = ('set_in_stock', 'set_out_stock')
    set_in_stock.short_description = 'İşaretli ürünleri stoğa ekle'
    set_out_stock.short_description = 'İşaretli ürünleri stoktan çıkar'

    def added_days_ago(self, object):
        from django.utils import timezone
        different = timezone.now() - object.create_date
        return different.days
    list_display += ['added_days_ago']

    def how_many_reviews(self, object):
        count = object.reviews.count()
        return count
    list_display += ['how_many_reviews']

admin.site.register(Product, ProductModelAdmin)


# ------------------ Review ------------------
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    # raw_id_fields = ('product',) 
    # raw id fields, review içinde product, id olarak görünsün istyorsak kullanılır.
admin.site.register(Review, ReviewModelAdmin)




# Alternative

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['author', 'post', 'created_at', 'is_approved']
#     list_display_links = ['post']
#     list_editable = ["is_approved"]   
#     search_fields = ["text", "author"]
#     list_filter = ["is_approved", "created_at"]
#     ordering = ["-created_at"]
#     readonly_fields = ["created_at"]