#Check the meta tag using bs4 or requests to get the date and articel and publisher name 
import webget
import mkcite
def CiteSelect():
    infdict = webget.parseinfo("https://www.thestack.technology/microsofts-new-ai-pcs-will-screenshot-everything-every-2-seconds/")
    print(infdict)
    print("Select a format (MLA,APA)")
    format = input("ENTER FORTMAT|:| ")
    if format.startswith("a") or format.startswith("A"):
        print("Run the APA function")
        mkcite.apa(infdict)
    else:
        print("Run the MLA function")


if __name__ == '__main__':
    print("DONT RUN ME")
    CiteSelect()
