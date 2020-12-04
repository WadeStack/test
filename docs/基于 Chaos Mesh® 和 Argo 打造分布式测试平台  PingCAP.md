# 基于 Chaos Mesh® 和 Argo 打造分布式测试平台 | PingCAP
   基于 Chaos Mesh® 和 Argo 打造分布式测试平台 | PingCAP                          

[![](https://pingcap.com/images/pingcap-logo.png)
](/zh)

-   [PingCAP University](https://university.pingcap.com/)
-   [文档](https://docs.pingcap.com/zh)
-   [案例](/cases-cn)
-   [社区](/community-cn)
-   [博客](/blog-cn)
-   [关于](/about-cn)
-   [问答](https://asktug.com)
-   [下载试用](/download-cn)
-   [联系我们](mailto:info@pingcap.com)

[![](https://pingcap.com/images/pingcap-logo.png)
](/en)

-   [文档](https://docs.pingcap.com/zh/tidb/v4.0/)
-   [案例](/cases-cn)
-   [社区](/community-cn)
-   [博客](/blog-cn)
-   [关于](/about-cn)
-   [问答](https://asktug.com)
-   [下载试用](/download-cn)
-   [联系我们](mailto:info@pingcap.com)
-   [PingCAP University](https://university.pingcap.com/)

#### **Contact**

-   [](javascript:void(0))

    ![](https://pingcap.com/images/wechat-qrcode.jpg)

    微信扫一扫  
    微信 ID：pingcap2015

[English](/blog)

热门标签[](/blog-cn/index.xml "RSS Feed")

[ALL (250)](#)

[Chaos Mesh (7)](#Chaos-Mesh) [Committer (3)](#Committer) [Contributor (9)](#Contributor) [DM (2)](#DM) [DM 源码阅读 (10)](#DM-%e6%ba%90%e7%a0%81%e9%98%85%e8%af%bb) [Go (3)](#Go) [HTAP (3)](#HTAP) [Hackathon (4)](#Hackathon) [K8s (2)](#K8s) [Key Visualizer (2)](#Key-Visualizer) [Kubernetes (3)](#Kubernetes) [Linux (2)](#Linux) [MVCC (2)](#MVCC) [MySQL (2)](#MySQL) [PD (5)](#PD) [Percolator (2)](#Percolator) [PingCAP (2)](#PingCAP) [Prometheus (3)](#Prometheus) [Raft (11)](#Raft) [RocksDB (3)](#RocksDB) [Rust (5)](#Rust) [SQL (6)](#SQL) [Spanner (2)](#Spanner) [TiDB (78)](#TiDB) [TiDB 4.0 新特性 (11)](#TiDB-4.0-%e6%96%b0%e7%89%b9%e6%80%a7) [TiDB Binlog (5)](#TiDB-Binlog) [TiDB Binlog 源码阅读 (9)](#TiDB-Binlog-%e6%ba%90%e7%a0%81%e9%98%85%e8%af%bb) [TiDB Ecosystem Tools (3)](#TiDB-Ecosystem-Tools) [TiDB Operator (5)](#TiDB-Operator) [TiDB 性能挑战赛 (2)](#TiDB-%e6%80%a7%e8%83%bd%e6%8c%91%e6%88%98%e8%b5%9b) [TiDB 易用性挑战赛 (4)](#TiDB-%e6%98%93%e7%94%a8%e6%80%a7%e6%8c%91%e6%88%98%e8%b5%9b) [TiDB 源码阅读 (24)](#TiDB-%e6%ba%90%e7%a0%81%e9%98%85%e8%af%bb) [TiFlash (7)](#TiFlash) [TiKV (27)](#TiKV) [TiKV 源码解析 (20)](#TiKV-%e6%ba%90%e7%a0%81%e8%a7%a3%e6%9e%90) [TiSpark (4)](#TiSpark) [WebAssembly (2)](#WebAssembly) [gRPC (2)](#gRPC) [事务 (4)](#%e4%ba%8b%e5%8a%a1) [优化器 (2)](#%e4%bc%98%e5%8c%96%e5%99%a8) [分布式系统前沿技术 (4)](#%e5%88%86%e5%b8%83%e5%bc%8f%e7%b3%bb%e7%bb%9f%e5%89%8d%e6%b2%bf%e6%8a%80%e6%9c%af) [分布式系统测试 (3)](#%e5%88%86%e5%b8%83%e5%bc%8f%e7%b3%bb%e7%bb%9f%e6%b5%8b%e8%af%95) [备份恢复 (2)](#%e5%a4%87%e4%bb%bd%e6%81%a2%e5%a4%8d) [工具 (4)](#%e5%b7%a5%e5%85%b7) [性能 (4)](#%e6%80%a7%e8%83%bd) [数据同步 (2)](#%e6%95%b0%e6%8d%ae%e5%90%8c%e6%ad%a5) [最佳实践 (6)](#%e6%9c%80%e4%bd%b3%e5%ae%9e%e8%b7%b5) [架构 (6)](#%e6%9e%b6%e6%9e%84) [版本 (2)](#%e7%89%88%e6%9c%ac) [社区 (102)](#%e7%a4%be%e5%8c%ba) [社区动态 (29)](#%e7%a4%be%e5%8c%ba%e5%8a%a8%e6%80%81) [集群调度 (2)](#%e9%9b%86%e7%be%a4%e8%b0%83%e5%ba%a6)

基于 Chaos Mesh® 和 Argo 打造分布式测试平台 \[![](https://pingcap.com/images/svgs/link.svg)

# ]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/# 基于 - chaos-mesh - 和 - argo - 打造分布式测试平台](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#基于-chaos-mesh-和-argo-打造分布式测试平台))

-   ![](https://pingcap.com/images/svgs/icon-date.svg)
    Mon, Jun 29, 2020
-   ![](https://pingcap.com/images/svgs/icon-writer.svg)
    叶奔， 殷成文

不久前我们开源了基于 Kubernetes 的混沌测试工具 [Chaos Mesh®](https://chaos-mesh.org)，Chaos Mesh 提供了模拟系统异常状况的能力，但这只是混沌工程中的一环，完整混沌工程核心原则包含了系统稳定状态的定义、提出假设、运行实验以及验证和改进。

本篇文章主要介绍我们是如何在 Chaos Mesh 和 [Argo](https://argoproj.github.io/) 的基础上打造自己的自动化测试平台 [TiPocket](https://github.com/pingcap/tipocket)，实现完全自动化的混沌测试，构成混沌测试完整闭环。

为什么需要 TiPocket? \[![](https://pingcap.com/images/svgs/link.svg)

## ]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/# 为什么需要 - tipocket-](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#为什么需要-tipocket-))

为了确保用户的数据安全，我们需要确保给用户提供的每一个 TiDB 版本都已经经过了严格的测试，所以我们为 TiDB 设计了各种异常场景，并实现了数十个测试 Case，所以在我们的 Kubernetes 集群中，可能同时运行着十几个甚至几十个混沌实验，即使我们拥有了 Chaos Mesh 来帮助我们管理错误注入，但这还远不够，我们还需要去管理 TiDB 集群，需要去收集指标，需要去分析结果，同时进行如此多的混沌实验，另一方面，我们还需要对 TiDB 生态中的其他工具进行混沌测试，这是无法想象的，因此，我们开发了 TiPocket 来解放自己。

**TiPocket 是一个基于 Kubernetes 和 Chaos Mesh 的完全自动化测试框架，目前我们主要使用它用来测试 TiDB 集群，不过由于它 All-in-K8s 的特性以及可扩展的接口，它目前也支持测试 TiDB 生态中的其他组件，只要简单的添加应用在 Kubernetes 中 Create/Delete 的逻辑，就可以很轻松的添加对各种应用的支持。**

Chaos Mesh 提供故障模拟的能力 \[![](https://pingcap.com/images/svgs/link.svg)

## ]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#chaos-mesh - 提供故障模拟的能力 -](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#chaos-mesh-提供故障模拟的能力-))

故障注入可以说是混沌测试中重要的一环，并且在分布式数据库领域，可能遇到的故障又非常的多，不仅仅是节点故障、各种网络故障、文件系统故障，更甚至可能遇到内核故障。如果 TiDB 不能正确的处理这些异常，那么后果是无法想象的，这也是最开始我们开发 Chaos Mesh 的主要原因之一。而 TiPocket 中很好的结合了 Chaos Mesh，将 Chaos Mesh 作为最基本的依赖之一，以达到混沌测试中故障注入的目的。 

![](https://download.pingcap.com/images/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/1-chaos-mesh.png)

目前我们已经在 TiPocket 提供了多种类型的故障注入： 

-   Network：基于 Chaos Mesh 的 NetworkChaos，提供模拟的网络分区，或者链路随机的丢包、乱序、重复、时延等。
-   Time Skew：基于 TimeChaos，模拟待测试容器发生时间偏移。TimeChaos 的实现也是非常有趣，感兴趣的话可以参考我们以前的 [文章](https://pingcap.com/blog/simulating-clock-skew-in-k8s-without-affecting-other-containers-on-node/)。
-   Kill：通过 PodChaos 来 kill 对应的 pod。细分下来我们也实现了多种 kill 类型，最简单的就是随机删除集群内的任意 pod；如果针对各个组件，也有专门的 Chaos 随机 kill 一个或两个 TiKV 节点，或者是专门 kill PD 的 leader 节点。
-   IO：基于 IOChaos，我们用的比较多的是给 TiKV 注入 IO Delay，再去看写入的情况。

解决了故障注入的问题，那么接下来我们就需要判断我们的系统在 TiDB 注入了故障后，是否符合预期呢？

如何判断 TiDB 是否正常？ \[![](https://pingcap.com/images/svgs/link.svg)

## ]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/# 如何判断 - tidb - 是否正常 -](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#如何判断-tidb-是否正常-))

为了高效的达成这目标，TiPocket 中实现了数十个测试 Case 并结合不同的检查工具来验证 TiDB 是正常。下面会用几个测试 Case 为例，简要介绍 TiPocket 是如何验证 TiDB 的。  

### Fuzz 测试：[SQLsmith](https://github.com/pingcap/tipocket/tree/master/pkg/go-sqlsmith) \[![](https://pingcap.com/images/svgs/link.svg)

]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#fuzz - 测试 sqlsmith-](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#fuzz-测试sqlsmith-))

SQLsmith 是一个生成随机 SQL 的工具，TiPocket 分别创建一个 TiDB 集群和一个 MySQL 实例，使用 go-sqlsmith 生成的随机 SQL 分别在 TiDB 和 MySQL 上执行，并对 TiDB 集群注入各种故障，最后对比执行的结果，如果出现结果不一致的情况，那么我们可以判断我们的系统存在问题。

### 事务一致性测试：Bank/Porcupine\[![](https://pingcap.com/images/svgs/link.svg)

]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/# 事务一致性测试 bankporcupine](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#事务一致性测试bankporcupine))

#### 1. [Bank](https://github.com/pingcap/tipocket/tree/master/cmd/bank)\[![](https://pingcap.com/images/svgs/link.svg)

]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#1-bank](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#1-bank))

银行测试是模拟一个银行系统中的转账流程。在这个测试中，我们创建一系列模拟银行账户，并随时选择两个账户使用事务进行相互转账，一个账户减去一定的金额，另一个账户增加对应的金额，这样的交易不断的并发执行着。在快照隔离下，所有的转账都必须保证每一个时刻所有的账户的总金额是相同的。TiDB 即使在注入各种故障的情况下，依然需要保证这样的约束是成立的，一旦约束被破坏，那么就可以判断此时的系统是不符合预期的。 

#### 2. [Porcupine](https://github.com/anishathalye/porcupine) \[![](https://pingcap.com/images/svgs/link.svg)

]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#2-porcupine-](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#2-porcupine-))

Porcupine 一个用 Go 实现的线性一致性验证工具。是基于 [P-compositionality](http://www.kroening.com/papers/forte2015-li.pdf) 算法，P-compositionality 算法利用了线性一致性的 Locality 原理，即如果一个调用历史的所有子历史都满足线性一致性，那么这个历史本身也满足线性一致性。因此，可以将一些不相关的历史划分开来，形成多个规模更小的子历史，转而验证这些子历史的线性一致性。在 TiPocket  有许多 Case 中使用了 [Pocupine 检查器](https://github.com/pingcap/tipocket/tree/master/pkg/check/porcupine) 去检查生成的历史，从而判断 TiDB 是否满足线性一致性的约束。 

### 事务隔离级别测试：[Elle](https://github.com/jepsen-io/elle)\[![](https://pingcap.com/images/svgs/link.svg)

]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/# 事务隔离级别测试 elle](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#事务隔离级别测试elle))

Elle 是用来验证数据库事务隔离级别的检查工具。Elle 是一个纯黑盒的测试工具，巧妙的构造了一个测试场景，通过客户端生成的历史构造出依赖关系图，通过判断依赖图中是否有环以及分析环来确定事务的出现的异常类型，来确定事务的隔离级别。在 TiPocket 中，我们参考 Elle 项目，实现了 Go 版本的 Elle 检查工具 [go-elle](https://github.com/pingcap/tipocket/tree/master/pkg/elle)，并结合 go-elle 工具来验证 TiDB 的隔离级别。

这些只是 TiPocket  中用来验证 TiDB 正确性的一小部分，如果读者有兴趣可以自行阅读相关 [源码](https://github.com/pingcap/tipocket)，查看更多的验证方法。现在我们有了故障注入，有了待测的 TiDB 集群，有了检验 TiDB 的方式，那么我们该如让这些混沌实验自动化的运行起来呢？如何最大化的利用资源呢？在下一小节我们会介绍 TiPocket 中是如何解决这个问题的。

Argo 让流程自动化起来  \[![](https://pingcap.com/images/svgs/link.svg)

## ]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#argo - 让流程自动化起来 --](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#argo-让流程自动化起来--))

和大多数的工程师一样，我们第一个想法是自己开发，造轮子，让 TiPocket 具备调度的功能和管理的功能，但是考虑到我们目前的人力和时间，并且我们知道目前已经有很多开源的工具可以提供类似的功能，所以最后我们选择让 TiPocket 更加纯粹，将调度和管理交给更加合适的工具去负责。在考虑到我们 All-in-K8s 的特性，[Argo](https://github.com/argoproj/argo) 就成为我们不二的选择。

![](https://pingcap.com/images/svgs/loader-spinner.svg)

Argo 是一个为 Kubernetes 而设计的工作流引擎，很早就在社区中开源，并且马上得到了广泛的关注和应用。像在知名的 [kubeflow](https://www.kubeflow.org/) 项目中，就大量使用了 Argo。下面我们首先来介绍下 Argo 的基本概念，再来讲讲如何结合 TiPocket 和 Argo。

Argo 为工作流抽象出了几种 [CRD](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)。最主要的包括了 Workflow Template、Workflow 以及 Cron Workflow。

-   Workflow Template 可以理解成工作流的模版，我们可以为每个不同的测试任务预先定义好模版，实际运行测试时传入不同的参数。
-   Workflow 将多个工作流模版进行编排，以不同的顺序组合起来进行执行，即实际运行的任务。基于 Argo 本身提供的能力，我们还可以在 pipeline 中实现条件判断、循环、DAG 等多种复杂的能力。
-   Cron Workflow 顾名思义，以 cron 的方式运行 Workflow，非常适合我们想要长期运行某些测试任务的情况。 

下面我们看一个简单示例：

Copy

```fallback
spec:
  entrypoint: call-tipocket-bank
  arguments:
    parameters:
      - name: ns
        value: tipocket-bank
            - name: nemesis
        value: random_kill,kill_pd_leader_5min,partition_one,subcritical_skews,big_skews,shuffle-leader-scheduler,shuffle-region-scheduler,random-merge-scheduler
  templates:
    - name: call-tipocket-bank
      steps:
        - - name: call-wait-cluster
            templateRef:
              name: wait-cluster
              template: wait-cluster
        - - name: call-tipocket-bank
            templateRef:
              name: tipocket-bank
              template: tipocket-bank

```

上面的示例中是我们定义的 Bank 测试的 Workflow。示例中我们用到了 Workflow template 以及使用参数定义我们需要的故障注入，这样我们就可以重复使用模版，根据不同的测试场景来同时运行多个 Workflow。在 TiPocket 中我们的故障注入是使用 nemesis 参数定义，也就是说我们提供了大量的故障注入，当用户想要使用的时候，只需要设置对应的参数即可，当然用户可以自己拓展 TiPocket 去增加更多的故障注入。更多的 Workflow 以及模版的示例，可以在 [TiPocket](https://github.com/pingcap/tipocket/tree/master/argo/workflow) 的仓库中找到。使用 Argo 可以很好的处理各种复杂的逻辑，可以做到以写代码的方式去定义我们 Workflow，这对于开发者来说十分友好，这也是我们选择 Argo 的重要原因之一。

现在我们的混沌实验自动化跑起来了，这时候如果我们的结果不符合预期，我们该如何去定位我们的问题呢？幸运的是 TiDB 中会保存丰富的监控信息，但是 Log 也是必不可少的。因此我们需要一个更好的日志收集手段，让我们的系统具有更好的可观测性。

Loki 提高实验的可观测性 \[![](https://pingcap.com/images/svgs/link.svg)

## ]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#loki - 提高实验的可观测性](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#loki-提高实验的可观测性))

可观测性，在云原生中系统中是非常重要的一环。通常来说可观测性主要包含 Metrics（指标），Logging（日志）和 Tracing（追踪）。由于 TiPocket 中主要运行的 test case，都是针对于测试 TiDB 集群，常依靠 metrics 和日志就能够定位问题。

![](https://pingcap.com/images/svgs/loader-spinner.svg)

Metrics 不用多说，Prometheus 已经成为了在 Kubernetes 监控的事实标准。然而对于日志，却没有一个统一的答案。比如 elasticsearch，fluent-bit 以及 Kibana 的解决方案，尽管这一套系统运行良好，但是却会消耗比较多的资源，并且维护成本太高。最终我们放弃了 EFK 的方案，而是采用了 [Grafana](https://grafana.com/) 开源的 [Loki](https://github.com/grafana/loki) 项目来作为日志的解决方案。

Loki 采用了跟 Prometheus 一样的 label 系统，我们可以很轻松的将 Prometheus 的监控指标与对应 pod 的日志结合起来，并且使用类似的查询语言去查询。另外 Grafana 目前也已经支持了 Loki dashboard，所以只需要使用 Grafana 就同时展示监控指标和日志了，非常方便。另一方面，TiDB 自带的监控系统中也含有 Grafana 组件，这样我就可以直接复用此 Grafana。

看一下效果 \[![](https://pingcap.com/images/svgs/link.svg)

## ]([https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/# 看一下效果](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/#看一下效果))

上面介绍了这么多，最后让我们看一下在 TiPocket 中一个完整的混沌实验到底是什么样子的呢？

1.  创建 Argo Cron Workflow 任务，在这个 Cron Workflow 中定义待测试的集群，注入的故障，用来检查 TiDB 集群正确性的测试 Case，以及任务的执行时间等。在 Cron Workflow 在运行过程中有需要的话还支持实时查看 Case 的日志。

    ![](https://pingcap.com/images/svgs/loader-spinner.svg)
2.  集群内部通过 Prometheus-operator 运行了 Prometheus。在 Prometheus 中配置了针对 Argo workflow 的告警规则。如果任务失败，则会发送到 Alertmanager，再由 Alertmanager 发送到 Slack channel 通知结果。

    ![](https://pingcap.com/images/svgs/loader-spinner.svg)
3.  警报中包含了对应 Argo Workflow 的地址，在 Workflow 页面中我们可以直接点击链接跳转到 Grafana 查找集群监控及日志。此时就可以进入下图的日志 Dashboard 进行查询了。

    ![](https://pingcap.com/images/svgs/loader-spinner.svg)

    不过这个时候也由不太方便的地方。目前在 Grafana logs dashboard 中，没有办法设置日志查询的 step 参数。这个参数用来控制日志查询时的采样，并且为了控制查询的数量，它会随着你查询的总时间而自动调整。比如查询 1 分钟的日志，step 会自动配置成 1s；查询 1 天的日志，step 可能变成了 30s，在这个时候就会有部分日志展示不出来。所以一般推荐尽量加入多的过滤条件进行搜索，或者使用 Loki 的命令行工具 logcli 将所有日志下载下来再查询。
4.  如果测试 Case 正常结束，那么集群会正常清理，等待 Argo 调度下一次测试的执行。

**以上就是我们如何利用 Chaos Mesh 和一些开源项目打造自动化混沌测试平台的完整流程。如果你也对混沌工程感兴趣的话，欢迎一起参与 [TiPocket](https://github.com/pingcap/tipocket) 和 [Chaos Mesh](https://github.com/pingcap/chaos-mesh) !**

分享到微信

![](data:image/png;base64,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)

打开微信，使用 “扫一扫” 即可将网页分享至朋友圈。

#### **产品**

-   [TiDB](/docs-cn/v3.0/)
-   [TiSpark](/docs-cn/v3.0/reference/tispark/)
-   [TiDB 路线图](/docs-cn/v3.0/roadmap/)

#### **文档**

-   [快速入门](https://docs.pingcap.com/zh/tidb/v4.0/quick-start-with-tidb)
-   [最佳实践](/blog-cn/tidb-best-practice/)
-   [常见问题解答](/docs-cn/stable/faq/tidb/)
-   [TiDB 周边工具](/docs-cn/stable/reference/tools/user-guide/)
-   [版本发布说明](https://docs.pingcap.com/zh/tidb/dev/release-notes)

#### **资源**

-   [博客](/blog-cn/)
-   [GitHub](https://github.com/pingcap)
-   [TiDB in Action](https://book.tidb.io)
-   [PingCAP University](https://university.pingcap.com/)
-   [联合解决方案](/solutions/intel/)
-   [Ask TUG](https://asktug.com/)

#### **公司**

-   [关于我们](/about-cn/)
-   [招贤纳士](https://job.pingcap.com/)
-   [新闻报道](/about-cn/news/)
-   [隐私申明](/zh/privacy-policy/)

#### **联系我们**

-   [Twitter](https://twitter.com/PingCAP)
-   [LinkedIn](https://www.linkedin.com/company/pingcap/)
-   [Reddit](https://www.reddit.com/r/TiDB/)
-   [Google Group](https://groups.google.com/forum/#!forum/tidb-user)
-   [Stack Overflow](https://stackoverflow.com/questions/tagged/tidb)
-   [微信公众号](javascript:void(0))

    ![](https://pingcap.com/images/wechat-qrcode.jpg)

    微信扫一扫  
    微信 ID：pingcap2015

© 2020 北京平凯星辰科技发展有限公司

[English](/blog) [京 ICP 备 16046278 号 - 2](http://www.beian.miit.gov.cn/) 
 [https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/](https://pingcap.com/blog-cn/building-a-distributed-test-platform-based-on-chaos-mesh-and-argo/)
