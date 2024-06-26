<div align="center">
<br/>
<br/>
  <h1 align="center">
    GPro
  </h1>
  <h4 align="center">
    本 科 毕 业 设 计
  </h4>
</div>

* 题目：基于Vue的音频源分离系统的设计与实现

* 语言：Javascript、Python

* 技术栈：Vue、Node.js、Flask、深度学习、音频处理

Vue前端设计实现参考：https://github.com/maomao1996/Vue-mmPlayer

Node.js：下载网易云音乐 NodeJS 版 API，该份源码已经下架，可以在某些百度网盘获取源码。

demucs：该模型的功能是分离一首音乐中人声、背景和乐器声音，目前可以部署在本地运行，也可以下载 `demucs` 调用 .pth 文件，项目源于：https://github.com/facebookresearch/demucs

## 持续更新！！！

#### 功能实现 

* 播放音频【网易云音乐】

* 分离音频

* 分离音频可视化


#### Demo演示

在线播放的音频可视化

![1716885461944](image/README/1716885461944.png)

播放的音频以分离的轨道播放

![1716838713765](image/README/1716838713765.png)

#### 目前只是简单的文档演示，后续有机会补上。

## 使用说明

### 1、通过源码部署

Requirements

* 下载 `Node.js` 16.04版本

```bash 
pip install -U demucs
```
### 2、通过docker部署

## 配置说明


