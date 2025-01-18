from django.forms import widgets
from django.utils.safestring import mark_safe


class GrapeJSWidget(widgets.Textarea):
    class Media:
        css = {
            'all': [
                'https://unpkg.com/grapesjs/dist/css/grapes.min.css',
                'https://unpkg.com/grapesjs/dist/css/grapesjs-preset-webpage.min.css',
                'https://unpkg.com/grapick/dist/grapick.min.css',
            ]
        }
        js = [
            'https://unpkg.com/grapesjs',
            'https://unpkg.com/grapesjs-preset-webpage',
            'https://unpkg.com/grapesjs-blocks-basic',
            'https://unpkg.com/grapesjs-plugin-forms',
            'https://unpkg.com/grapesjs-component-countdown',
            'https://unpkg.com/grapesjs-plugin-export',
            'https://unpkg.com/grapesjs-tabs',
            'https://unpkg.com/grapesjs-custom-code',
            'https://unpkg.com/grapesjs-touch',
            'https://unpkg.com/grapesjs-parser-postcss',
            'https://unpkg.com/grapesjs-tooltip',
            'https://unpkg.com/grapesjs-tui-image-editor',
            'https://unpkg.com/grapesjs-typed',
            'https://unpkg.com/grapesjs-style-bg',
        ]

    def __init__(self, *args, css_files=None, **kwargs):
        """
        Initialize the widget with optional custom CSS files.
        :param css_files: List of CSS file URLs to be included in the GrapeJS editor.
        """
        super().__init__(*args, **kwargs)
        self.css_files = css_files or []

    def render(self, name, value, attrs=None, renderer=None):
        # Render the textarea for GrapeJS
        html = super().render(name, value, attrs, renderer)

        # Generate custom CSS links
        custom_css_links = ''.join(
            f'<link rel="stylesheet" href="{css}" type="text/css">' for css in self.css_files
        )

        # Add GrapeJS initialization script with plugins and CSS
        grapejs_script = f"""
        <div id="gjs-container-{name}" style="height: 500px; border: 1px solid #ddd; margin-top: 10px;"></div>
        
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                var editor = grapesjs.init({{
                    container: '#gjs-container-{name}',
                    height: '80vh',
                    fromElement: true,
                    showOffsets: true,
                    assetManager: {{
                        embedAsBase64: true,
                        assets: [],
                    }},
                    selectorManager: {{ componentFirst: true }},
                    styleManager: {{
                        sectors: [
                            {{
                                name: 'General',
                                properties: [
                                    'width', 'min-height', 'margin', 'padding'
                                ],
                            }},
                            {{
                                name: 'Typography',
                                properties: [
                                    'font-family', 'font-size', 'font-weight', 'color', 'letter-spacing', 
                                    'line-height', 'text-align', 'text-shadow',
                                ],
                            }},
                            {{
                                name: 'Decorations',
                                properties: [
                                    'border-radius', 'border', 'box-shadow', 'background',
                                ],
                            }},
                        ],
                    }},
                    plugins: [
                        'gjs-blocks-basic',
                        'grapesjs-plugin-forms',
                        'grapesjs-component-countdown',
                        'grapesjs-plugin-export',
                        'grapesjs-tabs',
                        'grapesjs-custom-code',
                        'grapesjs-touch',
                        'grapesjs-parser-postcss',
                        'grapesjs-tooltip',
                        'grapesjs-tui-image-editor',
                        'grapesjs-typed',
                        'grapesjs-style-bg',
                        'grapesjs-preset-webpage',
                    ],
                    pluginsOpts: {{
                        'gjs-blocks-basic': {{ flexGrid: true }},
                        'grapesjs-preset-webpage': {{
                            modalImportTitle: 'Import Template',
                            modalImportLabel: '<div style="margin-bottom: 10px;">Paste here your HTML/CSS and click Import</div>',
                            modalImportContent: function(editor) {{
                                return editor.getHtml() + '<style>' + editor.getCss() + '</style>';
                            }},
                        }},
                        'grapesjs-tooltip': {{
                            tooltipBgColor: '#333',
                            tooltipColor: '#fff',
                        }},
                    }},
                }});
                


                // Inject custom CSS files into the GrapeJS iframe
                var customCssFiles = {self.css_files};
                editor.on('load', function() {{
                    var iframe = editor.Canvas.getFrameEl();
                    var head = iframe.contentDocument.head;
                    customCssFiles.forEach(function(cssFile) {{
                        var link = document.createElement('link');
                        link.rel = 'stylesheet';
                        link.href = cssFile;
                        head.appendChild(link);
                    }});
                }});
                
                // Update the textarea value on changes in GrapeJS editor
                editor.on('update', () => {{
                    document.querySelector('[name="{name}"]').value = editor.getHtml();
                }});
            }});
        </script>
        """
        return mark_safe(html + grapejs_script)
