# Django

## Django、Flask、Tornado 的对比

- Django: 大而全，它的 MTV 框架、自带的 ORM、admin 后台管理，自带的 sqlite 数据库和开发测试用的服务器，提高了开发效率；
- Flask: 轻量级，可扩展性强，核心基于 Werkzeug WSGI 工具和 jinja2 模板引擎；
- Tornado: 少而精，异步非阻塞，两大核心模块如下
  - iostream: 对非阻塞式的 socket 进行简单的封装；
  - ioloop: 对 I/O 多路复用的封装，它实现了一个单例。

## 什么是 WSGI?

WSGI, 描述 web server 如何与 web application 通信的一种规范。

WSGI 协议主要包括 server 和 application 两部分：

- WSGI server 负责从客户端接收请求，将 request 转发给 application, 将 application 返回的 response 返回给客户端；
- WSGI application 接收由 server 转发的 request，处理请求，并将处理结果返回给 server;
- application 中可以包括多个栈式的中间件 (middlewares)，这些中间件需要同时实现 server 和 application, 可以在 WSGI 服务器和 WSGI 应用之间起调节作用；对服务器来说，中间件扮演应用程序，对应用程序来说，中间件扮演服务器。

## 简述什么是 FBV 和 CBV?

- FBV (function base views) 基于函数的视图；CBV (class base views) 基于类的视图；
- 使用 FBV 模式，在 URL 匹配成功后，会直接执行对应的视图函数；使用 CBV 模式，在 URL 匹配成功后，会找到视图函数中对应的类，然后这个类回到请求头中找到对应的 Request Method;
- 用户发送 URL 请求，Django 会依次遍历路由映射表中的所有记录，一旦路由映射表其中的一条匹配成功，就执行视图函数中对应的函数名，这是 FBV 的执行流程；
- 当服务器使用 CBV 模式时，用户发给服务器的请求包括 URL 和 Method, 这两个信息都是字符串类型。服务器通过路由映射表匹配成功后会自动去找 dispatch 方法，然后 Django 会通过 dispatch 反射的方式找到类中对应的方法并执行。类中的方法执行完毕之后，会把客户端想要的数据返回给 dispatch 方法，由 dispatch 方法把数据返回给客户端。

## Django 请求的生命周期

![1](https://tva1.sinaimg.cn/large/008eGmZEly1gnu3r9imq8j30pg0tgaf7.jpg)

1. `request wsgi`: 请求封装后交给 `web` 框架 `Flask、Django`;
2. `request middleware` 中间件：对请求进行校验或在请求对象中添加其它相关数据，例如：`csrf、request.session`;
3. `url conf` 路由匹配：根据浏览器发送的不同 url 去匹配不同的视图函数；
4. `view` 视图函数：在视图函数中进行业务逻辑的处理，可能涉及到：`orm、templates => 渲染`；
5. `view middleware` 中间件：对响应的数据进行处理；
6. `response wsgi`: 将响应的内容发送给浏览器。

## Django Middlewares 中间件的作用和应用场景

中间件是介于 request 与 response 处理之间的一道处理过程，用于在全局范围内改变 Django 的输入和输出。

简单来说中间件是帮助我们在视图函数执行之前和执行之后都可以做一些额外的操作。

explames:

1. Django 项目中默认启动了 csrf 保护，每次请求时通过 csrf 中间件检查请求中是否有正确的 token 值；
2. 当用户在页面上发送请求时，通过自定义的认证中间件，判断用户是否已经登录，未登录就去登录；
3. 当有用户请求时，判断用户是否在白名单或者在黑名单；

内置的五个方法：

1. `process_request`: 请求进来时，权限认证；
2. `process_view`: 路由匹配之后，能够得到视图函数；
3. `process_exception`: 异常时执行；
4. `process_template_response`: 模板渲染时执行；
5. `process_response`: 请求有响应时执行。

## Django ORM 和 QuerySet

- O (object): 类和对象；
- R (Relation): 关系，关系数据库中的表格；
- M (Mapping): 映射。

Django ORM 框架的功能：

1. 建立模型类和表之间的对应关系，允许通过面向对象的方式来操作数据库；
2. 根据设计的模型类来生成数据库中的表格；
3. 通过方便的配置进行数据库的切换；
4. 缺点：性能损耗、过度封装、有一定学习成本。

## 使用 ORM 和原生 SQL 的优缺点
