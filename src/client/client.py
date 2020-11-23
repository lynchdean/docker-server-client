from urllib.request import urlopen

link = "http://host.docker.internal:5000/"
f = urlopen(link)
myfile = f.read()
print(myfile)
