#!/usr/bin/env python3
# @File    : fetch.py
# @Time    : 1/14/2021 2:21 PM
# @Author  : Zavier Cai
# @Email   : caizefeng18@gmail.com
import os
import re

import requests
from bs4 import BeautifulSoup


def get_chapter_level(chapter, root_node):
    li_tag = chapter.parent
    parent_count = 0
    for parent in li_tag.parents:
        if parent.name == 'li':
            if parent['class'] == ['chapter']:
                parent_count += 1
        elif parent == root_node:
            return parent_count


def parse_contents(URL):
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'lxml')
    contents_tag = soup.find('ul', {"class": "summary"})
    contents_list = []
    chapters_list = contents_tag.find_all('a', {"href": re.compile(r'^((?!#).)*\.html$')})  # select url without anchors

    root_node = contents_tag
    for chapter in chapters_list:
        level = get_chapter_level(chapter, root_node)
        contents_list.append({"name": chapter.get_text(),
                              "url": os.path.join(URL, chapter["href"]),
                              "level": level,
                              })

    return contents_list
