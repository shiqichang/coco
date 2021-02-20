# Vue.js

## 1. 什么是 MVVM?

MVVM, Model-View-ViewModel, 是一种设计思想。

Model 层代表数据模型，也可以在 Model 中定义数据的修改和操作的业务逻辑；View 代表 UI 组件，负责将数据模型转化为 UI 展示出来；ViewModel 是一个同步 View 和 Model 的对象。

## 2. 父组件向子组件传值的方法？

父组件传递的数据，子组件用 props 方法接收。

子组件通过两种方式接收：可以传递任何类型（数组、对象等）

- props: ['title', 'likes', 'isPublished', 'author']
- props: {title: String, likes: Number}

## 3. 子组件向父组件传值的方法？

子组件向父组件传值用 this.$emit(key, value).

父组件接收时需要在父组件中创建的子组件的标签中绑定 Key, 格式：@Key="方法名"，父组件声明这个方法，方法带参数，这个参数就是子组件传递的 Value.

## 4. Vuex 是什么？哪种功能场景使用它？

Vuex 是专门为 Vue.js 设计的状态管理模式，它采用集中式存储管理 Vue 应用中所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。

当项目庞大时使用它：

- 需要动态的注册响应式数据；
- 需要命名空间 namespace 管理组织数据；
- 希望通过插件，来更改记录；方便测试。

## 5. Vuex 有哪几种属性？

- state: 基本数据；
- getters: 从基本数据派生的数据；
- mutations: 提交更改数据的方法，同步；
- actions: 像一个装饰器，包裹 mutations, 使之异步；
- modules: 模块化 Vuex.

## 6. 如何让 CSS 只在当前组件中起作用？

当前组件的 < style> 标签修改为 < style scoped>

## 7. Vue 中常见的生命周期钩子函数

- beforeCreate: Vue 实例的挂载元素 $el 和数据对象 data 未定义，未初始化；
- created: Vue 实例的数据对象 data 有值了，$el 没有；
- beforeMount: Vue 实例的 $el 和 data 都初始化了，但还是虚拟的 dom 节点，具体的 data.filter 还未替换掉；
- mounted: Vue 实例挂载完成，data.filter 成功渲染；
- beforeUpdate: data 更新时触发；
- updated: data 更新时触发；
- beforeDestroy: 组件销毁时触发；
- destroyed: 组件销毁时触发，Vue 实例解除了事件监听和 dom 的绑定（无响应了），但 dom 节点依然存在。

## 8. Vue 生命周期总共有几个阶段？

- beforeCreate 创建前
- created 创建后
- beforeMount 载入前
- mounted 载入后
- beforeUpdate 更新前
- updated 更新后
- beforeDestroy 销毁前
- destroyed 销毁后

## 9. Vue 当中的指令及用法

- v-html: 渲染文本（能解析 HTML 标签）；
- v-text: 渲染文本（解析成文本）；
- v-bind: 绑定数据；
- v-once: 只绑定一次；
- v-model: 绑定模型；
- v-on: 绑定事件；
- v-if v-show: 条件渲染。

## 10. vue-cli 工程中常用的 npm 命令

- `npm install`: 下载 node_modules 资源包的命令；
- `npm run dev`: 启动 vue-cli 开发环境的 npm 命令；
- `npm run build`: vue-cli 生成生产环境部署资源的 npm 命令。

## 11. vue-cli 工程中每个文件夹和文件的用处

- build 文件夹：存放 webpack 的相关配置及脚本文件，偶尔用到 `webpack.base.conf.js`;
- config 文件夹：常用到此文件夹下的 config.js (index.js) 配置开发环境的端口号、是否开启热加载、设置生产环境的静态资源相对路径、是否开启 gzip 压缩、`npm run build` 打包生成静态资源的名称和路径等；
- node_modules 文件夹：存放 `npm install` 命令下载的开发环境和生产环境的各种依赖；
- src 文件夹：工程项目的源码及资源，包括页面图片、路由组件、路由配置、vuex、入口文件等；
- 其他文件：定义的一些项目信息、说明等。

## 12. vue-router 路由的两种模式
