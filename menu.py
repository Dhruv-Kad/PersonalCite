#Check the meta tag using bs4 or requests to get the date and articel and publisher name 

def CiteSelect():
    print("Select a format (MLA,APA)")
    format = input("ENTER FORTMAT|:| ")
    if format.startswith("a") or format.startswith("A"):
        print("APA")
    else:
        print("MLA")


if __name__ == '__main__':
    print("DONT RUN ME")
    CiteSelect()
