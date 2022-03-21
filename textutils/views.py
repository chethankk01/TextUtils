from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def removepunc(request):
    djtext = request.POST.get("text", "default")
    removepunc = request.POST.get("removepunc", "off")
    fullcaps = request.POST.get('fullcaps', 'off')
    # newlineremover = request.GET.get('newlineremover', 'off')
    # extraspaceremover = request.GET.get('extraspaceremover', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == "on":
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {"purpose": "Removed punctuations", "analyzed_text": analyzed}
    if fullcaps == "on":
        if len(analyzed) > 0:
            newtext = ""
            for i in range(len(analyzed)):
                newtext += analyzed[i].upper()
            analyzed = newtext
        else:
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
    # if newlineremover == "on":
    #     analyzed = ""
    #     for char in djtext:
    #         if char != "\n" and char!="\r":
    #             analyzed = analyzed + char
    #     params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    # if (extraspaceremover == "on"):
    #     analyzed = ""
    #     for index, char in enumerate(djtext):
    #         if not (djtext[index] == " " and djtext[index + 1] == " "):
    #             analyzed = analyzed + char
    #     params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)


