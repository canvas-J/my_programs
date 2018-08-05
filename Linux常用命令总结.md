Linux常用命令

文件和目录

tree
        以树状形式显示当前文件和目录
        需要安装该软件:sudo yum -y install tree(centos下)

ls
        查看指定目录下所有文件和目录信息
        -a(all) -- 列出当前目录下所有文件内容
        -R(recursive) -- 同时列出所有子目录层
        -l --除了文件名之外,还将文件的权限,所有者,文件大小等信息详细列出来

cd
        进入指定目录(cd + path)
        相对路径 -> cd ./robertohuang/tomcat
        绝对路径 -> cd /home/robertohuang/tomcat
        .. -> 当前目录的上一级
        . -> 当前目录
        进入家目录(/home/robertohuang)三种方式

cd 
        cd ~
        cd /home/robertohuang

pwd
        查看当前所在目录(printf working directory的缩写)

创建/删除目录

创建:mkdir + 目录名

        mkdir world -> 创建world目录
        mkdir -p world/a/b -> 创建多级目录加参数-p

删除:rmdir + 目录名

        只能删除空目录,使用频率不高

创建/删除文件
        创建:touch + 文件名

cp

拷贝文件
        cp file1.txt file2.txt -> 将file1.txt中的内容拷贝到file2.txt
        文件不存在创建文件
        文件存在,覆盖原文件

拷贝目录
        cp -r dir1 dir2 -> 将目录dir1中的内容拷贝到dir2中
        dir2 目录不存在创建目录

scp命令
        scp:super copy的缩写
        使用该命令的前提条件
        目标主机已经成功安装openssh-server

        使用格式

        scp -r 目标用户名@目标主机IP地址:/目标文件的绝对路径 /保存到本机的绝对（相对）路径
        在后续会提示输入yes此时,只能输"yes"而不能简单输入"Y"
        scp -r 目标用户名@目标主机IP地址:/目标文件的绝对路径 /保存到本机的绝对/相对路径
        scp -r usertest@192.168.29.128:/home/usertest/test /home/robertohuang/test
        拷贝目录需要加参数 -r

查看文件内容

        cat
        cat file.txt -> 将文件内容一次性输出到终端,如果文件太长,无法再终端全部显示
        more
        more + 文件名
        文件内容分页显示到终端,但是只能一直向下浏览,不能回退

相关操作
        回车:显示下一行
        空格:显示下一页
        ctrl+c 或 q:退出

less
        less + 文件名
        文件内容分页显示到终端,可以自由上下浏览
        相关操作
        回车:显示下一行
        空格:显示下一页
        ctrl+p 或 ↑:滚动到上一行
        ctrl+n 或 ↓:滚动到下一行
        q:退出

head
        从文件头部开始查看前x行的内容
        head -5 hello.c --> 查看hello.c文件前五行的内容
        如果没有指定行数,默认显示前10行内容

tail
        从文件尾部开始查看后x行的内容
        tail -5 hello.c --> 查看hello.c文件后五行的内容
        如果没有指定行数,默认显示后10行内容

ln
        软连接(符号链接)
        相当于windows下快捷方式
        注意事项
        创建软链接,源文件要使用绝对路径
        软连接大小:源文件+路径 的总字节数
        目录可以创建软链接
        示例:ln -s /home/robertohuang/a.txt（源文件名+绝对路径） a.test（软链接的名字）

硬链接
        注意事项
        以文件副本的形式存在,但不占用实际空间
        不允许给目录创建硬链接
        硬链接只有在同一个文件系统中才能创建
        硬链接能够同步更新
        linux下每一个文件都对应一个Inode,创建硬链接后两个文件的Inode是相同的
        查看文件的Inode:stat a.txt
        文件创建硬链接后,硬链接计数+1,删除一个硬链接,硬链接计数-1

文件或目录属性

wc
        查看文件的字数、字节数、行数
        wc a.txt
                行数  字数  字节数  文件名
        结果：7      23      120      a.txt
        参数
        -c:只显示字节数
        -l:只显示行数
        -w:只显示字数

od
        查看二进制文件信息

du
        查看某个目录的大小(disk use的缩写)

df
        查看磁盘的使用情况(disk free的缩写)
        一般加参数 -h(human)以人类能看懂的方式显示 
        (du, df)

which
        查看指定命令所在的路径
        which指令会在PATH变量指定的路径中,搜索某个系统命令的位置,并且返回第一个搜索结果

删除:rm
        (创建/删除目录, 创建/删除文件)
        删除文件:rm file1.txt
        删除目录:rm -r dir 递归删除
        rm删除的文件或目录是不易恢复的,数据不会放入回收站中
        相关参数
        -i -> 提示用户是否需要删除目录或文件
        -f -> 强制删除,使用rm命令的时候默认已经添加了-f参数

文件权限,用户,用户组

whoami
        查看当前登录用户

chmod
        修改文件访问权限(change mod的缩写)
        修改方式
        文字设定法
        chmod [who] [+|-|=] [mode] 文件名
        操作对象【who】
        u -- 用户(user)
        g -- 同组用户(group)
        o -- 其他用户(other)
        a -- 所用用户(all)【默认】

        操作符【+-=】
        + -- 添加权限
        - -- 取消权限
        = -- 赋予给定权限并取消其他权限

        权限【mode】
        r -- 读
        w -- 写
        x -- 执行
        例:chmod u + wx file.txt
        数字设定法
        数字表示的含义
        0 -- 没有权限(-)
        1 -- 执行权限(x)
        2 -- 写权限(w)
        4 -- 读权限(r)
        操作符【+-=】
        + -- 添加权限
        - -- 取消权限
        = -- 赋予给定权限并取消其他权限 (默认为=)
        例:chmod 777 file.txt

chown
        将指定文件的拥有者改为指定的用户或组(change owner的缩写)
        用法
        chown + 文件所属用户 + 文件或目录名
        chown robertohuang text.txt
        chown + 文件所属用户:文件所属组 + 文件或目录名
        chown robertohuang:robertohuang text.txt
        chgrp
改变文件或目录的所属群组

        用法
        chgrp + 用户组 + 文件或目录名
        chgrp robertohuang text.txt

查找和检索

find
        按文件名查询：-name
        find + 路径 + -name + 文件名
        find /home/robertohuang -name a.txt
        按文件大小查询：-size
        find + 路径 + -size + 范围
        范围
        大于:+表示  -- +100k
        小于:-表示  --  -100k
        等于:不需要添加符号  -- 100k
        大小
        M必须大写
        k必须小写
        例子:
        等于100k的文件: find ~/ -size 100k
        大于100k的文件: find ~/ -size +100k
        大于50k, 小于100k的文件: find ~/ -size +50k -size -100k
        按文件类型查询：-type
        find + 路径 + -type + 类型
        类型
        1. 普通文件类型用 f 表示而不是 -
        2. d -> 目录
        3. l -> 符号链接
        4. b -> 块设备文件
        5. c -> 字符设备文件
        6. s -> socket文件，网络套接字
        7. p -> 管道
        例子:find /home/robertohuang -type d

grep
        按文件内容查找
        参数：-r
        grep -r + “查找的关键字” + 路径
        grep -r "main void" /home/robertohuang

压缩包管理
        .gz格式
        压缩:gzip命令 
        压缩过程中不保留源文件
        不能对目录进行压缩
        不能对多个文件进行打包压缩
        解压缩:gunzip 命令
        .bz2格式
        压缩:bzip2命令
        通过使用参数 -k(keep) 保留源文件
        不能对目录进行压缩
        不能对多个文件进行打包压缩
        解压缩:bunzip2命令

zip
        打包
        zip -r + 打包之后的文件名(dir.zip) + (打包的目录)dir
        解包
        unzip dir.zip
        使用参数-d来解压到指定目录 unzip dir.zip -d /home/robertohuang/test

tar
        该命令可以只打包不压缩
        通过添加参数，来完成文件的压缩和解压
        参数
        z -> 用 gzip 来压缩/解压缩文件
        j -> 用 bzip2 来压缩/解压缩文件
        c -> create，创建新的压缩文件。如果用户想备份一个目录或是一些文件，就要选择这个选项。
        x -> 从压缩文件中释放文件
        v -> 详细报告tar处理的文件信息
        f -> 指定压缩文件的名字

互斥
        (z -> 用 gzip 来压缩/解压缩文件, j -> 用 bzip2 来压缩/解压缩文件)
        互斥
        (c -> create，创建新的压缩文件。如果用户想备份一个目录或是一些文件，就要选择这个选项。, x -> 从压缩文件中释放文件)
        压缩
        tar + 参数（zcvf） + 压缩包名字.tar.gz + 原材料（要打包压缩的文件或目录）
        tar + 参数（jcvf） + 压缩包名字.tar.bz2 + 原材料（要打包压缩的文件或目录）
        解压缩
        tar + 参数（zxvf） + 已有的压缩包（test.tar.gz）
        tar + 参数（jxvf） + 已有的压缩包（test.tar.bz2）
        指定解压目录：添加参数 -C（大写）
        tar zxvf test.tar.gz -C + 解压目录(/home/robertohuang)

进程管理

who
        查看当前在线用户的情况
        登录的用户名
        使用的设备终端(pts)
        登录到系统的时间

tty设备
        tty1 - tty6 表示文字界面
        ctrl + alt + [F1-F6]
        tty7 图形界面
        子主题 1
        ctrl +　alt + F7
        互不影响
        (tty1 - tty6 表示文字界面, tty7 图形界面)
ps
        查看整个系统内部所运行的进程状况
        涉及的参数
        a:(all)当前系统所有用户的进程
        u:查看进程所有者及其他一些信息
        x:显示没有控制终端的进程 -- 不能与用户进行交互的进程【输入、输出】
        -e:显示所有进程
        -f:显示UID,PPIP,C与STIME栏位
        显示当前用户下所有进程

ps aux
        对显示的进程过滤
        ps aux | grep xxx
        什么是管道（|）
        指令1的输出作为指令2的输入
        指令2处理完毕，将信息输出到屏幕
        grep查询是需要占用一个进程的，所有结果 > 2 才能说明查询结果存在
        如果结果有一条，表示没有查询的进程
        查询结果中PID表示进程ID

kill
        用来终止指定的进程(terminate a process)的运行
        查看信号编号
        kill -l
        杀死进程
        kill -9 89899【PID-进程标识号】
        向当前进程发送了9号信号（SIGKILL）

env
        查看当前进程环境变量
        环境变量
        当前系统下用户的配置路径信息
        格式为键值对：key=value：value  （多个值之间用 ： 分隔）

PATH:该环境变量中记录着shell命令解析器去查找命令的目录位置,从前往后的顺序查找

LANG:语言以及字符集

top
        相当于windows下的任务管理器
        文字版
        不能翻页

网络管理
        ifconfig
        获取网络接口配置信息,还可以修改这些配置
        获取网络接口信息

        ping
        测试与目标主机的连通性
        命令格式
        ping [参数] [主机名或IP地址]
        参数
        -c 数目:在发送指定数目的包后停止。
        -i 秒数:设定间隔几秒送一个网络封包给一台机器，预设值是一秒送一次

        nslookup
        需要先安装nslookup:yum -y install bind-utils
        查看服务器域名对应的IP地址
        一般访问网站都是使用域名,如:www.baidu.com,使用该命令就可查看百度所有服务器的IP地址

用户管理

创建用户
        adduser + 用户名
        useradd -s /bin/bash -g usertest -d /home/usertest -m usertest
        -s:指定新用户登陆时shell类型
        -g:指定所属组，该组必须已经存在
        -d:用户家目录
        -m 用户家目录不存在时,自动创建该目录

设置用户组
        groupadd usertest
        删除用户
        deluser + 用户名
        userdel -r usertest
        选项 -r 的作用是把用户的主目录一起删除

切换用户
        su + 用户名

设置密码
        sudo passwd + 用户名（luffy）
        passwd root
        passwd
        设置root密码
        (passwd root, passwd)

退出登录用户
exit

其他命令

清屏
        clear
        Ctrl + l

查看帮助命令
        man + 命令,如man ls

设置或查看别名
查看
        alias

设置
        alias pag='ps aux | grep'
        需要长久有效需要去设置配置文件:.bashrc

echo
        在显示器上显示数据
        普通数据：echo 字符串
        显示环境变量：echo $PATH
        显示上一次程序退出值：echo $?
        $ : 取值
        ?：最近一次程序退出时的返回值
        (显示环境变量：echo $PATH, 显示上一次程序退出值：echo $?)

关机重启
        poweroff
        reboot
        shutdown
        参数
        -t<秒数>:送出警告信息和删除信息之间要延迟多少秒
        -k:只是送出信息给所有用户，但不会实际关机
        -r:shutdown之后重新启动
        -h:将系统关机
        -n:不调用init程序进行关机,而由shutdown自己进行
        -f:重新开机时,跳过fsck指令,不检查档案系统
        -F:重新开机时,强迫做fsck检查
        -c:将已经正在shutdown的动作取消

        例子:
        shutdown -r now 立刻重新开机
        shutdown -h now 立刻关机
        shutdown -k now 'Hey! Go away! now....' 发出警告讯息, 但没有真的关机
        shutdown -t3 -r now 立刻重新开机,但在警告和删除processes 之间, 延迟3秒钟.
        shutdown -h 10:42 'Hey! Go away!' 10:42 分关机
        shutdown -r 10 'Hey! Go away!' 10 分钟后关机
        shutdown -c 将刚才下的shutdown指令取消,必须切换至其它tty,登入之後,才能下此一指令
        shutdown now切换至单人操作模式(不加任何选项时)

free
        查看内存使用情况
