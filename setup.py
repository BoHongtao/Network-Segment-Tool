# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/8/27 9:32
from setuptools import setup, find_packages

setup(
    name = 'baseip',
    version = '0.0.1',
    description = 'deal ip',
    license = 'MIT License',
    install_requires = [],
    packages = ['baseip'],  # 要打包的项目文件夹
    include_package_data=True,   # 自动打包文件夹内所有数据
    author = 'bohongtao',
    author_email = 'BoHongtao@yeah.net',
    url = 'https://github.com/bohongtao',
)