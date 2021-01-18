import setuptools


def get_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


def get_required_packages():
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()


setuptools.setup(
    name='html2pdf_bookdown',
    version='0.1.0',
    description='Fetch and convert HTML to PDF for eBooks published with Bookdown',
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    author='Zavier Cai',
    author_email='caizefeng18@gmail.com',
    url='https://github.com/caizefeng/html2pdf_bookdown',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    keywords='html pdf conversion bookdown',
    # project_urls={
    #     'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
    # },
    packages=setuptools.find_packages(),
    install_requires=get_required_packages(),
    python_requires='>=3.6',
    # package_data={
    #     'html2pdf_bookdown': ['data/*'],
    # },
    # data_files=[('my_data', ['html2pdf_bookdown/data/2'])],
    entry_points={
        'console_scripts': [
            'html2pdf_bookdown=html2pdf_bookdown.__main__:main',
        ],
    },
)
