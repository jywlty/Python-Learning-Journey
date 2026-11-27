import os
file=input()
f=open(os.path.abspath(file),"r",encoding='utf-8')
t=f.read()
t=t.replace("\n",",")
libs=t.split(",")
f.close()
try:
    for lib in libs:
        os.system("pip install "+lib)
except SyntaxError:
    print("文件编译失败")
except ImportError:
    print("找不到模块")
except FileNotFoundError:
    print("系统找不到cmd.exe或pip可执行文件、路径非法")
except PermissionError:
    print("无权限写系统目录、无权限启动进程")
except UnicodeEncodeError:
    print('中文路径、中文用户名,cmd编码GBK与UTF-8冲突')
else:
    print("Successful")
finally:
    print("程序结束")

