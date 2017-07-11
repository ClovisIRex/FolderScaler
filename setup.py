from setuptools import  setup


setup(
    name='FolderScaler',
    version= '1.0',
    py_modules=['folderscaler/scaler/scaler'],
    install_requires=[
        'Click', 'scandir',
    ],
    entry_points='''
        cons
    '''
)