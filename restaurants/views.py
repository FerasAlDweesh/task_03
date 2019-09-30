from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
	"my_list" : [
    {"restaurant_name" : "Elevation",
    "food_type" : "burger"}, 

    {"restaurant_name" : "Five Guys",
    "food_type" : "burger"}, 

    {"restaurant_name" : "Shake Shack",
    "food_type" : "burger"}, 
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object" : {
    "restaurant_name": "Pizza Hut",
    "food_type" : "pizza" 
    }
    }
    return render(request, 'detail.html', context)
