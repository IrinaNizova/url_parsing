from django.shortcuts import render_to_response
from result.models import DataFromUrl
from sites.models import Sites

def index(request):
    results = Sites.objects.all()
    return render_to_response('index.html', {'results': results})

def details(request, url_id):
    try:
        site = Sites.objects.get(id=url_id)
        result = DataFromUrl.objects.get(url_id=url_id)
        h1 = result.h1
        return render_to_response('details.html',
                              {'url': site.url,
                               'code': str(result.status_code),
                               'title': result.title,
                               'charset': result.charset,
                               'date': result.date.strftime("%d.%m.%y %H:%M:%S"),
                               'h1': h1.split(';;') if h1 else '',
                               'error_reason': result.error_reason })
    except:
        return render_to_response('not_found.html')
