from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # return HttpResponse("HOME")

def analyzer(request):
    text = request.POST.get("text","default")
    removepun = request.POST.get("removepunc","off")
    fullcap = request.POST.get("fullcaps", "off")
    newlinerem = request.POST.get("nlrem", "off")

    if removepun == 'on':
        analyzed = ""
        punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in text:
            if char not in punc:
                analyzed = analyzed + char
        params = {
            'purpose': 'REMOVE PUNCTUATIONS',
            'analyzed_text':analyzed
        }
        return render(request,'analyze.html',params)

    elif fullcap == 'on':
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {
            'purpose': 'UPPER CASE CONVERTER',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)

    elif newlinerem == 'on':

        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {
            'purpose': 'NEWLINE REMOVER',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)

    else:

        analyzed = ""
        params = {
            'purpose': 'ERROR',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)

    return render(request,'analyze.html',params)
