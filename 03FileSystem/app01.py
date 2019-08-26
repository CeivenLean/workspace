import os


# s = os.getcwd()
# print(s)

# 将文件路径分解成：　目录，文件名(带.后缀)
# fpath , fname = os.path.split( "/Users/xxxl/VSProjects/workspace/03FileSystem/app01.py")

# 分解成　目录文件名, .后缀
# fpathandname , fext = os.path.splitext( "/Users/xxxl/VSProjects/workspace/03FileSystem/app01.py")
# print(fpathandname, fext)


# 判断一个路径（ 文件夹或文件）是否存在
# boo = os.path.exists( "你要判断的路径")


# 判断一个路径是否是文件
# boo = os.path.isfile( "你要判断的路径")

# 判断一个路径是否是文件夹
# boo = os.path.isdir( "你要判断的路径")

# 获取某目录中的文件及子目录的名字列表
p = "/Users/xxxl/VSProjects/workspace"
files = os.listdir(p)

# 过滤掉文件
filesname = [ x for x in files if os.path.isdir( p + x ) ]
# 过滤掉文件夹
filename = [ x for x in files if os.path.isfile( p + x ) ]



# 创建目录
os.makedirs("绝对路径")


os.rmdir( 'path' )
os.remove(   'filename' )
os.name( 'oldfileName', 'newFilename')



if __name__ == "__main__":
    print(os.getcwd())  # /Users/xxxl/VSProjects/workspace

    path1=os.path.abspath('.')   #表示当前所处的文件夹的绝对路径
    path2=os.path.abspath('..')
    print(path1)  # /Users/xxxl/VSProjects/workspace
    print(path2)  # /Users/xxxl/VSProjects
    d = os.path.dirname(__file__)
    print(d)  # /Users/xxxl/VSProjects/workspace/02excel
    d2 = os.path.abspath(__file__)
    print(d2)  # /Users/xxxl/VSProjects/workspace/02excel/findindex.py
