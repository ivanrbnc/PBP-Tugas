from django.shortcuts import render
from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_watchlist (request):
    watchlist_data = WatchlistItem.objects.all()
    context = {
        'nama': 'Ivan Rabbani Cezeliano',
        'npm' : '2106701892',
        'message': which_message(),
        'watchlist': watchlist_data
    }
    return render(request, "mywatchlist.html", context)

def show_xml (request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json (request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# If you want to see the html version for WatchlistItem
# def show_html (request):
#     watchlist_data = WatchlistItem.objects.all().values()
#     return HttpResponse(watchlist_data)

# Bonus (!)
def which_message():
    # Simple counter
    counter_true = 0
    counter_false = 0

    #Get every "watched" value from WatchlistItem
    watchlist_data = WatchlistItem.objects.all().values("watched")

    # Categorize each of them
    for object in watchlist_data:
        if object == {'watched': True}:
            counter_true += 1
        else:
            counter_false += 1
    
    # Return by condition
    if counter_true >= counter_false:
        return "Selamat, kamu sudah banyak menonton!"
    else:
        return "Wah, kamu masih sedikit menonton!"
