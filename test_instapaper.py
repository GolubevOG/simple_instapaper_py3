import instapaper
#import mydata
import config

def main():
    username = config.user
    password = config.password
    url = config.url
    instapaper.add_urls(username,password,url)

if __name__ == '__main__':
    main()
