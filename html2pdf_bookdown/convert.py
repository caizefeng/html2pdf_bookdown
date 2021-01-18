#!/usr/bin/env python3
# @File    : convert.py
# @Time    : 1/14/2021 2:22 PM
# @Author  : Zavier Cai
# @Email   : caizefeng18@gmail.com
import base64
import os
import time

from PyPDF2 import PdfFileReader, PdfFileMerger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm


def print_to_pdf(contents_list, book_name, time_wait=2, separated_suffix='PDFs'):
    separated_dir_name = "_".join((book_name, separated_suffix))
    os.makedirs(separated_dir_name, exist_ok=True)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)

    print("Fetching and printing separated PDFs:")
    for section in tqdm(contents_list):
        driver.get(section["url"])
        time.sleep(time_wait)
        pdf = driver.execute_cdp_cmd("Page.printToPDF", {
            "displayHeaderFooter": False,
            "printBackground": True,
            # "paperWidth": 8.27,  # A4
            # "paperHeight": 11.69,  # A4
        })

        single_pdf_path = os.path.join(separated_dir_name, "{}.pdf".format(section["name"].replace('/', '+')))
        section["single_pdf_path"] = single_pdf_path
        with open(single_pdf_path, "wb+") as f:
            f.write(base64.b64decode(pdf['data']))
            page_num = PdfFileReader(f).getNumPages()
            section["page_num"] = page_num

    driver.quit()
    return contents_list


def merge_and_bookmark(contents_list, book_name):
    pdfmerger = PdfFileMerger()
    page_idx = 0
    last_level = -1
    level_list = [pdfmerger.addBookmark(book_name, page_idx)]  # Like a depth meter
    print("Merging and bookmarking PDFs:")
    for section in tqdm(contents_list):
        for _ in range(last_level - section["level"] + 1):
            level_list.pop()
        parent = level_list[-1]
        level_list.append(pdfmerger.addBookmark(section["name"], page_idx, parent))
        pdfmerger.append(open(section["single_pdf_path"], 'rb'))

        page_idx += section["page_num"]
        last_level = section["level"]

    with open("{}.pdf".format(book_name), 'wb') as f_output:
        pdfmerger.write(f_output)
