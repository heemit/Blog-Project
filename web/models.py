from django.db                          import models
from django.contrib.auth.models         import User
from django.core.serializers            import serialize
import json

# Simple History Model
from simple_history.models              import HistoricalRecords

# Model Utils
from model_utils                        import FieldTracker

# TinyMCE - For rich text editing
from tinymce.models                     import HTMLField

from grape_js.models                    import GrapeJsHTMLField
# Common Model
class CommonModel(models.Model):
    extra_params    =   models.JSONField        (blank=True, null=True, help_text="Extra parameters related to the model.")
    created_at      =   models.DateTimeField    (auto_now_add=True, blank=True, null=True, help_text="The date and time when the object was created.")
    updated_at      =   models.DateTimeField    (auto_now=True, blank=True, null=True, help_text="The date and time when the object was last updated.")
    created_by      =   models.ForeignKey       (User, blank=True, null=True, on_delete=models.SET_NULL, related_name="created_%(class)s", help_text="The user who created the object.")
    
    history         =   HistoricalRecords(inherit=True)
    tracker         =   FieldTracker()

    admin_meta      =   {}
    
    class Meta:
        abstract = True

    def get_json(self):
        # Serialize the model instance into JSON format
        data = serialize    ('json', [self], ensure_ascii=False)
        
        # Convert the serialized data into a Python object
        data = json.loads   (data)
        
        # Return the first item in the list as we are serializing a single instance
        return data[0] if data else {}

# Blog Category Model
class BlogCategory(CommonModel):
    category    =   models.CharField    (max_length=100, unique=True, help_text="The name of the blog category.")
    slug        =   models.SlugField    (max_length=100, unique=True, blank=True, null=True, help_text="A unique slug for the category, used in URLs.")
    
    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural =   "Blog Categories"
        ordering            =   ['category']
    
    admin_meta = {
        'list_display': ("category", "slug"),
        'list_editable': ("slug",),
        'list_per_page': 50,
    }

# Blog Model
class Blog(CommonModel):

    title               =   models.CharField    (max_length=200, help_text="The title of the blog post.")
    sub_title           =   models.CharField    (max_length=200, blank=True, null=True, help_text="An optional subtitle for the blog post.")
    thumbnail           =   models.CharField    (max_length=255, blank=True, null=True, help_text="The relative path to the blog thumbnail image in GitHub (e.g., 'blog/image1.jpg').")
    category            =   models.ForeignKey   (BlogCategory, null=True, on_delete=models.SET_NULL, help_text="The category to which the blog belongs.")
    featured_text       =   models.TextField    (null=True, blank=True, help_text="A featured text or excerpt from the blog, with rich text support.")
    text                =   models.TextField    (null=True, blank=True, help_text="The main content of the blog post, with rich text support.")
    slug                =   models.SlugField    (unique=True, blank=True, null=True, help_text="A unique slug for the blog, auto-generated based on the title.")
    readtime            =   models.CharField    (max_length=200, null=True, blank=True, help_text="An estimated reading time for the blog post.")
    tags                =   models.TextField    (null=True, blank=True, default='all', help_text="A list of tags for the blog (comma-separated).")
    
    order_by            =   models.IntegerField (default=0, help_text="The ordering of the blog post. Higher numbers come first.")
    
    admin_meta =    {
        'list_display'      :   ("id", "title", "category", "slug", "created_at"),
        'list_editable'     :   ("category",),
        'list_per_page'     :   50,
        'list_filter'       :   ("category",),
        'inline'            :   [{'BlogImage': 'blog'}]
    }

    def __str__(self):
        return str(self.title)
    
    def get_thumbnail_url(self):
        if self.thumbnail:
            return f"https://raw.githubusercontent.com/heemit/Blog-Project/main/media/{self.thumbnail}"
        return "default-image-url"  # URL for a default image in case none is provided
    
    class Meta:
        verbose_name_plural = "Blog"
        ordering            = ['order_by']  # Sort in descending order
        