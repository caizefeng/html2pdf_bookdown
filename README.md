# html2pdf_bookdown
Fetch and convert HTML to PDF for eBooks published with **Bookdown**

## Usage
```
html2pdf_bookdown [-h] [-u URL] [-n BOOK_NAME]
```
E.g. 
```
html2pdf_bookdown -u https://christophm.github.io/interpretable-ml-book -n Interpretable-Machine-Learning-by-Christoph-Molnar
```
will generate a combined PDF named `Interpretable-Machine-Learning-by-Christoph-Molnar.pdf` and a directory containing
several PDFs, one for each chapter.

## Installation
1. Make sure **Google Chrome** has been installed and the corresponding **ChromeDriver** (needed by **Selenium**, can be downloaded 
from [this website](https://sites.google.com/a/chromium.org/chromedriver/downloads)) is in your *PATH*.

2. Then using `pip`
```
pip install html2pdf_bookdown
```
