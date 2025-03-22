from django.shortcuts import render
from .models import Product, Category, Tag


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(description__icontains=search_query)

    # Filter by category
    category_id = request.GET.get('category', '')
    if category_id and category_id != 'all':
        products = products.filter(category_id=category_id)

    # Filter by tags
    selected_tags = request.GET.getlist('tags')
    if selected_tags:
        for tag_id in selected_tags:
            products = products.filter(tags__id=tag_id)

    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_tags': selected_tags,
    }

    return render(request, 'index.html', context=context)
