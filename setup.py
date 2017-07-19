from setuptools import setup, find_packages


setup(
    name='Fscaler',
    version= '1.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['fscaler/scaler/scaler'],
    install_requires=[
        'Click', 'scandir',
    ],
    entry_points='''
        [console_scripts]
        fscaler=fscaler.cli:cli
    '''
)
