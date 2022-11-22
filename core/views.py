from django.http import HttpResponse

def home(request):
   text = """<h1>My new website.</h1>"""
   return HttpResponse(text)
