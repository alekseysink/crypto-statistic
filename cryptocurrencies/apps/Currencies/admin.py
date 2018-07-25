from django.contrib import admin

# Register your models here.
from cryptocurrencies.apps.Currencies.models import CryptoCurrency, CryptoCurrencyRateData, \
    CryptoCurrencyRateDataChanges


@admin.register(CryptoCurrency)
class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'start_date', 'algorithm', 'created_at')


@admin.register(CryptoCurrencyRateData)
class CryptoCurrencyRateDataAdmin(admin.ModelAdmin):
    list_display = (
        'get_crypto_name',
        'open_rate',
        'high_rate',
        'low_rate',
        'adj_close',
        'close_rate',
        'volume',
        'date'
    )

    ordering = [
        '-date',
    ]

    search_fields = [
        'crypto_currency__symbol'
    ]

    def get_crypto_name(self, obj):
        return obj.crypto_currency.name

    get_crypto_name.short_description = 'Crypto Currency Name'
    get_crypto_name.admin_order_field = 'crypto_currency__name'


@admin.register(CryptoCurrencyRateDataChanges)
class CryptoCurrencyRateChangesAdmin(admin.ModelAdmin):
    list_display = (
        'get_crypto_symbol',
        'changes',
        'date',
    )

    search_fields = (
        'crypto_currency__symbol',
    )

    ordering = (
        '-date',
    )

    def get_crypto_symbol(self, obj):
        return obj.crypto_currency.symbol