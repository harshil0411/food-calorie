from django.shortcuts import render


# Create your views here.
def home(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'spdwxHwE7hDs4xVR/eSVPQ==zYNauQEAY39rmqro'})
        try:
            api = json.loads(api_request.content)
            print(api["items"], "=======")
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api["items"]})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
