import urllib.request


url1=""
url2=""
url3=""



urllist={url1,url2,url3}
const=1

for url in urllist:
    urllib.request.urlretrieve(url,"picture"+ str(const)+"jpg") # burda dosya turunu girmemiz gerekıyor yoksa acılmaz.
    const+=1

