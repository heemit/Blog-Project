from django.contrib         import admin
from django.db              import models
from tinymce.widgets        import TinyMCE
from tinymce.models         import HTMLField
from django.utils.text      import slugify

# Import models
from .models                import Blog, BlogCategory

# Generic Admin Class
class GenericAdmin(admin.ModelAdmin):
    # Use TinyMCE for TextField and HTMLField
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
        HTMLField: {"widget": TinyMCE()},
    }

    def get_readonly_fields(self, request, obj=None):
        """Returns readonly fields for the model in the admin."""
        readonly_fields = [field.name for field in self.model._meta.fields if not field.editable]
        return readonly_fields + ['created_at', 'updated_at', 'created_by']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user  # Use the User object
        obj.updated_by = request.user  # Always update on save
        super().save_model(request, obj, form, change)

# BlogCategory Admin Customizations
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display    =   ['category', 'slug']
    search_fields   =   ['category', 'slug']
    list_per_page   =   50
    list_editable   =   ['slug']
    list_filter     =   []

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.category)  # Automatically generate slug if empty
        super().save_model(request, obj, form, change)

# Blog Admin Customizations
class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
        HTMLField: {"widget": TinyMCE()},
    }

    list_display    =   ["id", "title", "category", "slug", "order_by", "created_at", "updated_at"]
    list_editable   =   ["category", "slug", "order_by"]
    list_filter     =   ["category", "order_by"]
    search_fields   =   ["category", "title", "sub_title", "slug"]
    list_per_page   =   50

    fieldsets = (
        (None, {
            'fields': ('title', 'sub_title', 'thumbnail', 'category', 'featured_text', 'text', 'slug', 'readtime', 'tags', 'order_by'),
        }),
    )

    def save_model(self, request, obj, form, change):
        # Auto-generate the slug if not provided, but only for new objects
        if not obj.slug:
            obj.slug = slugify(obj.title)

        # Ensure the slug doesn't exceed 255 characters
        if len(obj.slug) > 255:
            obj.slug = obj.slug[:255]

        # Automatically set 'created_by' and 'updated_by' fields based on logged-in user
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user  # Always update on save
        
        super().save_model(request, obj, form, change)

# Register BlogCategory and Blog with their custom Admin classes dynamically
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
