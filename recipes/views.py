from django.shortcuts import render
import requests 
from django.conf import settings
# Create your views here.
def index(request):
    # Get 'q' parameter from the request, default to "pork"
    query_set = request.GET.get('userText', 'pork')

    response = requests.get(
        f"https://api.edamam.com/api/recipes/v2?type=public&q={query_set}&app_id={settings.EDAMAM_APP_ID}&app_key={settings.EDAMAM_APP_KEY}"
    )

    json_response = response.json()
    recipes = json_response.get('hits', [])

    return render(request, 'recipes/index.html', {
        "recipes": recipes,
    })

def recipe_search(request):
    if request.method == 'POST':
        user_text = request.POST.get('userText')
        url = (
            f"https://api.edamam.com/api/recipes/v2"
            f"?type=public&q={user_text}"
            f"&app_id={settings.EDAMAM_APP_ID}"
            f"&app_key={settings.EDAMAM_APP_KEY}"
        )
        response = requests.get(url)
        json_response = response.json()
        recipes = json_response.get('hits', [])
        return render(request, 'recipes/index.html', {
            "recipes": recipes,
        })
    else:
        return render(request, 'recipes/index.html', {
            "recipes": [],
        })
    
    
def about(request):
    return render(request, 'recipes/about.html')

def contact(request):
    name = "kenya"
    url = f"https://restcountries.com/v2/name/{name}"
    respnse=requests.get(url).json()
    flag = respnse[0]['flags']['png']
    return render(request, 'recipes/contact.html',{
        'flag':flag
    })

