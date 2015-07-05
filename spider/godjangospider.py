#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import requests
from bs4 import BeautifulSoup as Soup


session = requests.Session()
url_list = []
video_list = []
base = 'https://godjango.com'


def login(username, password):
    url = 'https://godjango.com/accounts/login/'
    r = session.get(url)
    soup = Soup(r.text, "html.parser")
    form = soup.find('form', class_='form-horizontal')
    token = form.select('input[type="hidden"]')[0].get('value')
    data = {'username': username,
            'password': password,
            'csrfmiddlewaretoken': token}
    r = session.post(url, data=data)
    if r.status_code == requests.codes.ok:
        print('Login succeed!')
        return True
    else:
        print(r.text)
        return False


def list_url(page):
    if type(page) is int:
        return 'https://godjango.com/browse/?page=%d' % page
    else:
        return 'https://godjango.com/browse/' + page


def get_list(page):
    if not page:
        return None
    url = list_url(page)
    r = session.get(url)
    soup = Soup(r.text, "html.parser")
    page_links = soup.select('h4.media-heading a')
    for page_link in page_links:
        url_list.append(base + page_link.get('href'))
    next_page = soup.select('ul.pagination a')[-1]
    if next_page.string == 'Next':
        print('we have next page for download')
        return next_page.get('href')
    else:
        return None


def get_page(page_url):
    r = session.get(page_url)
    soup = Soup(r.text, "html.parser")
    url = base+soup.select_one("div.video-meta a").get('href')
    video_list.append(url)
    print(url)


def main():
    parser = argparse.ArgumentParser(description='GoDjango Spider')
    parser.add_argument('-u', '--username', help='GoDjango username')
    parser.add_argument('-p', '--password', help='GoDjango password')
    parser.add_argument('-f', '--file', help='Output file name')
    args = parser.parse_args()
    if not (args.username and args.password):
        print('GoDjango Spider. ')
        print('Please use "godjangospider.py -h" to get more information.')
        return
    # Login User
    if not login(args.username, args.password):
        print('Username or Password is incorrect')
        return
    # Get Video List
    current_page = 1
    while True:
        if current_page:
            current_page = get_list(current_page)
        else:
            break
    # Get video download link list
    print('Start get video file link')
    for url in url_list:
        get_page(url)

    # Write video donwload link to file
    file_name = args.file if args.file else 'godjango_download.txt'
    with open(file_name, 'w+') as f:
        for video in video_list:
            f.write(video+'\n')


if __name__ == '__main__':
    main()
