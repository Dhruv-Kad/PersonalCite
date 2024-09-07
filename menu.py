#Check the meta tag using bs4 or requests to get the date and articel and publisher name 
import webget
import mkcite
def CiteSelect():
    usedurl = input("Enter the url below \n")
    infdict = webget.parseinfo(usedurl)
    print(infdict)
    print("Select a format (MLA,APA)")
    format = input("ENTER FORTMAT|:| ")
    if format.startswith("a") or format.startswith("A"):
        print("Run the APA function")
        mkcite.apa(infdict)
    else:
        mkcite.mla(infdict)

if __name__ == '__main__':
    print("DONT RUN ME")
    CiteSelect()
