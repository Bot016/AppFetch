import requests
from bs4 import BeautifulSoup

def response_get_html(url):
        response = requests.get(url)
        if response.status_code == 200:
            html = BeautifulSoup(response.content, 'html.parser')
            return html

class links():
    def Chrome():
        return "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BE5E20456-3691-AB08-C7F9-DDF68794A713%7D%26lang%3Dpt-BR%26browser%3D5%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe"
    
    def Firefox():
        url = "https://download-installer.cdn.mozilla.net/pub/firefox/releases/"
        html = response_get_html(url)
        if html:
            links = html.find_all('a', href=True)
            final_version = [link for link in links if link['href'].endswith('.0.1/')]
            if final_version:
                final_version.sort(key=lambda link: int(''.join(filter(str.isdigit, link['href'].split('/')[-2]))), reverse=True)
                latest_version = final_version[0]
                latest_version = latest_version['href']
                url = '/'.join(url.split('/', 3)[:3]) + latest_version + "win32/pt-PT/Firefox%20Installer.exe"
                return url
              
    def zip():
        url = "https://www.7-zip.org/download.html"
        html = response_get_html(url)
        if html:
            link = html.find_all('a', string="Download", href=lambda href: href and 'x64.exe' in href)
            url = '/'.join(url.split('/', 3)[:3]) + "/" + link[0].get('href')
            return url

    def Winrar():
        url = "https://www.win-rar.com/download.html"
        html = response_get_html(url)
        if html:
            link = html.find_all('a', href=True, string=lambda string: string and 'Portuguese Brazilian 64 bit' in string)
            url = link[0].get("href")
            return url
        
    def Thunderbird():
        url = "https://www.thunderbird.net/pt-BR/"
        html = response_get_html(url)
        if html:
            link = html.select_one('.download-link')
            url =link.get("href")
            return url

    def Antivírus():
        url = "https://raw.githubusercontent.com/Bot016/AppFetch/main/files/Ainvirus-Kasperski.exe"
        return url

    def Small_Office():
        url = "https://raw.githubusercontent.com/Bot016/AppFetch/main/files/smalloffice.exe"
        return url
    
    def Anydesk():
        url = 'https://download.anydesk.com/AnyDesk.exe'
        return url

    def CCleaner():
        print("CClenare")
    
    def Java_8():
        print("Java_8")

links.Antivírus()