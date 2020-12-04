# 使用 benchmarkSQL 测试数据库的 TPCC - konglingbin - 博客园
压力测试是指在 MySQL 上线前，需要进行大量的压力测试，从而达到交付的标准。压力测试不仅可以测试 MySQL 服务的稳定性，还可以测试出 MySQL 和系统的瓶颈。

TPCC 测试：Transaction Processing Performance Council，要熟练使用

TPC 是一系列事务处理和数据库基准测试的规范。其中 TPC-C 是针对 OLTP 的基准测试模型，一方面可以衡量数据库的性能，另一方面可以衡量硬件性价比，也是广泛应用并关注的一种测试模型。

TPC-C 模型是以一个在线零售业为例，设计的一种模型。具体架构如下所示：

 ![](https://img2018.cnblogs.com/blog/1309603/201905/1309603-20190508230126685-1687114996.png)

 [https://rensanning.iteye.com/blog/2159732?utm_source=jiancool](https://rensanning.iteye.com/blog/2159732?utm_source=jiancool)

 [SysBench](https://launchpad.net/sysbench)   
使用： 

引用

$ sysbench --test=oltp --db-driver=mysql --mysql-password=sbtest prepare   
$ sysbench --test=oltp --db-driver=mysql --mysql-password=sbtest run

结果： 

引用

sysbench 0.4.12:  multi-threaded system evaluation benchmark 

Running the test with following options:   
Number of threads: 1 

Doing OLTP test.   
Running mixed OLTP test   
Using Special distribution (12 iterations,  1 pct of values are returned in 75 pct cases)   
Using "BEGIN" for starting transactions 

TPC-C 测试模型给基准测试提供了一种统一的测试标准，并非实际应用系统中的真实测试结果，但通过测试结果，可以大体观察出 MySQL 数据库服务稳定性、性能以及系统性能等一系列问题。TPC-C 仅仅是一个测试模型，而在实际测试中，需要参考和使用一些测试工具，对系统和 MySQL 数据库进行压力测试、稳定性测试。

1. 安装 bzr 工具

\[root@mysql1 /]# yum install bzr

2. 下载 tpcc-mysql

\[root@mysql1 /]# bzr branch lp:~percona-dev/perconatools/tpcc-mysql

3. 编译安装 tpcc-mysql

\[root@mysql1 /]# export PATH=/usr/local/mysql/bin:$PATH

\[root@mysql1 /]# cd tpcc-mysql/src

\[root@mysql1 src]# make

4. 创建库

\[mysql@mysql1 ~]$ mysqladmin -usystem -p123456 -S /data/mysqldata/3306/mysql.sock create tpcc

5. 创建表

\[mysql@mysql1 ~]$ mysql -usystem -p123456 -S /data/mysqldata/3306/mysql.sock tpcc &lt; /tpcc-mysql/create_table.sql

6. 添加外键

\[mysql@mysql1 ~]$ mysql -usystem -p123456 -S /data/mysqldata/3306/mysql.sock tpcc &lt; /tpcc-mysql/add_fkey_idx.sql

7. 加载数据

tpcc 默认会读取 /var/lib/mysql/mysql.sock 这个 socket 位置，因此如果你的 socket 不在相应路径的话，就需要做个软连接

\[root@mysql1 ~]# ln -s /data/mysqldata/3306/mysql.sock /var/lib/mysql/mysql.sock

\[root@mysql1 ~]# ln -s /usr/local/mysql/lib/libmysqlclient.so.18 /usr/lib64

如果出现错误，尝试上面的步骤

\[mysql@mysql1 ~]$ /tpcc-mysql/tpcc_load localhost tpcc system "123456" 10

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* ###easy### TPC-C Data Loader  \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<Parameters>

     \[server]: localhost

     \[port]: 3306

     \[DBname]: tpcc

       \[user]: system

       \[pass]: 123456

  \[warehouse]: 10

TPCC Data Load Started...

Loading Item

.................................................. 5000

.................................................. 10000

.................................................. 15000

...DATA LOADING COMPLETED SUCCESSFULLY.

8. 进行测试

\[mysql@mysql1 ~]$ /tpcc-mysql/tpcc_start -h localhost -d tpcc -u system -p "123456" -w 1 -c 10 -r 10 -l 20 -f /home/mysql/tpcc_mysql.log -t /home/mysql/tpcc_mysql.rtx

\-h：测试主机

\-d：测试的数据库

\-u：测试的用户

\-p：测试用户的密码

\-w：测试的 warehouse 数

\-c：测试的连接线程数

\-r：预热时间，warmup_time，以秒为单位，默认是 10 秒，目的是为了将数据加载到内存

\-l：测试时间，默认为 20 秒

\-i：report_interval 指定生成报告的间隔时间

\-f：report_file 将测试中各项操作的记录输出到指定文件内保存

\-t：trx_file 输出更详细的操作信息到指定文件内保存

下面是返回结果：

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\* ###easy### TPC-C Load Generator \*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

option h with value 'localhost'

option d with value 'tpcc'

option u with value 'system'

option p with value '123456'

option w with value '1'

option c with value '10'

option r with value '10'

option l with value '20'

option f with value '/home/mysql/tpcc_mysql.log'

option t with value '/home/mysql/tpcc_mysql.rtx'

<Parameters>

     \[server]: localhost

     \[port]: 3306

     \[DBname]: tpcc

       \[user]: system

       \[pass]: 123456

  \[warehouse]: 1

 \[connection]: 10

     \[rampup]: 10 (sec.)

    \[measure]: 20 (sec.)

RAMP-UP TIME.(10 sec.)

MEASURING START.

  10, 686(0):2.044|3.593, 684(0):0.487|1.325, 68(0):0.136|0.212, 68(0):2.060|2.095, 69(0):5.817|6.441

  20, 676(0):1.508|2.585, 679(0):0.352|1.618, 67(0):0.140|0.294, 68(0):1.585|1.762, 67(0):4.154|5.968

分为 6 项，依次为操作时间 (秒)、创建订单、订单支付、查询订单、发货以及查询库存

STOPPING THREADS..........

<Raw Results>

  \[0] sc:1362  lt:0  rt:0  fl:0

  \[1] sc:1363  lt:0  rt:0  fl:0

  \[2] sc:135  lt:0  rt:0  fl:0

  \[3] sc:136  lt:0  rt:0  fl:0

  \[4] sc:136  lt:0  rt:0  fl:0

 in 20 sec.

&lt;Raw Results2(sum ver.)>

  \[0] sc:1362  lt:0  rt:0  fl:0

  \[1] sc:1363  lt:0  rt:0  fl:0

  \[2] sc:135  lt:0  rt:0  fl:0

  \[3] sc:136  lt:0  rt:0  fl:0

  \[4] sc:136  lt:0  rt:0  fl:0

<Constraint Check> (all must be \[OK])

 \[transaction percentage]

        Payment: 43.52% (>=43.0%) \[OK]

   Order-Status: 4.31% (>= 4.0%) \[OK]

       Delivery: 4.34% (>= 4.0%) \[OK]

    Stock-Level: 4.34% (>= 4.0%) \[OK]

 \[response time (at least 90% passed)]

      New-Order: 100.00%  \[OK]

        Payment: 100.00%  \[OK]

   Order-Status: 100.00%  \[OK]

       Delivery: 100.00%  \[OK]

    Stock-Level: 100.00%  \[OK]

<TpmC> 

                 4086.000 TpmC  每分钟能够处理的订单数量

benchmarkSQL 在使用时分为数据准备和测试执行两个阶段，其中数据准备阶段完全在命令行环境，而执行测试则根据当前用户状态而自动选择在命令行，或界面中执行。JDK1.7

二、数据准备：  
1. 在 lib 中放置 JDBC 驱动；  
2. 修改 run 目录下：run 开头的 3 个文件，修改里面 jdbc 驱动名称；  
3. 修改配置文件，其中 props.ora 和 props.pg 分别是对应 oracle 和 pg 数据库的；

第一个部分是 JDBC 连接信息。

第二个部分是场景设置，其中 runTxnsPerTerminal 是每分钟执行事务数，runMins 是执行多少分钟，limitTxnsPerMin 是每分钟执行的事务总数，并且这里时间的单位是分钟。场景执行的最低条件是第二项大于 0。

第三个部分是 TPCC 中，五个事务执行的比例，总数等于 100，通常不用修改。

1) 建表：  
建表的前提是初始化数据库

然后执行./runSQL kingbase.properties sqlTableCreates

sqlTableCreates 是默认的建表语句，首先在库中创建一个 benchmarksql 模式，所有表都创建在这个模式下。

\* 由于建表语句中没有表空间的设置信息，因此如果创建比较大的表，系统会报错，只要根据之前执行 TPCC 测试时的建表语句，稍加修改即可。

\* 在 ISQL 模式下，使用 set search_path = 模式名； 可以切换当前操作路径，按默认的方式查看指定模式下的内容。

\* 在 run 中，对应建表，建索引，还有删除表，复制表，删除索引等几个脚本，可以配合使用。

2) 加载数据：  
在 run 下执行./runLoader.sh kingbase.properties numWarehouses 1300 

注意如果表过大，需要提前修改建表语句，增加表空间。

3) 创建索引：  
在 run 下执行./runSQL kingbase.properties sqlIndexCreates

4) 执行测试：  
在 run 下执行./runBenchmark.sh kingbase.properties

系统开始滚屏，执行指定时间后显示需要的统计信息：

 一、BenchmarkSQL 是什么？  
      BenchmarkSQL 是一款经典的开源数据库测试工具，内嵌了 TPCC 测试脚本，可以对 EnterpriseDB、PostgreSQL、MySQL、Oracle 以及 SQL Server 等数据库直接进行测试。

二、测试前提  
1. 安装 JDK。因为 BenchmarkSQL 本身是使用 Java 语言编写的，所以如果在 Linux 系统下还没有安装 JDK 的话，我们首先需要对其进行安装；  
2. 安装 PostgreSQL 数据库系统。俗话说巧妇难为无米之炊，测试之前肯定需要有测试对象，本文是测试 PG 系统，故需安装有 PG；  
3. 安装 BenchmarkSQL  
可到 [http://sourceforge.net](http://sourceforge.net) 中搜索 BenchmarkSQL 即可下到，windows，linux 版均有。我下载的是 linux 版的软件包 BenchmarkSQL-2.3.3.zip，unzip 解压后可以在 README 文件中看到该软件的使用说明，下面用中文具体介绍一下它的使用方法。

三、测试步骤  
1. 启动待测试的数据库系统，这里即指启动 PostgreSQL

2. 在 BenchmarkSQL-2.3.3/run 目录下找到 postgres.properties 配置文件，修改该文件如下：  
driver=org.postgresql.Driver  
conn=jdbc:postgresql://localhost:5432/test        # 链接数据库地址  
user=postgres      # 链接数据库用户名  
password=password    # 密码  
如果想测试其他数据库系统，则修改其他相应的配置文件即可，如 oracle.properties 等等。

3. 创建 TPC-C 基础表（即上篇博文中介绍的 TPC-C 模拟场景中 9 张表）  
命令： runSQL.sh postgres.properties sqlTableCreates

4. 向数据库中导入指定大小的数据 (参考资料 2 中此步有个小问题，多写一个等号)  
命令：loadData.sh postgres.properties numWarehouses 10  
numWarehouse 指的是仓库数（具体含义见上篇博文），默认为 1，导入 9 张表的数据大小大概 70 多 M，  
当 numWarehouse 为 10 时，数据大小可以近似当作 1GB 数据。

5. 为基础表创建必要的索引  
命令： runSQL.sh postgres.properties sqlIndexCreates

6. 运行 runBenchmark.sh 借助 GUI 程序测试数据库  
命令：runBenchmark.sh postgres.properties  
注意：不要忘记设置图形界面的仓库数时要与第 4 步中设置的数量相符；此外，测试的结果报告除了显示在图形界面有显示以外，还在 run/reports 目录下有备份，随时可以查阅。 
 [https://www.cnblogs.com/klb561/p/10835775.html](https://www.cnblogs.com/klb561/p/10835775.html)
