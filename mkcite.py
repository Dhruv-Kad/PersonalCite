def apa(totaldictl):
    apaneedlist = ["SiteName", "SiteUrl", "ArticleTitle", "ArticlePublisherLocal", "ArticleAuthor", 'ArticlePublishedTime']
    apadict = {}
    dellist = []
    for tkey in totaldictl:
        for i in apaneedlist:
            if(tkey == i):
                apadict[i] = totaldictl[tkey]
    for x in apadict:
        if (apadict[x].startswith("*N")):
            o = input("If you know the " + x + " enter !, otherwise enter NO: ")
            if("!" in o):
                apadict[x] = input("Enter the value here: ")
            else:
                dellist.append(x)
    for delitem in dellist:
        apadict[delitem] = ""
    print(apadict["SiteName"] + "." + apadict["ArticlePublishedTime"] + "." + apadict["ArticleTitle"] + " " + apadict["ArticleAuthor"] + ", " + apadict["SiteUrl"])
