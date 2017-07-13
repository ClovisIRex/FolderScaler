from setuptools import  setup


setup(
    name='Fscaler',
    version= '1.0',
    py_modules=['fscaler/scaler/scaler'],
    install_requires=[
        'Click', 'scandir',
    ],
    entry_points='''
        cons
    '''
)