
import urllib.request,re

def get_html(city,year,month):
    url='https://.tianqi.com/lishi/%s/%s%s.html' % (city,year,month)
    request = urllib.request.Request(url)
    request.add_header('User-Agent','Mozilla/5.0')
    return urllib.request.urlopen(request).read().decode('UTF-8')

print(get_html("guangzhou",'2018','01'))
