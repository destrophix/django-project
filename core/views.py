from django.http import HttpResponse

def home(request):
   text = """<h1>Hello World Website using CI/CD pipelining.</h1>"""
   return HttpResponse(text)
