#!/usr/bin/env python3
# @File    : github_book.py
# @Time    : 1/12/2021 11:18 AM
# @Author  : Zavier Cai
# @Email   : caizefeng18@gmail.com
import argparse

from html2pdf_bookdown.convert import print_to_pdf, merge_and_bookmark
from html2pdf_bookdown.fetch import parse_contents


def main():
    parser = argparse.ArgumentParser(description="Fetch and convert HTML to PDF for eBooks published with Bookdown")
    parser.add_argument("-u", "--url", default="https://christophm.github.io/interpretable-ml-book")
    parser.add_argument("-n", "--book_name", default="Interpretable-Machine-Learning")
    args = parser.parse_args()

    contents_list = parse_contents(args.url)
    contents_list_modified = print_to_pdf(contents_list, args.book_name)
    merge_and_bookmark(contents_list_modified, args.book_name)


if __name__ == '__main__':
    main()
