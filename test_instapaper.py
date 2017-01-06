import instapaper

def main():
    username = 'testName'
    password = 'testPassword'
    url = 'https://ru.wikipedia.org/wiki/%D0%9B%D0%B0%D1%82%D0%B2%D0%B8%D1%8F_%D0%BD%D0%B0_%C2%AB%D0%95%D0%B2%D1%80%D0%BE%D0%B2%D0%B8%D0%B4%D0%B5%D0%BD%D0%B8%D0%B8-2009%C2%BB'
    instapaper.authenticate(username,password)
    instapaper.add_urls(username,password,url)

if __name__ == '__main__':
    main()
