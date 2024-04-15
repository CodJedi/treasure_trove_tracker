from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib import admin
from treasure_trove_tracker.accounts.forms import TreasuryUserCreationForm , TreasuryUserUpdateForm


UserModel = get_user_model()

@admin.register(UserModel)
class TreasuryUserAdmin(auth_admin.UserAdmin):
    model = UserModel
    add_form = TreasuryUserCreationForm
    form = TreasuryUserUpdateForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ()}),
        (('Permissions'), {'fields': ( 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'pk', 'is_superuser', 'is_staff')
    search_fields = ('email',)
    ordering = ('pk',)

