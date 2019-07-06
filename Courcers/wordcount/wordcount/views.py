from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['name']
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

    SortedWord = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':SortedWord})
