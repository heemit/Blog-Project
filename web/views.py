from django.shortcuts           import render, get_object_or_404
from django.core.paginator      import Paginator
from .models                    import Blog, BlogCategory

# Helper function to handle common filtering, pagination, and context setup
def get_blog_context(request):
    # Get the search query and category slug from the GET request
    query           =   request.GET.get('query', '').strip()
    category_slug   =   request.GET.get('category', '').strip()

    # Fetch blogs and filter based on query and category
    blogs           =   Blog.objects.all()
    
    # Apply query filtering if provided
    if query:
        blogs = blogs.filter    (title__icontains=query)
    
    # Apply category filtering if provided
    if category_slug and category_slug != 'all':
        blogs = blogs.filter    (category__slug=category_slug)

    # Pagination setup
    paginator       =   Paginator(blogs, 6)  # Paginate by 6 blogs per page
    page_number     =   request.GET.get('page')
    page_obj        =   paginator.get_page(page_number)
    
    # Get categories for sidebar filter
    categories      =   BlogCategory.objects.all()

    # Return everything needed to render the page
    return {
        'page_obj': page_obj,
        'categories': categories,
        'query': query,
        'category_slug': category_slug
    }

# Function-Based Views
def index(request):
    # Home page with a photo and a quote
    return render(request, 'web/index.html')

def blog_list(request):
    # Get blog context (filtered blogs, pagination, categories, search query, etc.)
    context = get_blog_context(request)
    return render(request, 'web/blog_list.html', context)

def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'web/blog_details.html', {'blog': blog})

def search(request):
    # Get blog context (same as in blog_list view)
    context = get_blog_context(request)
    return render(request, 'web/blog_list.html', context)
