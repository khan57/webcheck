from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request,'home.html',{"name":"Haseeb"})

def count(request):
	fulltxt=request.GET['fulltext']
	print(fulltxt)
	wordlist=fulltxt.split()
	print(wordlist)
	print(wordlist[1])
	wordDictionary={}
	for word in wordlist:
		if word in wordDictionary:
			#increment
			wordDictionary[word]+=1
		else:
			#add to dictionary
			wordDictionary[word]=1

	print(wordDictionary)


	return render(request,'count.html',{'ftext':fulltxt,'count':len(wordlist),'allwords':wordDictionary.items()})

def firstpage(request):
	return HttpResponse('<h1>This is my first page in django!! yeah</h1>')
def about(request):
	return render(request,'aboutus.html',{'name':'HaseebKhattak'})