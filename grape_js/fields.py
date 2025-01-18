from django.forms import CharField
from grape_js.widgets import GrapeJSWidget

class GrapeJsFormField(CharField):
    def __init__(self, *args, css_files=None, **kwargs):
        """
        Initialize the GrapeJS form field.
        :param css_files: List of CSS file URLs to be included in the GrapeJS editor.
        """
        kwargs['widget'] = GrapeJSWidget(css_files=css_files)
        super().__init__(*args, **kwargs)