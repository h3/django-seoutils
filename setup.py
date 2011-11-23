# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='SEOUtils',
    version='1.0.0',
    description='Django SEO Utils.',
    author='Maxime Haineault (Motion Média)',
    author_email='max@motion-m.ca',
    url='',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
#   package_data={'seoutils': [
#       'templates/*',
#       ]},
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
