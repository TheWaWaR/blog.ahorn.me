---
layout: post
title: Jenkins 入门教程
---

# Jenkins 安装配置教程

本教程以 jenkins `**2.19**` 为例

## 安装 jenkins

* 安装 java
* 安装 jenkins, 直接看官方文档即可: https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins
* 启动 jenkins 并访问 http://localhost:8080/
  - 输入 `/var/lib/jenkins/secrets/initialAdminPassword` 文件中的密码
  - 点击安装推荐的插件列表
  - 创建管理员帐号

## 安装 jenkins 插件

进入: `Manage Jenkins > Manage Plugins > Available` 
 然后再搜索框中输入相应插件名字，安装完插件后记得重启 jenkins

* GitHub Pull Request Builder

## 配置插件

进入: `Manage Jenkins > Configure System` 

* GitHub Pull Request Builder
  - GitHub Auth > Credentials，点击 Add > Jenkins
  - Kind 选 Secret text，下面 Secret 的内容是 Github 中生成的 Access Token
  - Github 中进入 Settings > Personal access tokens > Generate new token, 选中 repo, admin:repo_hook
  - Credentials 添加完成后，点击 Test Credentials > 选中Test basic connection to GitHub > Connect to API


