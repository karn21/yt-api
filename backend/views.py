from django.shortcuts import render
from api.models import Video
from django.db.models import Q


# dashboard view
def dashboard(request):
    # get all videos
    videos = Video.objects.all()

    if request.method == 'POST':
        # get search query for filtering
        search = request.POST.get('search')
        if search:
            # filter with origin search query
            final_qs = videos.filter(Q(title__icontains=search) | Q(
                description__icontains=search)).distinct()
            # split query string
            search = search.split(" ")
            # search with each query string
            for q in search:
                qs = videos.filter(Q(title__icontains=q) | Q(
                    description__icontains=q)).distinct()
                final_qs = (qs | final_qs).distinct()
            videos = final_qs

        # get sorting field
        order_field = request.POST.get('order_field')
        if order_field:
            # get sorting order (asc/desc)
            order = request.POST.get('order')
            if order == 'descending':
                order_field = '-'+order_field
            videos = videos.order_by(order_field)

    context = {
        'videos': videos
    }
    return render(request, "dashboard.html", context)
