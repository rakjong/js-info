import sys
from urllib.parse import urlparse
from urllib.request import urlopen

from lxml import etree
url = sys.argv[1]
baseurl = url[:url.rfind("/")]
content = urlopen(url).read()
html = etree.HTML(content)
# fetch script src
srcs = html.xpath('//script/@src')
# fetch script body
script_body = html.xpath('//script/text()')
for body in script_body:
	f1=open('js-body.txt','w')
	f1.write(body)
    #print('<script>'+body+'</script>')
	f1.close()

f2=open('js-url.txt','w')
for src in srcs:
	
	if urlparse(src).netloc == '':
		#print("{}/{}".format(baseurl, src))
		f2.write("{}/{}".format(baseurl, src)+'\n')

	else:
		f2.write(src+'\n')
		#print(src)
f2.close()
