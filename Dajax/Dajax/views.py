from django.http import HttpResponse

def common(request):
     return HttpResponse("<a href='ajax'>Ajax Base CRUD Operation</a></br><a href='cbv'>Class Base CRUD Operation</a></br><a href='fbv'> Function Base CRUD Operation</a>")