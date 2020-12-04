# Git-ComdLine-REST
[Permalink](https://github.com/wolverinn/Waking-Up/blob/cc918c65743540ff7a249b147da288edb7fef5bc/Git-ComdLine-REST.md)

95 lines (83 sloc) 6.51 KB

-   [Git](#git)
    -   [Git 常用命令](#git-%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4)
    -   [Git 标签管理](#git-%E6%A0%87%E7%AD%BE%E7%AE%A1%E7%90%86)
    -   [Git 撤销与回滚](#git-%E6%92%A4%E9%94%80%E4%B8%8E%E5%9B%9E%E6%BB%9A)
    -   [Git 分支管理](#git-%E5%88%86%E6%94%AF%E7%AE%A1%E7%90%86)
-   [RESTful API](#restful-api)
-   [Linux 常用命令](#linux-%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4)
-   [参考](#%E5%8F%82%E8%80%83)

* * *

## Git

#### Git 常用命令

-   `git init`
-   `git clone`
-   `git remote add origin ***.git`
-   `git push -u origin master`
-   推送到远程仓库的 dev 分支：`git push origin dev`
-   `git log`
-   `git log --graph --pretty=oneline --abbrev-commit`
-   `git status`
-   `git diff`
-   `git add *`
-   `git commit -m "message"`
-   commit 之后又改了一个小 bug，但是又不想增加一个 commit，可以用：`git commit --amend --no-edit`，直接将改动添加到上一次的 commit 中
-   `git push`
-   `git pull`
-   `touch .gitignore`

#### Git 标签管理

-   首先切换到需要打标签的分支上，然后使用`git tag v1.0`就可以在当前 commit 打上 v1.0 的标签
-   `git tag v1.0 commitID` 对特定 commit 打标签
-   打标签时加上 message：`git tag -a <tagname> -m "message"`
-   `git tag` 查看所有标签
-   `git show [tagname]` 查看标签详细信息
-   `git push origin <tagname>`可以推送一个本地标签到远程仓库
-   `git push origin --tags`可以推送全部未推送过的本地标签
-   `git tag -d <tagname>`可以删除一个本地标签
-   `git push origin :refs/tags/<tagname>`可以删除一个远程标签（先从本地删除）

#### Git 撤销与回滚

-   **暂存区**：`git add`之后 commit 之前存在的区域；**工作区**：`git commit`之后存在的区域；**远程仓库**：`git push`之后；
-   作了修改，但还没`git add`，撤销到上一次提交：`git checkout -f -- filename`；`git checkout -f -- .`
-   作了修改，并且已经`git add`，但还没`git commit`：
    -   先将暂存区的修改撤销：`git reset HEAD filename`/`git reset HEAD`；此时修改只存在于工作区，变为了 "unstaged changes"；
    -   再利用上面的 checkout 命令从工作区撤销修改
-   `git add`之后，作了修改，想丢弃这次修改：`git checkout -f --filename`会回到最近一次`git add`
-   作了修改，并且已经`git commit`了，想撤销这次的修改：
    -   `git revert commitID`. 其实，`git revert`可以用来撤销任意一次的修改，不一定要是最近一次
    -   `git reset --hard commitID`/`git reset --hard HEAD^`（HEAD 表示当前版本，几个 ^ 表示倒数第几个版本，倒数第 100 个版本可以用 HEAD~100）；参数`--hard`：强制将暂存区和工作区都同步到指定的版本
    -   `git reset`和`git revert`的区别是：reset 是用来回滚的，将 HEAD 的指针指向了想要回滚的版本，作为最新的版本，而后面的版本也都没有了；而 revert 只是用来撤销某一次更改，对之后的更改并没有影响
    -   然后再用`git push -f`提交到远程仓库

#### Git 分支管理

-   创建分支: `git branch test`
-   切换分支: `git checkout test`
-   创建并切换分支：`git checkout -b test`
-   将 test 分支的更改合并到 master 分支：先在 test 分支上 commit、push，再：`git checkout master`; `git merge test`
-   如果合并时产生冲突：先手动解决冲突，再合并
-   删除分支：`git branch -d test`
-   `git stash`
    -   如果当前分支还有任务没有做完，也不想提交，但此时需要切换或者创建其它分支，就可以使用 stash 将当前分支的所有修改（包括暂存区）先储藏起来；然后就可以切换到其它分支
    -   在其它分支工作完成之后，首先切换回原来的分支，然后使用`git stash list`命令查看
    -   可以使用`git stash apply <stash number>`恢复之前储藏的工作现场，再使用`git stash drop <stash number>`删除掉储藏的内容
    -   也可以直接用`git stash pop`恢复并删除内容
-   如果在其它分支上做了一个修改（比如修复了一个 bug，这次修改有一个 commitID），想要将这次修改应用到当前分支上，可以使用：`git cherry-pick commitID`，可以复制一个特定的提交到当前分支

## RESTful API

REST 指 Representational State Transfer，可以翻译为 “表现层状态转化”

#### 主要思想

-   对网络上的所有资源，都有一个**统一资源标识符** URI(Uniform Resource Identifier)；
-   这些资源可以有多种表现形式，即 REST 中的 “表现层”Representation，比如，文本可以用 txt 格式表现，也可以用 HTML 格式、XML 格式、JSON 格式表现。URI 只代表资源的实体，不代表它的形式；
-   “无状态 (Stateless)” 思想：服务端不应该保存客户端状态，只需要处理当前的请求，不需了解请求的历史，客户端每一次请求中包含处理该请求所需的一切信息；
-   客户端使用 HTTP 协议中的 GET/POST/PUT/DELETE 方法对服务器的资源进行操作，即 REST 中的” 状态转化 “

#### 设计原则

-   URL 设计
    -   最好只使用名词，而使用 GET/POST/PUT/DELETE 方法的不同表示不同的操作；比如使用`POST /user`代替`/user/create`
    -   GET：获取资源；POST：新建 / 更新资源；PUT：更新资源；DELETE：删除资源；
    -   对于只支持 GET/POST 的客户端，使用`X-HTTP-Method-Override`属性，覆盖 POST 方法；
    -   避免多级 URL，比如使用`GET /authors/12?categories=2`代替`GET /authors/12/categories/2`；
    -   避免在 URI 中带上版本号。不同的版本，可以理解成同一种资源的不同表现形式，所以应该采用同一个 URI，版本号可以在 HTTP 请求头信息的 Accept 字段中进行区分
-   状态码：服务器应该返回尽可能精确的状态码，客户端只需查看状态码，就可以判断出发生了什么情况。见计算机网络部分 -- [HTTP 请求有哪些常见状态码？](https://github.com/wolverinn/Waking-Up/blob/master/Computer%20Network.md#HTTP%E8%AF%B7%E6%B1%82%E6%9C%89%E5%93%AA%E4%BA%9B%E5%B8%B8%E8%A7%81%E7%8A%B6%E6%80%81%E7%A0%81)
-   服务器回应：在响应中放上其它 API 的链接，方便用户寻找

## Linux 常用命令

### 参考

-   [Git 教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/896043488029600)
-   [RESTful API 最佳实践 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html)
-   [GitHub - jlevy/the-art-of-command-line: Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md) 
    [https://github.com/wolverinn/Waking-Up/blob/master/Git-ComdLine-REST.md](https://github.com/wolverinn/Waking-Up/blob/master/Git-ComdLine-REST.md)
