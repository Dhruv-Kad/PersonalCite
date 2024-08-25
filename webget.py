# This is the part that should get information from the web so that the user has a more streamlined experince
from bs4 import  BeautifulSoup
import requests
infolist = ["SiteName", "ArticleTitle", "ArticlePublishedTime", "ArticlePublisher", "ArticleAuthor"]
infodict = {}
#probably going to need to come up with some redanduancy for all the different ways that metadata can be associated
#never mind
def getinfo(url):
    matchtable = ["og:site_name", "og:title", "article:published_time", "article:publisher", "article:author"]
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    inflist_counter = 0
    for i in matchtable:
        match1 = soup.find('meta', property= (i))
        infodict[infolist[inflist_counter]] = match1
        inflist_counter += 1
    print(infodict)
    return(prettify(infodict))

def prettify(uglydict):
    pretdict ={}
    for i in uglydict:
        nonefs = False
        if(uglydict[i] is None):
            nonefs = True
        uglyval = str(uglydict[i])
        binaryno = 0
        print(i + " is " + uglyval)
        prettyval = ""
        for q in uglyval:
            if(q == '"'):
                binaryno+=1
                if(binaryno == 2):
                    if(nonefs == True):
                        prettyval == "UIN"
                    pretdict[i] = prettyval
                    prettyval = ""
                    break
            if(binaryno%2  == 1 ):
                prettyval += q 
    return pretdict 
    

def parseinfo(url): 
        #Make a list with the key parts of a citation formatted pretty
    allreqs = [
            "SiteName",
            "ArticleTitle",
            "ArticlePublishedTime",
            "ArticlePublisher",
            "ArticleAuthor",
            "SiteUrl" ,
            "AccessDate",
            "Other contributers"
    ]

    foundinfo = getinfo(url)
    y=0
    allreqdict = {}
    for x in foundinfo:
        val = foundinfo[x]
        allreqdict[allreqs[y]] = val
        y += 1 
    print(allreqdict)

if __name__ == '__main__':
    print(parseinfo('https://www.thestack.technology/microsofts-new-ai-pcs-will-screenshot-everything-every-2-seconds/'))
