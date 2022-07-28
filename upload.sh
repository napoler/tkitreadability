#!/bin/bash
#这里是一个自动执行上传的命令

# 安装依赖查找库
pip install pipreqs
pip install twine
#遇到已经存在 强制覆盖 requirements.txt
# pipreqs ./ --force

rm -rf dist
#打包
python3 setup.py sdist
python setup.py bdist_wheel --universal # 打包为无需build的wheel。其中--universal表示py2和py3通用的pure python模块。不满足通用或pure条件的模块不需加此参数
#python3 setup.py install
#上传
# python3 setup.py sdist upload
twine upload dist/*
