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
