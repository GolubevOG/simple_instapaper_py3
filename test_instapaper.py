import instapaper

def main():
    username = 'testName'
    password = 'testPassword'
    instapaper.authenticate(username,password)
    instapaper.add_urls(username,password,'https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D0%BA%D0%BE%D0%B2%D0%B8%D1%87,_%D0%9C%D0%B8%D0%BB%D0%BB%D0%B5')

if __name__ == '__main__':
    main()
