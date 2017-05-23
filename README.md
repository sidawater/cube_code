# cube_code

### pip包管理
```
sudo apt install python3-pip
sudo apt install python-pip
```

### 虚拟环境
```
sudo pip3 install virtualenv
sudo pip install virtualenvwrapper
```

 编辑 ~/.bashrc 文件, 添加以下语句:
```
# virtualenv
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh
export WORKON_HOME=$HOME/.virtualenvs
```
 新建虚拟环境virtualcube
```
 mkvirtualenv --python=`which python3` virtualcube
 workon virtualcube
```
项目下运行
```
pip3 install docker/python/python.txt
```
