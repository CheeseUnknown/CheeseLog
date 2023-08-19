# **Logger**

日志系统的主体。

```python
from CheeseAPI import logger
```

## **`self.messageTemplate: str = '(%l) %t > %c'`**

消息模版，使用占位符替换内容：

| key | description |
| - | - |
| %l | 消息等级的key |
| %t | 时间模版 |
| %c | 消息内容 |

该模版是默认模版。

## **`self.styledMessageTemplate: str = '(<black>%l</black>) <black>%t</black> > %c'`**

消息样式模版，与`self.messageTemplate`相同，仅在`self.styled == True`时生效。

该模版是默认模版。

## **`self.timerTemplate: str = '%Y-%m-%d %H:%M:%S.%f'`**

使用`strftime`进行日期处理。

该模版是默认模版。

## **`self.levels: Dict[str, Level] = ...`**

更多的请查看[Level]('./Level.md')。

创建一个自定义的消息等级并打印：

```python
from CheeseLog import logger, Level

logger.levels['MY_LEVEL'] = Level(40, styledMessageTemplate = '(<green>%l</green>) <black>%t</black> > %c')
logger.default('MY_LEVEL', 'Hello World')
logger.destory()
```

## **`self.weightFilter: int = 0`**

权重过滤，优先级最高。

## **`self.levelFilter: Set[str] = set()`**

指定消息等级过滤，优先级其次。

## **`self.moduleFilter: Dict[str, int | Set[str]] = {}`**

指定模块的消息等级过滤，优先级最次。

```python
from CheeseLog import logger

# 两者只能选其一
# 指定模块的消息等级权重过滤
logger.moduleFilter['Xxx'] = 20
# 指定模块的指定消息等级过滤
logger.moduleFilter['Xxx'] = set([ 'DEBUG', 'WARNING' ])
```

## **`self.logger_weightFilter: int = 0`**

同`self.weightFilter`，在其之后进行日志过滤。

## **`self.logger_levelFilter: Set[str] = set([ 'LOADING' ])`**

同`self.levelFilter`，在其之后进行日志过滤。

## **`self.logger_moduleFilter: Dict[str, int | Set[str]] = {}`**

同`self.moduleFilter`，在其之后进行日志过滤。

## **`self.styled: bool = True`**

控制台是否打印样式。

## **`self.filePath: str | None = None`**

该值不为`None`时，尝试将消息输出到日志文件中。

## **`def destory(self)`**

当程序关闭时，有时会出现部分内容被遗漏的情况，请使用`destory()`等待数据处理完毕。
