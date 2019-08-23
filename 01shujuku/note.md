一、MS Sql Server

# pip install pymssql

import pymssql

注：mac系统直接用pip会出错
解决：
    1）替换brew.git:
    cd "$(brew --repo)"
    git remote set-url origin https://mirrors.ustc.edu.cn/brew.git

    替换homebrew-core.git:
    cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
    git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git 
    重置brew.git:
    cd "$(brew --repo)"
    git remote set-url origin https://github.com/Homebrew/brew.git

    重置homebrew-core.git:
    cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
    git remote set-url origin https://github.com/Homebrew/homebrew-core.git

    2）使用homebrew先安装freetds 0.91版本：
        brew unlink freetds 
        brew install freetds@0.91 
        brew link --force freetds@0.91 
    3)  pip3 install pymssql

 

二、Oracle

# pip install cy-Oracle

import cx_Oracle

 

三、MySQl

# pip install mysql-connector-python

import mysql-connector