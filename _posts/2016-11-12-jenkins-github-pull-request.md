---
layout: post
title: Jenkins 入门教程
---

# Jenkins 安装配置

本教程以 jenkins `2.19` 为例

## 安装 jenkins

* 安装 java
* 安装 jenkins, 直接看 [官方文档][jenkins-install] 即可: 
* 启动 jenkins 并访问 http://localhost:8080/
  - 输入 `/var/lib/jenkins/secrets/initialAdminPassword` 文件中的密码
  - 点击安装推荐的插件列表
  - 创建管理员帐号

## 安装 jenkins 插件

进入: `Manage Jenkins > Manage Plugins > Available` 
 然后再搜索框中输入相应插件名字，安装完插件后记得重启 jenkins

* [GitHub Pull Request Builder][plugin-pr]

## 配置插件

进入: `Manage Jenkins > Configure System` 

* GitHub Pull Request Builder
  - GitHub Auth > Credentials，点击 Add > Jenkins
  - Kind 选 Secret text，下面 Secret 的内容是 Github 中生成的 Access Token
  - Github 中进入 Settings > Personal access tokens > Generate new token, 选中 repo, admin:repo_hook
  - Credentials 添加完成后，点击 Test Credentials > 选中Test basic connection to GitHub > Connect to API

# Jenkins 使用

## 添加一个自动 build Pull Request 的 job

![build 状态][build-status]

### 功能

* 对应项目提交 Pull Request 通过 github webhook 自动触发 build
* build 完后会在对应的 Pull Request 中显示 build 状态

### 配置步骤

* New Item > 输入 job 名字 > 中 Freestyle project
*  General
  - 选中 Github project > 填入 Project url
* Source Code Management
  - 选中 Git 
  - 填入项目 git repo 地址, 例如: https://github.com/emqtt/emqttd.git
* Build Triggers
  - 选中 GitHub Pull Request Builder
  - 选择刚刚添加的 GitHub API credentials
  - Admin list 中填入相应的用户名 (只有在这个列表中的用户提的 Pull Request 才会触发 build, 因为 build 允许运行任意脚本，是很危险的)
  - 选中 Use github hooks for build triggering
* Build
  - 点击 Add build step > Execute shell
  - 输入 build 用的 shell 命令，比如 make build
* 点击保存，保存之后 Jenkins 会自动生成一条对应项目的 Webhook, 这样这个项目一旦有 PR 就能及时通知到 Jenkins 触发 build 操作


[build-status]: http://7te9fl.com1.z0.glb.clouddn.com/build-status.png
[jenkins-install]: https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins
[plugin-pr]: https://wiki.jenkins-ci.org/display/JENKINS/GitHub+pull+request+builder+plugin