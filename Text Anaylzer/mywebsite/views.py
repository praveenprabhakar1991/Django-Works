from django.http import HttpResponse
from django.shortcuts import render

def navigationpanel(request):
     list = '''
     <h2> My Github page </h2>
     <a href = 'https://github.com/praveenprabhakar1991'> <p> ***Click to View*** </p> </a>
     <h2> My Youtube Page </h2>
     <a href = 'https://www.youtube.com/watch?v=mB34HoNog6U'> <p> ***Click to View***  </p> </a>
     <h2> My Facebook Page </h2>
     <a href = 'https://www.facebook.com/prabhakarbonez'> <p> ***Click to View***  </p> </a>
     <h2> My Instagram page </h2>
     <a href = 'https://www.instagram.com/praveen_prabhakar_/'> <p> ***Click to View*** </p> </a> 
     <a href = '/'> Back to Home Page </a>
     '''
     return HttpResponse(list)

def index(request):
     # return HttpResponse("<h1> index Page </h1>")
     # parameters = { 'name' : 'Prabhakar' , 'place' : 'Bengaluru' }
     # return render(request, 'index.html', parameters)
     return render(request, 'index.html')

def analyzer(request):
     # Get the text
     djtext = request.POST.get('text','default')

     # Check Checkbox Values
     removepunc = request.POST.get('removepunc','off')
     caps = request.POST.get('caps','off')
     newlineremover = request.POST.get('newlineremover', 'off')
     xtraspaceremover = request.POST.get('xtraspaceremover' , 'off')
     numremover = request.POST.get('numremover' , 'off')
     charcount = request.POST.get('charcount', 'off')

     # Remove punctuation if the 'removepunc' flag is 'on'
     if removepunc == 'on':
          analyzed = " "
          punctuations = '''!@#$%^&*()_+-=[]{};:'",.<>?/`~'''
          for char in djtext:
               if char not in punctuations:
                    analyzed += char
          parameters = {'purpose' : 'Removed Punctuations' , 'analyzed_text' : analyzed}
          djtext = analyzed

     # Converted To Uppercase Text if the 'caps' flag is 'on'
     if caps == 'on':
          analyzed = " "
          for char in djtext:
               analyzed += char.upper()
          parameters = {'purpose' : '( Converted To Uppercase Text )' , 'analyzed_text' : analyzed}
          djtext = analyzed

     # Removed New Lines if the 'newlineremover' flag is 'on'
     if newlineremover == 'on':
          analyzed = " "
          for char in djtext:
               if char != '\n' and char!= '\r':
                    analyzed += char
          parameters = {'purpose' : 'Removed New Lines' , 'analyzed_text' : analyzed}
          djtext = analyzed

     # Removed Extra Spaces if the 'xtraspaceremover' flag is 'on'
     if xtraspaceremover == 'on':
          analyzed = " "
          for index, char in enumerate(djtext):
               # It is for an extraspace in the last of the string
               if char == djtext[-1]:
                    if not (djtext[index] == " "):
                         analyzed += char
               elif not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed += char
          parameters = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
          djtext = analyzed

     # Removed Numbers if the 'numremover' flag is 'on'
     if numremover == 'on':
          analyzed = " "
          numbers = '0123456789'
          for char in djtext:
               if char not in numbers:
                    analyzed += char
          parameters = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}

     # Character Count if the 'charcount' flag is 'on'
     if charcount == 'on':
          analyzed = " "
          for char in djtext:
               analyzed = len(djtext)
          parameters = {'purpose': 'Character Count', 'analyzed_text': analyzed}
          djtext = analyzed

     if (removepunc != 'on' and caps != 'on' and newlineremover != 'on' and xtraspaceremover != 'on' and charcount != 'on' and numremover != 'on'):
          return HttpResponse('ERROR! Please Select Any Operation and Try Again!')

     return render(request, 'analyzer.html', parameters)