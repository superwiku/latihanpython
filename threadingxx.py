import urllib2
import threading

def get_content_len(url):
	response = urllib2.urlopen(url)
	content = response.read()
	print len(content)

urls = [
	"http://www.srikandiart.com", 
	"http://www.srikandiart.com/digital/spanduk.html",
	"http://www.srikandiart.com/digital/sticker.html",
	"http://www.srikandiart.com/digital/standingbanner.html",
	"http://www.srikandiart.com/digital/kain.html"
]

for url in urls:
	t = threading.Thread(target=get_content_len, args=(url,))
	t.start()

print "Mengambil panjang halaman web sudah selesai..."