from django.http import HttpResponse

def home(request):
   text = """<h1>Welcome to my website.</h1>"""
   return HttpResponse(text)
