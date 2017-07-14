from setuptools import setup

with open('miio/version.py') as f: exec(f.read())

setup(
    name='python2-miio',

    version=__version__,
    description='Python2 library for interfacing with Xiaomi miio components',
    url='https://github.com/wzpan/python2-miio',

    author='Joseph Pan',
    author_email='m@hahack.com',

    license='GPLv3',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
    ],

    keywords='xiaomi miio',

    packages=["miio"],

    install_requires=['construct', 'click', 'cryptography', 'pretty_cron'],
    entry_points={
        'console_scripts': [
            'miio2=miio.cli:cli',
        ],
    },
)
