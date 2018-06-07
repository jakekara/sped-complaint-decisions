from dllinks import get_urls, download_urls

urls = [
    "http://portal.ct.gov/SDE/Special-Education/Special-Education-Hearing-Decisions/2018",
    "http://portal.ct.gov/SDE/Special-Education/Special-Education-Hearing-Decisions/2017",
    "http://portal.ct.gov/SDE/Special-Education/Special-Education-Hearing-Decisions/2016",
    "http://portal.ct.gov/SDE/Special-Education/Special-Education-Hearing-Decisions/2014-2015",
    "http://portal.ct.gov/SDE/Special-Education/Special-Education-Hearing-Decisions/2012-2013",
    "http://portal.ct.gov/SDE/Special-Education/Special-Education-Hearing-Decisions/2010-2011",
    "http://portal.ct.gov/SDE/Special-Education/Special-Education-Hearing-Decisions/2009-1998"
]

pdf_dir = "pdf"

for url in urls:
    print ("Downloading PDFs from " + str(url))
    pdf_urls = get_urls(url)
    download_urls(pdf_urls, dst=pdf_dir, base_url=url)
