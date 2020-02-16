from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
    return render(request, "chat.html", {})


def logged(request):
    try :
        bot_name = request.POST["bot_name"]
        streamer_name = request.POST["streamer_name"]
        stream_token = request.POST["stream_token"]

        return render(
            request,
            "chat_logged.html",
            {
                "streamer_name": streamer_name,
                "stream_token": stream_token,
                "bot_name": bot_name,
            },
        )
    except MultiValueDictKeyError :
        return redirect("/")


def redirect_style_css(request):
    
    response = redirect("/static/css/styles.css")
    print("redirect to /static/css/styles.css")
    return response

def redirect_favicon(request):
    response = redirect("/static/images/favicon.ico")
    print("redirect to /static/images/favicon.ico")
    return response