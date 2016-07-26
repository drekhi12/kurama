import cookielib
import urllib2
import mechanize

br = mechanize.Browser()
cookiejar = cookielib.LWPCookieJar()
br.set_cookiejar(cookiejar)
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' ) ]

user = "username"
passw = "password"
url = "https://www.facebook.com/login.php"

br.open(url)
br.select_form(nr=0)
br.form['email'] = user
br.form['pass'] = passw
response = br.submit()

fileobj = open("HTML-OUTPUT.txt","wb")
fileobj.write(response.read())
fileobj.close()
