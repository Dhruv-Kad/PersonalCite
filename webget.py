# This is the part that should get information from the web so that the user has a more streamlined experince
from bs4 import  BeautifulSoup
import requests
infolist = ["SiteName", "ArticleTitle", "ArticlePublishedTime", "ArticlePublisher", "ArticleAuthor"]
infodict = {}

# Uses BeautifulSoup to scrape a site for info then formats the info into a prettifier
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
#Prettifier gets ride of html tags and reduces down to the strings we need
def prettify(uglydict):
    pretdict ={}
    for i in uglydict:
        uglyval = str(uglydict[i])
        binaryno = 0
        print(i + " is " + uglyval)
        prettyval = ""
        for q in uglyval:
            if(q == '"'):
                binaryno+=1
                if(binaryno == 2):
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
    #takes the found info and stores it
    for x in foundinfo:
        val = foundinfo[x]
        allreqdict[allreqs[y]] = val
        y += 1
    while(int(len(allreqs)) - y > 0):
        allreqdict[allreqs[y]] = "*NFound"
        y += 1
    print("FINAL DICT AHHHHH")
    return(allreqdict)
if __name__ == '__main__':
    print(parseinfo('https://www.thestack.technology/microsofts-new-ai-pcs-will-screenshot-everything-every-2-seconds/'))
