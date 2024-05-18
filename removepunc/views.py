from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request,'index.html')

# def correct(request):
#    djtext =request.GET.get('text','default')
#    print(djtext)

#    return HttpResponse("remove puncta")

def analyze(request):
    djtext =request.GET.get('text','default')
    removepunc =request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    lowcaps=request.GET.get('lowcaps','off')
    analyzed=""
    if (removepunc=="on" or fullcaps =="on" or lowcaps =="on"):
        if removepunc == "on":
            analyzed=""
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            djtext=analyzed
            params={'text':djtext ,'purpose': "Removing punctuations",'analyzed_text':analyzed}

        if fullcaps =="on":
            analyzed=""
            for char in djtext:
                analyzed=analyzed+char.upper()
            djtext=analyzed
            
            params={'text':djtext ,'purpose': "Upper case ",'analyzed_text':analyzed}
        
        
        if lowcaps =="on":
            analyzed=""
            for char in djtext:
                analyzed=analyzed+char.lower()
            djtext=analyzed
            params={'text':djtext ,'purpose': "lower case ",'analyzed_text':analyzed}
        
        return render (request,'analyze.html',params)

    else:
        return HttpResponse('error')