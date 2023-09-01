import webbrowser
favourites = {
    "Google": "https://www.google.com/",
    "facebook": "https://www.facebook.com/",
    "youtube" : "https://www.youtube.com/"
}
def firefox(url):
    webbrowser.register('firefox',None,webbrowser.GenericBrowser('firefox'))
    webbrowser.get('firefox').open(url)

if __name__ == "__main__":
    print("welcome to favourite websites")
    print("available websites: ")
    for i in favourites :
        print("-",i)
    website_choice = input("enter the name of website you want ")
    if website_choice in favourites:
        url = favourites[website_choice]
        firefox(url)
    else:
        print("it is not in your favourites")



    
