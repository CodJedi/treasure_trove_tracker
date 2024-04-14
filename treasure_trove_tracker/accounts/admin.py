from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from treasure_trove_tracker.accounts.models import TreasuryUser
from treasure_trove_tracker.finance.models import Transaction, Category, Trades, ProfitGoal

admin.site.register(TreasuryUser, UserAdmin)
admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(Trades)
admin.site.register(ProfitGoal)



class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'transaction_type',
        'amount',
        'date',
    )
    list_filter = (
        'date',
        'transaction_type',
    )
    search_fields = (
        'description',
    )


# admin.site.register(TransactionAdmin)
