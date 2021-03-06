# 数据仓库

## 数据仓库数据模型设计的先后次序

- 概念模型设计（业务模型）：界定系统边界；确定主要的主题域及其内容；
- 逻辑模型设计：维度建模方法（事实表、维度表），以星型和雪花型来组织数据；
- 物理模型设计：将数据仓库的逻辑模型物理化到数据库的过程。

## 关系模型 & 维度模型

- 关系建模：3NF 模型
- 维度模型：事实表、维度表、星型模型、雪花模型

ODS + 维度模型 + 宽表模型 = DW 模型

**设计原则**：业务内聚、源系统解藕、计算复用

**宽表物理设计结构**：基本属性、日行为汇总指标、周期行为汇总指标、历史累计属性和指标

## ETL

### 数据抽取

- 全量抽取
  - 数据量比较小，不易判断其数据发生变化，如关系表、维度表、配置表
- 增量抽取
  - 数据量大，节约抽取事件
  - 通过时间标识字段抽取增量，如 createtime, updatetime;
  - 根据上次抽取结束时记录的自增长 ID 抽取增量；
  - 通过分析数据库日志获取增量；
  - 通过与前一天数据的 Hash 比较；
  - 由源系统主动推送增量，如订单表、交易表

### 数据清洗

- 空值处理；
- 验证数据正确性
- 规范数据格式
- 数据转码
- 数据标准统一

### 数据转换和加载

- ODS (Operational Data Store)
- 数据转换：又称数据刷新，用 ODS 中的增量或全量数据来刷新 DW 中的表，DW 中的表基本按事先设计好的模型创建，如事实表、维度表、汇总表
- 数据加载：insert 数据到一张表

### ETL 过程中的元数据

- 源系统表的字段及其含义、源系统数据库的 IP、接口人、数据仓库表的字段及其含义；
- 源表和目的表的对应关系，一个任务对应的源表和目标表，任务之间的依赖关系；
- 任务每次执行情况，etc
