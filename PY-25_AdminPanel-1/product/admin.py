from django.contrib import admin
from .models import Product
from django.contrib.admin.options import ModelAdmin

admin.site.site_title = 'Backend Development'
admin.site.site_header = 'Ömer YILDIRIM'
admin.site.index_title = 'My Index Page'


# ------------------ Product ------------------

class ProductAdmin(ModelAdmin):
    #görüntülenecek alanlar:
    list_display = ('id','name', 'description', 'is_in_stock',)
    # değiştirilebilecek alanlar:
    list_editable = ('is_in_stock',)
    # Kayda gitmek için linkleme:
    list_display_links = ['name', 'id']
    # filtreleme: 
    list_filter = ['is_in_stock', 'create_date', 'update_date']
    # arama yapılacak alanlar:
    search_fields = ['name', 'id']
    # sıralama:
    ordering = ['-name']
    #sayfa başına kayıt sayısı:
    list_per_page = 20



admin.site.register(Product, ProductAdmin)



# Alternative

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['author', 'post', 'created_at', 'is_approved']
#     list_display_links = ['post']
#     list_editable = ["is_approved"]   
#     search_fields = ["text", "author"]
#     list_filter = ["is_approved", "created_at"]
#     ordering = ["-created_at"]
#     readonly_fields = ["created_at"]