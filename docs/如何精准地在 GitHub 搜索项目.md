# 如何精准地在 GitHub 搜索项目
小时候，我们遇到不会的字可以查新华字典，写作文也可以从作文书或文摘中找到合适的素材。现如今，写代码同样可以去 Github 上找适用的代码片段，甚至整个开源框架，不用重复造轮子的好处不言而喻。[![](https://camo.githubusercontent.com/b9a7a3da45bd5a69451fd2e3821b4eb198b8e900226a049198ba33eeefc889b0/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f38623362323439302d353836642d313165612d393032612d313135353138663736373833)
](https://camo.githubusercontent.com/b9a7a3da45bd5a69451fd2e3821b4eb198b8e900226a049198ba33eeefc889b0/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f38623362323439302d353836642d313165612d393032612d313135353138663736373833)

> 在 GitHub，您可以十分轻易地找到海量的开源代码。
>
> **查资源，学习优秀的框架，精准地在 GitHub 搜索项目是一种能力！**

今天主要分享一些检索上的技巧，能够帮助您更精确的找到需要的项目代码。

开始之前，有必要说一下几个常用词的含义：

```
watch：持续收到该项目的动态
fork：复制某个项目到自己的 Github 仓库中
star：可以理解为点赞
clone：将项目下载至本地
Issue：发现 bug，及时讨论
follow：关注你感兴趣的作者，会收到他们的动态
topic：主题

```

## GitHub 常用的搜索功能

**1. 关键字搜索**

例如：咱们需要找一个热门的 vue 框架

进入 GitHub 主页，直接使用关键字 vue 搜索。[![](https://camo.githubusercontent.com/649c2b5a81cb7afee9e559842ec32dcdc55cc0125bb5811165917def3ab10ce8/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f30363165363661302d356366352d313165612d383135352d396436643034383836643562)
](https://camo.githubusercontent.com/649c2b5a81cb7afee9e559842ec32dcdc55cc0125bb5811165917def3ab10ce8/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f30363165363661302d356366352d313165612d383135352d396436643034383836643562)  
本次共搜索到了 362257 个结果

不难看出，vue 是当前比较流行的前端框架

回到正题，搜索到的结果这么多，选哪个？

这个时候需要用到 github 过滤器

**2. Github 过滤器**

在 github 搜索结果面板上，可以通过代码仓库、代码、评论、语言、多种排序等方式进行二次筛选，精细化搜索，一步步缩小范围。 [![](https://camo.githubusercontent.com/2aad5f97c5a65b67cebc642c32e76e607ea766eb5afe03ed9baf7e1f4f9fb1b3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f34306661643163302d356433392d313165612d623761302d333936376665636439306434)
](https://camo.githubusercontent.com/2aad5f97c5a65b67cebc642c32e76e607ea766eb5afe03ed9baf7e1f4f9fb1b3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f34306661643163302d356433392d313165612d623761302d333936376665636439306434)  
例如：我们在语言栏选择 Vue，可以查看 Vue 语言的相关项目，结果更有针对性

**3. 多条件搜索**

大多数时候，上面两种方式还不能满足要求，可以用多条件组合搜索

例如：想要找 **评分高的基于 vue 开发的后台管理系统框架**

咱们可以在搜索框中搜索：

**vue 后台管理 stars:">1000"**

结果如下： [![](https://camo.githubusercontent.com/4086ab829cbc4098351e2418198fda6f3e3b6edb9f0d964c06477ebfbe6e730c/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f64313033356236302d356432362d313165612d383135352d396436643034383836643562)
](https://camo.githubusercontent.com/4086ab829cbc4098351e2418198fda6f3e3b6edb9f0d964c06477ebfbe6e730c/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f64313033356236302d356432362d313165612d383135352d396436643034383836643562)  
使用组合条件后，共查到 14 个项目

排名靠前的是当前比较热门的几个 vue 后台管理系统开源项目：

**vue-manage-system**、**vue2-manger**、**eladmin**

本次搜索，只是简单几步操作就找到了咱们需要的开源项目！

**注意：**

-   搜索语句不能有特殊字符，如： . , : ; /\\ \` ’ ” = \* ! ? # $ & + ^ | ~ &lt;> () {} \[]
-   搜索语法可以参考 Github 官方文档 [![](https://camo.githubusercontent.com/a9e19805fd83b14878b94312344a6197a6c06a365730239e08118f995d94f147/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f62623131653333302d356432622d313165612d393437332d616466376462303364616536)
    ](https://camo.githubusercontent.com/a9e19805fd83b14878b94312344a6197a6c06a365730239e08118f995d94f147/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f62623131653333302d356432622d313165612d393437332d616466376462303364616536)  
    地址：[https://help.github.com/cn/github/searching-for-information-on-github/understanding-the-search-syntax](https://help.github.com/cn/github/searching-for-information-on-github/understanding-the-search-syntax)

    **4. 傻瓜式搜索**

多条件搜索是方便快捷，但是搜索条件不但语法麻烦，而且容易忘

有没有更简便的方法？当然！

github 提供可视化高级搜索页面，这里我称之为 “**傻瓜式搜索**”

直接访问地址：[https://github.com/search/advanced](https://github.com/search/advanced) [![](https://camo.githubusercontent.com/551aae142748b57d586c0d440b13421f25a1fc3244d9601e61433d8103f289a3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f35356131336365302d356366332d313165612d396364352d383936376634373632393332)
](https://camo.githubusercontent.com/551aae142748b57d586c0d440b13421f25a1fc3244d9601e61433d8103f289a3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f35356131336365302d356366332d313165612d396364352d383936376634373632393332)  
你也可以在语言栏下面点击 “Advanced search”，进入 [![](https://camo.githubusercontent.com/689bfd88e7d811116a4745848b4697787a69045b3f1131f0a8d111b850eee798/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f65653162343738302d356433302d313165612d613866342d376234373432353131663366)
](https://camo.githubusercontent.com/689bfd88e7d811116a4745848b4697787a69045b3f1131f0a8d111b850eee798/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f65653162343738302d356433302d313165612d613866342d376234373432353131663366)  
“**傻瓜式搜索**” 不需要您记住复杂的条件和语法，操作简便！

只需要在可视化搜索面板输入过滤条件，github 会自动帮咱们把这些复杂的查询条件拼接搜索框中，然后显示查询结果。

哈哈，够傻瓜吧？

**5. github 搜索帮助**

github 提供了详细的帮助文档，咱们可以在上面学习搜索技巧，提高搜索的精准度。 [![](https://camo.githubusercontent.com/b46b0e621c89f33794254d25357b21684a2ee0e91d7af5dc811ef651f11f4c5a/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f66623438373665302d356366332d313165612d396364352d383936376634373632393332)
](https://camo.githubusercontent.com/b46b0e621c89f33794254d25357b21684a2ee0e91d7af5dc811ef651f11f4c5a/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f66623438373665302d356366332d313165612d396364352d383936376634373632393332)  
地址： [https://help.github.com/en/github/searching-for-information-on-github](https://help.github.com/en/github/searching-for-information-on-github)

## 你不知道的 GitHub 敏捷搜索秘籍

前面讲到的是主要是一些搜索方法

按照拿来即用的原则

我总结了平常用得最多的 **GitHub 敏捷搜索小秘籍**

大家可以收藏起来，方便下次使用！

还是以 vue 为例：

1.  搜索仓库名称包含 vue 关键字的所有项目

    **in:name vue**
2.  搜索描述中包含 vue 关键字的项目

    **in:description vue**
3.  搜索 readme 文件中包含 vue 关键字的项目

    **in:readme vue**
4.  搜索 vue 关键字项目中，关注超过 100 个的项目

    **star:>100 vue**
5.  搜索 fork 超过 100 的 vue 项目

    **fork:>100 vue**
6.  搜索 2 月 4 日后创建的 vue 项目

    **create:>2020-02-04 vue**
7.  搜索 2 月 4 日后还有更新的 vue 项目

    **pushed:>2020-02-04 vue**
8.  搜索开发者是 lin-xin，开发语言是 vue 的项目

    **user:lin-xin language:vue**

## 如何让自己的项目在 GitHub 上加星

想要在 GitHub 上创建有价值的项目，或者通俗地讲 “**打造 GitHub 千星项目**” ，首先要创建一个你认为对别人有帮助的东西，找到自己的问题并解决它，也许别人也和你一样面临着同样的问题，专注于创造有价值的内容，流量只是附带的而已。

建议从以下几个方面入手：

-   选好项目
-   做好阅读和调研
-   建好项目仓库
-   写好 Readme
-   配上好图
-   注重反馈回路
-   社区交流是关键

## Octotree Chrome 插件的使用

Octotree Chrome 插件能够帮助咱们在查看 github 项目时，清晰明了的看到项目的结构以及具体代码，使下载代码更具有目的性，减少不必要代码的下载，从而大大提升开发效率。

效果图：（**安装插件前**） [![](https://camo.githubusercontent.com/a52f1c8abeea942e3f3e30c96d51d1c17caf4c5771741b5a7eb3f8ff328b7df1/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f61616462663262302d353936642d313165612d393032612d313135353138663736373833)
](https://camo.githubusercontent.com/a52f1c8abeea942e3f3e30c96d51d1c17caf4c5771741b5a7eb3f8ff328b7df1/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f61616462663262302d353936642d313165612d393032612d313135353138663736373833)  
效果图：（**安装插件后**） [![](https://camo.githubusercontent.com/8c19d1e5ec9a2ee038069d748c0b63920dbcbe51d5eeb922b79558f52de31166/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f63303664333033302d353936642d313165612d613866342d376234373432353131663366)
](https://camo.githubusercontent.com/8c19d1e5ec9a2ee038069d748c0b63920dbcbe51d5eeb922b79558f52de31166/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f63303664333033302d353936642d313165612d613866342d376234373432353131663366)  
**安装步骤：**

-   下载 octotree Chrome 插件

    地址：[http://www.cnplugins.com/devtool/octotree/download.html](http://www.cnplugins.com/devtool/octotree/download.html)
-   打开 chrome 浏览器进入软件界面够，我们在搜索栏中输入 chrome：//extensions，然后在左侧的功能中选择 “扩展程序”。
-   直接拖动我们已经下载的 octotree chrome 插件至扩展程序界面。
-   随即弹出 “要添加 octotree 吗”，用户点击 “添加扩展程序” 按钮即可进行添加。
-   添加成功以后打开 github，在项目左上侧有一个三角收缩符号，点击三角符号，即可看到项目结构图以及具体代码。 [![](https://camo.githubusercontent.com/913244d5274be50fdd92830df8182c766ee75117d2aae3b162f3428d3d2ef437/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f34663832666163302d353936652d313165612d386362622d353365626661613732653630)
    ](https://camo.githubusercontent.com/913244d5274be50fdd92830df8182c766ee75117d2aae3b162f3428d3d2ef437/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f34663832666163302d353936652d313165612d386362622d353365626661613732653630)

## 附一、GitHub 上优质的开源项目

GitHub 平台上面有很多优秀且值得学习的开源项目，这里总结了比较热门的几个开源项目：

-   [**free-programming-books**](https://github.com/justjavac/free-programming-books-zh_CN)

    简介：整理了很多和编程相关的免费书籍，同时也有中文版项目。

    地址：[https://github.com/justjavac/free-programming-books-zh_CN](https://github.com/justjavac/free-programming-books-zh_CN) [![](https://camo.githubusercontent.com/a8ec8dcae1374d9ad6f61254b3b6a115eff0f4745ba75df29727c6d11b91f427/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f37643538346564302d353937302d313165612d393032612d313135353138663736373833)
    ](https://camo.githubusercontent.com/a8ec8dcae1374d9ad6f61254b3b6a115eff0f4745ba75df29727c6d11b91f427/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f37643538346564302d353937302d313165612d393032612d313135353138663736373833)
-   [**github-cheat-sheet**](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md)

    简介：整理了 GitHub 使用的各种技巧

    地址：[https://github.com/tiimgreen/github-cheat-sheet](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.zh-cn.md) [![](https://camo.githubusercontent.com/8276e391cd28cd7ef6c6de22f69a6019cf81dc1f001f354edba8fb9a600a5ab3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f61623837393461302d353937302d313165612d393032612d313135353138663736373833)
    ](https://camo.githubusercontent.com/8276e391cd28cd7ef6c6de22f69a6019cf81dc1f001f354edba8fb9a600a5ab3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f61623837393461302d353937302d313165612d393032612d313135353138663736373833)
-   [android-open-project](https://github.com/Trinea/android-open-project)

    简介：涵盖 Android 开发的优秀开源项目。

    地址：[https://github.com/Trinea/android-open-project](https://github.com/Trinea/android-open-project)[![](https://camo.githubusercontent.com/0f5b3a3fb261fd038db578cc7b0796476e5f66fd4f6ba33f73fe01d11b6047e3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f64353138323530302d353937302d313165612d393362352d333939336439656162363165)
    ](https://camo.githubusercontent.com/0f5b3a3fb261fd038db578cc7b0796476e5f66fd4f6ba33f73fe01d11b6047e3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f64353138323530302d353937302d313165612d393362352d333939336439656162363165)
-   [**chinese-independent-developer**](https://github.com/1c7/chinese-independent-developer)

    简介：聚合所有中国独立开发者的项目

    地址：[https://github.com/1c7/chinese-independent-developer](https://github.com/1c7/chinese-independent-developer) [![](https://camo.githubusercontent.com/70839a85a5d9eb7b02ce03fcc72698e2836dec8dcdf0d69fdf0b58c6ff0f16d3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f31303437383330302d353937312d313165612d386362622d353365626661613732653630)
    ](https://camo.githubusercontent.com/70839a85a5d9eb7b02ce03fcc72698e2836dec8dcdf0d69fdf0b58c6ff0f16d3/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f31303437383330302d353937312d313165612d386362622d353365626661613732653630)
-   [**芋道源码**](https://github.com/YunaiV/Blog)

    简介：程序员博客，每周一篇，内容精简，不咸不淡，期盼探讨。

    推荐指数：AAAAA

    地址：[https://github.com/YunaiV/Blog](https://github.com/YunaiV/Blog) [![](https://camo.githubusercontent.com/a7d2e42ad20c0ed8fab5d6a1f94eb8ca75451ada3c759e18f124fb235e11f64b/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f31353761343561302d353937322d313165612d613639352d386634633037396230333664)
    ](https://camo.githubusercontent.com/a7d2e42ad20c0ed8fab5d6a1f94eb8ca75451ada3c759e18f124fb235e11f64b/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f31353761343561302d353937322d313165612d613639352d386634633037396230333664)  
    [![](https://camo.githubusercontent.com/f22f058d82a03403efb4ca952c0e0904e1126991423b0ab89a394d4636dfd891/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f61356561323166302d353937322d313165612d386362622d353365626661613732653630)
    ](https://camo.githubusercontent.com/f22f058d82a03403efb4ca952c0e0904e1126991423b0ab89a394d4636dfd891/68747470733a2f2f696d616765732e676974626f6f6b2e636e2f61356561323166302d353937322d313165612d386362622d353365626661613732653630)

## 附二、GitHub 上值得前端学习的开源实战项目

**Vue.js**

• [vue-element-admin 是一个后台前端解决方案，它基于和 element-ui 实现](https://panjiachen.github.io/vue-element-admin)

• [基于 iView 的 Vue 2.0 管理系统模板](https://github.com/iview/iview-admin)

• [基于 vue2 + vuex 构建一个具有 45 个页面的大型单页面应用](https://github.com/bailicangdu/vue2-elm)

• [基于 vue + element-ui 的后台管理系统](https://github.com/bailicangdu/vue2-manage)

• [基于 Vue.js + Element UI 的后台管理系统解决方案](https://github.com/lin-xin/vue-manage-system)

• [基于 Vue (2.5) + vuex + vue-router + vue-axios +better-scroll + Scss + ES6 等开发一款移动端音乐 WebApp](https://github.com/caijinyc/vue-music-webapp)

• [Spring Boot 后端 + Vue 管理员前端 + 微信小程序用户前端 + Vue 用户移动端](https://github.com/linlinjava/litemall)

• [高仿网易云音乐的 webapp，只实现了 APP 的核心功能](https://github.com/javaSwing/NeteaseCloudWebApp)

• [Vue + TypeScript + Element-Ui 支持 markdown 渲染的博客前台展示](https://github.com/biaochenxuying/blog-vue-typescript)

• [更多…](https://github.com/opendigg/awesome-github-vue)

**React.js**

• [一套优秀的中后台前端解决方案](https://github.com/zuiidea/antd-admin)

• [网易云音乐第三方](https://github.com/trazyn/ieaseMusic)

• [一个 react + redux 的完整项目 和 个人总结](https://github.com/bailicangdu/react-pxq)

• [react 后台管理系统解决方案](https://github.com/yezihaohao/react-admin)

• [这是一个用来查看 GitHub 最受欢迎与最热项目的 App, 它基于 React Native 支持 Android 和 iOS 双平台](https://github.com/crazycodeboy/GitHubPopular)

• [RN 写的饿了么，还原度相当高，实现了各类动效](https://github.com/stoneWeb/elm-react-native)

• [仿知乎日报](https://github.com/race604/ZhiHuDaily-React-Native)

• [一个商城类的 RN 项目](https://github.com/bigsui/shopping-react-native)

• [react + Ant Design + 支持 markdown 的博客前台展示](https://github.com/biaochenxuying/blog-react)

• [基于 pro.ant.design 的 react + Ant Design 的博客管理后台项目](https://github.com/biaochenxuying/blog-react-admin)

• [使用 react hooks + koa2 + sequelize + mysql 搭建的前后台的博客](https://github.com/gershonv/react-blog)

• [基于 typescript koa2 react 的个人博客](https://github.com/fxy5869571/blog-react)

• [更多…](https://github.com/MarnoDev/react-native-open-project)

**Angular**

• [基于 angular.js,weui 和 node.js 重写的新闻客户端](https://github.com/windiest/Angular-news)

• [管理仪表板模板基于 Angular 7+，Bootstrap 4](https://github.com/akveo/ngx-admin)

**Node.js**

• [基于 node.js + Mongodb 构建的后台系统](https://github.com/bailicangdu/node-elm)

• [Nodeclub 是使用 Node.js 和 MongoDB 开发的社区系统](https://github.com/cnodejs/nodeclub)

• [基于 Node.js+MySQL 开发的开源微信小程序商城（微信小程序）](https://github.com/tumobi/nideshop-mini-program)

• [NideShop 开源微信小程序商城服务端 API（Node.js + ThinkJS）](https://github.com/tumobi/nideshop)

• [基于 react, node.js, go 开发的微商城（含微信小程序）](https://github.com/shen100/wemall)

• [React+Express+Mongo -> 前后端博客网站](https://github.com/Nealyang/React-Express-Blog-Demo)

• [基于 node + express + mongodb 的博客网站后台](https://github.com/biaochenxuying/blog-node)

> 坚持总结工作中遇到的技术问题，坚持记录工作中所思所见，欢迎大家一起探讨交流。

\-End-  
[https://gitbook.cn/books/5e60cb541a60a95634d16e4b/index.html](https://gitbook.cn/books/5e60cb541a60a95634d16e4b/index.html) 
 [https://github.com/WadeStack/test/issues/12](https://github.com/WadeStack/test/issues/12)
