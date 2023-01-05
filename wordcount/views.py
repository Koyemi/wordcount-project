from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
    return render(request, 'aboutme.html')

def homepage(request):
    return render(request, 'home.html')


def Koko(request):
     return HttpResponse('Hi, I am Koko/ Koyemi, How was your time in this webpage, I am 100% sure it sucked!')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
            #increase
        else:
            # add to worddictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sortedwords': sortedwords})
