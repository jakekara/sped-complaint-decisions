#!/usr/bin/env python2

""" Download all PDF links to directory """

import requests
from bs4 import BeautifulSoup
from os.path import basename, split, exists, join
from os import makedirs
from sys import argv
from urlparse import urljoin

def get_html(url):

    return requests.get(url).content

def get_soup(url):
    return BeautifulSoup(get_html(url),"html.parser")

def get_urls(url, extension="PDF", max_title=100):

    soup = get_soup(url)

    links = soup.find_all("a",href=True)

    tups = []

    for l in links:
        lupper = l["href"].upper()
        if not lupper.endswith(extension.upper()): continue

        tups.append((l["href"], basename(l["href"])))

    return tups

def sanitize_filename(fstr):

    return fstr.replace("/",".")

def mkdir(dst):

    if exists(dst): return

    makedirs(dst)

def download_urls(tups, dst="DOWNLOADS", base_url=""):

    mkdir(dst)

    for tup in tups:
        url, fname = tup
        # url = base_url + url
        url = urljoin(base_url, url)
        print url, fname
        open(join(dst, fname), "wb").write(requests.get(url).content)
    
    return
