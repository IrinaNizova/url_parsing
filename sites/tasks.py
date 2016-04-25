from celery.decorators import task
import urllib.request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from result.models import DataFromUrl

@task()
def handling_url(id, url):
    try:
        page = urllib.request.urlopen(url)
        code = page.getcode()
        site = page.read().decode('utf-8')
        tree = BeautifulSoup(site, fromEncoding='utf-8')

        charset = [tag['charset'] for tag in tree.findAll('meta') if 'charset' in tag.attrs]
        if charset:
            charset = charset[0]
        else:
            for tag in tree.findAll('meta'):
                if 'content' in tag.attrs:
                    if 'charset' in tag['content']:
                        charset = [s.split('=') for s in tag['content'].split(';')
                                   if 'charset' in s][0][1]

        h1 = ";;".join([h.contents[0] for h in tree.findAll('h1')])
        d = DataFromUrl(url_id=id, status_code=code, title=str(tree.head.title.string),
                        charset=charset, h1=h1)
        d.save()
    except HTTPError as err:
        d = DataFromUrl(url_id=id, status_code=err.code, error_reason=err.reason)
        d.save()
    except URLError as err:
        d = DataFromUrl(url_id=id, status_code=-1, error_reason=err.reason)
        d.save()
