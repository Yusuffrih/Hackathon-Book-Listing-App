from django.shortcuts import render
from .models import Book, Category

# Create your views here.


def all_books(request):
    book = Book.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                book = book.annotate(lower_name=Lower('name'))
            if sortkey == 'category_name':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            book = book.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            book = book.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('book'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            book = book.filter(queries)
    current_sorting = f'{sort}_{direction}'
    context = {
        'book': book,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'books/all_books.html', context)


def book_details(request, book_id):

    return render(request, 'books/book_details.html')
