from django.http import HttpResponse

def home(request):
   text = """<h1>Welcome to my website deploying using ci/cd</h1>"""
   return HttpResponse(text)
