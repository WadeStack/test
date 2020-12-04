# BenchmarkSQL5.0 数据库 TPC-C 基准测试 - 瑾熙的博客 | JL Blog
* * *

### 1、TPC-C 介绍[](#1tpc-c介绍)

TPC（Transaction Processing-Performance Council）是事务处理性能委员会的缩写。该组织的主要功能是指定商用应用基准程序 (Benchmark) 的标准规范、性能和价格度量，并管理测试结果的发布。  
其中 TPC-C 是在线事务处理（OLTP）的基准程序。TPC-C 会模拟一个批发商的货物管理环境，旨在模拟仓储、订单、配送等 OLTP 业务的过程。通过模拟这套复杂的业务流程，收集测试中的指标，从而得出最终的 TpmC 值，即每分钟可处理的事务数。

### 2、BenchmarkSQL 工具介绍[](#2benchmarksql工具介绍)

BenchmarkSQL 是一个同时支持 Oracle、MySQL 等关系型数据库的基准测试工具，通过使用 BenchmarkSQL 对数据库进行 TPC-C 标准测试，即模拟多种事务处理：新订单、支付操作、订单状态查询、发货、库存状态查询等，从而获得最终的 TpmC 值。

### 3、BenchmarkSQL 安装[](#3benchmarksql安装)

##### 3.1、配置 Java 环境变量[](#31配置java环境变量)

    [root@localhost opt]# tar zxvf jdk-8u65-linux-x64.tar.gz
    [root@localhost opt]# ln -s /opt/jdk1.8.0_65/ /usr/local/java
    [root@localhost opt]# vi /etc/profile
    export JAVA_HOME=/usr/local/java
    export PATH=$PATH:$JAVA_HOME/bin
    [root@localhost opt]# source /etc/profile
    [root@localhost opt]# java -version
    openjdk version "1.8.0_222"
    OpenJDK Runtime Environment (build 1.8.0_222-b10)
    OpenJDK 64-Bit Server VM (build 25.222-b10, mixed mode 

##### 3.2、安装 BenchmarkSQL 并编译[](#32安装benchmarksql并编译)

    [root@localhost opt]# unzip benchmarksql-5.0.zip
    [root@localhost opt]# yum install -y ant
    [root@localhost opt]# cd /opt/benchmarksql-5.0
    [root@localhost benchmarksql-5.0]# ant 

##### 3.3、添加 jdbc 驱动 jar 包[](#33添加jdbc驱动jar包)

将需要压测的数据库的驱动 jar 包放置 benchmarksql-5.0 的 lib 目录下

### 4、实际测试[](#4实际测试)

`这里的测试环境是某项目上的数据库服务器，测试了国产数据 HighGo4.3.2 和 Oracle11.2.0.4 的情况对比。在实际测试过程中例如测试 HighGo 的时候会将 Oracle 的服务停掉，同理测试 Oracle 的时候会将 HighGo 的服务停掉。另外某些配置参数需要调成相近，例如 HighGo 中的 shared_buffers 参数为设置内存占用参数调成物理内存的 70%，Oracle 的 SGA 大小也要调成 70% 占用。最后这种压测也只是基准测试，不能完全代表实际项目中的情况。`

##### 4.1、服务器硬件配置[](#41服务器硬件配置)

    操作系统： CentOS Linux release 7.6.1810 (Core)
    CPU： Intel(R) Xeon(R) CPU E7-4820 v2 @ 2.00GHz 64core
    内存：128G
    硬盘：1T 

##### 4.2、数据版本以及压测工具版本[](#42数据版本以及压测工具版本)

    Oracle版本：11.2.0.4
    HighGo版本：4.3.2 

##### 4.3、props 文件编写[](#43props文件编写)

jdbc 连接部分改成对应的数据库的 JDBC 连接，这里以 Oracle 为例:  
创建文件 props.ora 文件，文件存放在 run 目录下。  
其中压测的所连接的用户或者库需要手动创建。

    db=oracle
    driver=oracle.jdbc.driver.OracleDriver
    conn=jdbc:oracle:thin:@localhost:1521:orcl
    user=benchmarksql
    password=11111

    // 设定仓库数
    warehouses=20
    loadWorkers=4

    // 并发数
    terminals=64

    runTxnsPerTerminal=0
    // 压测时间
    runMins=10
    //每分钟的事务
    limitTxnsPerMin=0

    //The following five values must add up to 100
    newOrderWeight=45
    paymentWeight=43
    orderStatusWeight=4
    deliveryWeight=4
    stockLevelWeight=4

    // Directory name to create for collecting detailed result data.
    // Comment this out to suppress.
    resultDirectory=my_result_%tY-%tm-%td_%tH%tM%tS
    osCollectorScript=./misc/os_collector_linux.py
    osCollectorInterval=1
    //osCollectorSSHAddr=user@dbhost
    //指定网卡名称以及磁盘
    osCollectorDevices=net_eth0 blk_sda 

##### 4.4、准备测试数据[](#44准备测试数据)

需要执行部分脚本构建测试数据

    [root@localhost run]# ./runSQL.sh props.ora ./sql.common/tableCreates.sql
    [root@localhost run]# ./runLoader.sh props.ora numWAREHOUSES 20
    [root@localhost run]# ./runSQL.sh props.ora ./sql.common/indexCreates.sql 

##### 4.5、压测拓扑[](#45压测拓扑)

![](https://github.com/caosw199509/caosw199509.github.io/blob/master/work_img/2019-09-06/benchmarksql.png?raw=true)

##### 4.6、压测描述[](#46压测描述)

按照 BenchmarkSQL 官方文档中描述，其测试并发压力一般为 CPU 个数的 2-8 倍，故挑选了以下三种测试用例。  
用例一：测试 HighGo、Oracle 在 BenchmarkSQL 工具 64 线程 20 仓库下的 TpmC；  
用例二：测试 HighGo、Oracle 在 BenchmarkSQL 工具 128 线程 20 仓库下的 TpmC；  
用例三：测试 HighGo、Oracle 在 BenchmarkSQL 工具 64 线程 40 仓库下的 TpmC；

##### 4.7、用例一测试结果[](#47用例一测试结果)

###### 4.7.1、HighGo[](#471highgo)

![](https://github.com/caosw199509/caosw199509.github.io/blob/master/work_img/2019-09-06/highgo01.png?raw=true)

在 20 仓 64 并发终端下，HighGo 数据库 Tpmc 值为 96514.2

###### 4.7.2、Oracle[](#472oracle)

![](https://github.com/caosw199509/caosw199509.github.io/blob/master/work_img/2019-09-06/oracle01.png?raw=true)

在 20 仓 64 并发终端下，Oracle 数据库 Tpmc 值为 84668.78

##### 4.8、用例二测试结果[](#48用例二测试结果)

###### 4.8.1、HighGo[](#481highgo)

![](https://github.com/caosw199509/caosw199509.github.io/blob/master/work_img/2019-09-06/highgo02.png?raw=true)

在 20 仓 128 并发终端下，HighGo 数据库 Tpmc 值为 90814.89

###### 4.8.2、Oracle[](#482oracle)

![](https://github.com/caosw199509/caosw199509.github.io/blob/master/work_img/2019-09-06/oracle02.png?raw=true)

在 20 仓 128 并发终端下，Oracle 数据库 Tpmc 值为 108959.27

##### 4.9、用例三测试结果[](#49用例三测试结果)

###### 4.9.1、HighGo[](#491highgo)

![](https://github.com/caosw199509/caosw199509.github.io/blob/master/work_img/2019-09-06/highgo03.png?raw=true)

在 40 仓 64 并发终端下，HighGo 数据库 Tpmc 值为 61125.29

###### 4.9.2、Oracle[](#492oracle)

![](https://github.com/caosw199509/caosw199509.github.io/blob/master/work_img/2019-09-06/oracle03.png?raw=true)

在 40 仓 64 并发终端下，Oracle 数据库 Tpmc 值为 64919.13

##### 4.10、清楚测试环境[](#410清楚测试环境)

同样的有脚本可以进行清除

    [root@localhost run]# ./runDatabaseDestroy.sh props.ora 

 [https://caosw.top/2019/09/06/BenchmarkSQL5.0%E6%95%B0%E6%8D%AE%E5%BA%93TPC-C%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95/](https://caosw.top/2019/09/06/BenchmarkSQL5.0%E6%95%B0%E6%8D%AE%E5%BA%93TPC-C%E5%9F%BA%E5%87%86%E6%B5%8B%E8%AF%95/)
