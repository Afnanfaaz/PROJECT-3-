from distutils.core import setup

setup(
    name='airtraffic_analysis',
    version='0.2.1',
    description='Classes for technical analysis of airtraffic dataset.',
    author='Afnan',
    author_email='',
    license='MIT',
    url='',
    packages=['airtraffic_analysis'],
    install_requires=[
        'matplotlib>=3.0.2',
        'numpy>=1.15.2',
        'pandas>=0.23.4',
        'pandas-datareader>=0.7.0',
        'seaborn>=0.11.0',
        'statsmodels>=0.11.1',
    ],
)