
from datetime import date

def apa(totaldictl):
    apaneedlist = ["SiteName", "SiteUrl", "ArticleTitle", "ArticlePublisherLocal", "ArticleAuthor", 'ArticlePublishedTime']
    apadict = {}
    dellist = []

    for tkey in totaldictl:
        for i in apaneedlist:
            if(tkey == i):
                apadict[i] = totaldictl[tkey]
    if((apadict["ArticlePublishedTime"].startswith("*N")) != True):
        ndate = apadict["ArticlePublishedTime"]
        print(ndate)
        fdate = ""
        for z in ndate:
            if(z == "-"):
                break
            fdate += z
        apadict["ArticlePublishedTime"] = fdate
    for x in apadict:
        if (apadict[x].startswith("*N")):
            o = input("If you know the " + x + " enter !, otherwise enter NO: ")
            if("!" in o):
                apadict[x] = input("Enter the value here: ")
            else:
                apadict[x] = "" 
    
    print(apadict["SiteName"] + ".(" + apadict["ArticlePublishedTime"] + ")." + apadict["ArticleTitle"] + " " + apadict["ArticleAuthor"] + ", " + apadict["SiteUrl"])

def mla(totaldictl):
    mlaneedlist = ["ArticleAuthor", "ArticleTitle", "SiteName", "ArticlePublisher", "ArticlePublishedTime", "SiteUrl", "AccessDate", "ArticlePublisherLocal"]
    mladict = {}
    for tkey in totaldictl:
        for i in mlaneedlist:
            if(tkey == i):
                mladict[i] = totaldictl[tkey]
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    mladict["AccessDate"] = d2 
    print(mladict)
    
    if((mladict["ArticlePublishedTime"].startswith("*N")) != True):
        mdate = mladict["ArticlePublishedTime"]
        print(mdate)
        fdate = ""
        for z in mdate:
            if(z == "-"):
                break
            fdate += z
        mladict["ArticlePublishedTime"] = fdate
    for m in mladict:
        if(mladict[m].startswith("*N")):
            o = input("If you know the " + m + " enter it, otherwise enter !: ")
            if("!" in o):
                mladict[m] = "" 
            else:
                mladict[m] = o
    print(mladict["ArticleAuthor"] + ". " + mladict["ArticleTitle"] + ",(" + mladict["ArticlePublishedTime"] + ")," + mladict["ArticlePublisher"] + "," + mladict["ArticlePublisherLocal"] + ", " + mladict["SiteUrl"] + ". " + mladict["AccessDate"])
