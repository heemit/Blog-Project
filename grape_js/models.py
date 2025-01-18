from django.db          import models
from grape_js.fields    import GrapeJsFormField
from grape_js.widgets   import GrapeJSWidget



class GrapeJsHTMLField(models.TextField):
    def __init__(self, *args, css_files=None, **kwargs):
        """
        Initialize the custom GrapeJS HTML field with optional CSS files.
        :param css_files: List of CSS file URLs to be included in the GrapeJS editor.
        """
        self.css_files = css_files or []
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        # Pass css_files to the form field
        defaults = {
            'form_class': GrapeJsFormField,
            'css_files' : self.css_files,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)