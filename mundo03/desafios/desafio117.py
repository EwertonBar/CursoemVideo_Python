import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro.')
else:
    print('Ok')
    print(site.read())