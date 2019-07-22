from django.http import HttpResponse
from django.shortcuts import render
def index(request):
     return render(request,'index.html')

def detail(request):
     djtext = request.POST.get('text','default')
     showdetail = request.POST.get('remove_punctuation','off')
     full_cap = request.POST.get('full_cap','off')
     new_line_remove = request.POST.get('new_line_remove','off')
     spaceremove = request.POST.get('space_remover','off')
     extraspaces = request.POST.get('extraspace','off')
     charcount = request.POST.get('charcount','off')

     if showdetail == "on":
          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          analyze =""
          for char in djtext:
               if char not in punctuations:
                    analyze = analyze + char
          params = {'purpose':'Remove Punctuation','analyzed_text':analyze}
          djtext = analyze

     if full_cap =="on":
          analyze=""
          for char in djtext:
               analyze = analyze + char.upper()
               params = {'purpose':'Upper case','analyzed_text':analyze}
          djtext = analyze

     if(new_line_remove =="on"):
          analyze=""
          for char in djtext:
               if char != '\n' and char!='\r':
                    analyze = analyze + char
                    params = {'purpose':'NEw LineRemoverer','analyzed_text':analyze}
               djtext = analyze

     if(spaceremove =="on"):
          analyze=""
          for char in djtext:
               if char != ' ':
                    analyze = analyze + char
                    params = {'purpose':'Space_Removerer','analyzed_text':analyze}
               djtext = analyze



     if(charcount =="on"):
          analyze=""
          count = 0
          for i in range(len(djtext)):
               if djtext[i]==" ":
                    pass
               else:
                    count+=1
                    params = {'purpose':'Extra space Removerer','matter':'No of Chararcter is : ' , 'count':count, 'analyzed_text':analyze}
               djtext = analyze

     if(extraspaces =="on"):
          analyze=""
          for index, char in enumerate(djtext):
               if not(djtext[index] == " " and djtext[index+1] == " "):
                    analyze = analyze + char
                    params = {'purpose':'Extra space Removerer','analyzed_text':analyze}
               djtext = analyze

     if(full_cap!="on" and showdetail!="on" and new_line_remove!="on" and extraspaces!="on" and charcount!="on"):
          return HttpResponse("Error Error Error")
     
     return render(request, 'detail.html', params)

def contact(request):
     return render(request, 'contact.html')




# def about(request):
#      return HttpResponse('''<h1>about</h1> <a href="http://127.0.0.1:8000/" >back_to_home</a>''')
# def kenny(request):
#      return HttpResponse('''<h1>kenny</h1> <a href="http://127.0.0.1:8000/" >back_to_home</a>''')