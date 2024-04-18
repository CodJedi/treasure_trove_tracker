from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib import admin
from treasure_trove_tracker.accounts.forms import TreasuryUserCreationForm , TreasuryUserUpdateForm
from treasure_trove_tracker.finance.models import ContactEmailMessage, Comment, Post

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
    list_display = ('email', 'is_superuser', 'is_staff')
    search_fields = ('email',  )
    ordering = ('email', 'pk')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date',)
    list_filter = ('created_date', )
    search_fields = ('title', 'content', 'author__email')
    actions = ['delete_posts',]


    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser or request.user.is_staff:
    #         return qs
    #     return qs.filter(author=request.user)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date',)
    list_filter = ('created_date',)
    search_fields = ('post__title', 'text', 'author__email')
    actions = [ 'delete_comments']

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser or request.user.has_perm('moderate_comments'):
    #         return qs
    #     return qs.filter(author=request.user)
@admin.register(ContactEmailMessage)
class ContactEmailMessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'email', 'message')
    search_fields = ('theme', 'email', 'message')
    list_filter = ('theme', 'email', 'created_at')
    ordering = ('theme', 'email', 'message')