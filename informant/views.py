from django.shortcuts import render

def post_list(request):
    return render(request, 'informant/post_list.html', {})
