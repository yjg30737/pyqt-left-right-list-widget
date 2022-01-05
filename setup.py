from setuptools import setup, find_packages

setup(
    name='pyqt-left-right-list-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QListWidget which can add QListWidgetItem consist of two words.'
                'One word is left-aligned, the other is right-aligned.',
    url='https://github.com/yjg30737/pyqt-left-right-list-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)