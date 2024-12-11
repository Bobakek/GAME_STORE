
from django.contrib import admin
from .models import Game, Buyer

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')  # Отображение полей в списке
    list_filter = ('size', 'cost')           # Фильтрация по полям size и cost
    search_fields = ('title',)               # Поиск по полю title
    list_per_page = 20                       # Ограничение записей до 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')  # Отображение полей в списке
    list_filter = ('balance', 'age')          # Фильтрация по полям balance и age
    search_fields = ('name',)                 # Поиск по полю name
    list_per_page = 30                        # Ограничение записей до 30
    readonly_fields = ('balance',)            # Поле balance только для чтения
