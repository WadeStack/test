# MkDocs: 构建你自己的知识库
## 1. 介绍

> [github](https://github.com/mkdocs/mkdocs)
>
> [homepage](https://www.mkdocs.org/)
>
> [MkDocs 中文文档](https://mkdocs.zimoapps.com/)

MkDocs 是一个快速、简单、华丽的静态网站生成器，适用于构建项目文档。文档源文件以 Markdown 编写，并使用一个 YAML 文件来进行配置。 MkDocs 生成完全静态的 HTML 网站，你可以将其部署到 GitHub pages、Amzzon S3 或你自己选择的其它任意地方。

MkDocs 有一堆很好看的主题。 官方内置了两个主题： mkdocs 和 readthedocs， 也可以从 MkDocs wiki 中选择第三方主题， 或者自定义主题。

支持实时预览你的网站：当你编辑 Md 文件时，内置的开发服务可以帮助你预览显示效果。当文档有改动时，甚至还可以自动载入并刷新你的浏览器。

运行：

```null
mkdocs serve
```

## 2. 文件布局

> [docs](https://www.mkdocs.org/user-guide/writing-your-docs/)

您的文档来源应作为常规的 Markdown 文件编写（请参见 下面的 “使用 Markdown 编写”），并将其放置在 document 目录中。默认情况下，此目录将被命名 docs，并将位于 mkdocs.yml 配置文件旁边项目的顶层。

您可以创建的最简单的项目如下所示：

```null
mkdocs.yml
docs/
    index.md
```

按照约定，应为您的项目主页命名 index.md（有关详细信息，请参见下面的索引页面）。以下任何文件扩展名可用于您的 Markdown 源文件：markdown,mdown,mkdn,mkd,md。无论任何设置如何，文档目录中包括的所有 Markdown 文件都将在内置站点中呈现。

您还可以将 Markdown 文件包括在嵌套目录中。

```null
docs/
    index.md
    user-guide/getting-started.md
    user-guide/configuration-options.md
    license.md
```

## 3. 索引页: index.md

默认情况下，请求目录时，大多数 Web 服务器将返回 index.html 该目录中包含的索引文件（通常名为）（如果存在）。因此，上面所有示例中的首页都被命名为 index.md，MkDocs 将 index.html 在构建网站时将其呈现到该首页。

许多资源库托管站点在浏览目录内容时通过显示 README 文件的内容来提供对 README 文件的特殊处理。因此，MkDocs 将允许您将索引页命名为 README.md 而不是 index.md。这样，当用户浏览您的源代码时，资源库主机可以显示该目录的索引页，因为它是 README 文件。但是，当 MkDocs 渲染您的站点时，该文件将被重命名为，index.html 以便服务器将其用作适当的索引文件。

如果在同一目录中找到一个 index.md 文件和一个 README.md 文件，则 index.md 使用该 README.md 文件，而忽略该文件。

## 4. 配置页面和导航

文件中的 `nav` 或 `pages` 定义了全局站点导航菜单中包含的页面以及该菜单的结构。如果未提供，则将通过发现文档目录中的所有 Markdown 文件来自动创建导航。自动创建的导航配置将始终按文件名的字母数字顺序进行排序（除非索引文件始终始终在子部分中列出）。如果您希望导航菜单的排序方式不同，则需要手动定义导航配置。

```null
nav:
    - Home: 'index.md'
    - 'User Guide':
        - 'Writing your docs': 'writing-your-docs.md'
        - 'Styling your docs': 'styling-your-docs.md'
    - About:
        - 'License': 'license.md'
        - 'Release Notes': 'release-notes.md'
```

## 5. 主题

> [homepage](https://www.mkdocs.org/user-guide/configuration/#theme)

Sets the theme and theme specific configuration of your documentation site. May be either a string or a set of key/value pairs.

If a string, it must be the string name of a known installed theme. For a list of available themes visit styling your docs.

An example set of key/value pairs might look something like this:

```null
theme:
    name: mkdocs
    custom_dir: my_theme_customizations/
    static_templates:
        - sitemap.html
    include_sidebar: false
```

## 6. Configuration: 全部配置项

> [homepage](https://www.mkdocs.org/user-guide/configuration/)

## 7. 插件

> [homepage](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins)

### 7.1. Search

A search plugin is provided by default with MkDocs which uses lunr.js as a search engine. The following config options are available to alter the behavior of the search plugin:

separator 默认值: `'[\s\-]+'`

A regular expression which matches the characters used as word separators when building the index. By default whitespace and the hyphen (-) are used. To add the dot (.) as a word separator you might do this:

```null
plugins:
    - search:
        separator: '[\s\-\.]+'
```

### 7.2. mkdocs-localsearch

> [gihub](https://github.com/wilhelmer/mkdocs-localsearch)

注意：此插件仅适用于 Material for MkDocs 主题（且 mkdocs_material 版本要求 >=5.0）。如果您需要其他主题的支持，请随时创建请求请求。

### 7.3. awesome-pages-plugin: 简化页面顺序配置

> [github](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)

#### 7.3.1. 安装

Install the package with pip:

```null
pip install mkdocs-awesome-pages-plugin
```

Enable the plugin in your mkdocs.yml:

```null
plugins:
    - search
    - awesome-pages
```

#### 7.3.2. 自定义导航

Create a YAML file named .pages in a directory and use the nav attribute to customize the navigation on that level. List the files and subdirectories in the order that they should appear in the navigation.

```null
nav:
    - subdirectory
    - page1.md
    - page2.md
```

#### 7.3.3. Rest（剩余页面）

```null
nav:
    - introduction.md
    - ...
    - summary.md
```

#### 7.3.4. Titles

```null
nav:
    - ...
    - First page: page1.md
```

#### 7.3.5. Links

```null
nav:
    - ...
    - Link Title: https://lukasgeiter.com
```

#### 7.3.6. 修改排序

可单独在子目录中创建 `.pages` 文件并如下配置：

```null
order: desc
```

#### 7.3.7. 隐藏子目录

可单独在子目录中创建 `.pages` 文件并如下配置：

```null
hide: true
```

#### 7.3.8. 设置目录标题

可单独在子目录中创建 `.pages` 文件并如下配置：

```null
title: Page Title
```

#### 7.3.9. 折叠子目录

例如，如果您具有以下文件结构：

```null
文档/
├─SECTION1 /
│ ├─IMG /
│ │ ├─image1.png
│ │ └─image2.png
│ └─index.md ＃第一节
└─SECTION2 /
  └─index.md ＃第2节
```

这些页面将在根目录中显示在导航中：

-   第一节
-   第二节

而不是 MkDocs 默认显示它们的方式：

-   第一节
    -   指数
-   第二节
    -   指数

配置方式

-   For all pages

    Collapsing can be enabled globally using the `collapse_single_pages` option in `mkdocs.yml` .
-   For a sub-section

    如下配置，将**递归**影响子目录：

    ```null
    collapse_single_pages: true
    ```
-   For a single page

    如果要启用或禁用单个页面的折叠而不进行递归应用设置，在目录中创建一个名为 `.pages` 的 YAML 文件，并将其设置 collapse 为 true 或 false：

    ```null
    collapse: true
    ```

## 8. 生成静态页面

首先生成文档：

```null
mkdocs build
```

这将创建一个名为 site 的新目录。 看一下该目录的情况：

```null
$ ls site
about  fonts  index.html  license  search.html
css    img    js          mkdocs   sitemap.xml
```

请注意，你的源文档已输出为两个名为 `index.html` 和 `about/index.html` 的 HTML 文件。同时各种其他媒体文件也已被复制到 site 目录中作为文档主题的一部分。另外还有一个 sitemap.xml 文件和 mkdocs/search_index.json。

如果你正在使用版本控制软件，例如 git，你可能不希望将生成的文件包含到存储库中。只需要在. gitignore 文件中添加一行 site / 即可。

```null
echo "site/" >> .gitignore
```

如果你正在使用其他版本控制工具，请你自行查阅相关文档，了解如何忽略特定目录。

一段时间后，文件可能会从文档中删除，但它们仍将驻留在 site 目录中。 要删除那些陈旧的文件，只需在运行 mkdocs 命令时带上 --clean 参数即可。

```null
mkdocs build --clean
```

## 9. 部署

刚刚生成的文档站点仅使用静态文件，因此你几乎可以在任何地方托管它。`GitHub project pages` 和 `Amazon S3` 是个很不错的托管地方，具体取决于你的需求。将整个 site 目录的内容上传到你托管网站的地方，然后就完成了。 
 [https://www.cnblogs.com/brt2/p/13950073.html#733-rest%EF%BC%88%E5%89%A9%E4%BD%99%E9%A1%B5%E9%9D%A2%EF%BC%89](https://www.cnblogs.com/brt2/p/13950073.html#733-rest%EF%BC%88%E5%89%A9%E4%BD%99%E9%A1%B5%E9%9D%A2%EF%BC%89)
