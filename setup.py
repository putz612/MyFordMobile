from setuptools import setup

setup(
    name='myfordmobile',
    version='0.0.1',
    description='Python 3 API for myfordmobile.com.',
    url='https://github.com/putz612/MyFordMobile/',
    license='MIT',
    author='Jason Sievert',
    author_email='jsievert@gmail.com',
    packages=['myfordmobile'],
    install_requires=['beautifulsoup4==4.5.1', 'requests>=2.20.0'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
