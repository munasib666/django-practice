from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    vowel = request.GET.get('vowel','off')
    evenodd = request.GET.get('evenodd','off')
    dtoh = request.GET.get('dtoh','off')
    btod = request.GET.get('btod','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose':'removed punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif vowel == 'on':
        vowel ='aeiou'
        analyzed=''
        for char in djtext:
            if char  in vowel:
                analyzed = analyzed+char
        params ={'purpose':'vowel','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    elif evenodd == 'on':
        a = int(djtext)
        if a%2==0:
            analyzed  = "jor"
        else:
            return HttpResponse('Bijor')
        params = {'purpose': 'Odd Even checker', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif dtoh == 'on':
        a = int(djtext)
        b = format(a, '02x')
        analyzed  = b
        params = {'purpose': 'Decimal to Hexadecimal converter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse('Erorr')