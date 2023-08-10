# **消息实例**

## **`class Logger(threading.Thread)`**

日志类。

- **`self.filePath: Optional[str] = None`**

    若要输出日志文件，请为该值设置一个有效的文件路径，例如`./myLog.log`。

- **`self.messageTemplate: str = '(%level) %timer > %content'`**

    消息模版使用日期的匹配词，并有几个自定义的匹配词：

    | 匹配词 | 匹配内容 |
    | - | - |
    | %level | 消息等级 |
    | %content | 消息内容 |
    | %timer | 日期模版 |

- **`self.timerTemplate: str = '%Y-%m-%d %H:%M:%S.%f'`**

- **`self.filter: NonNegativeInt | set[str] = []`**

    过滤消息。

    当该值为`set`时，会对其中符合等级的消息进行过滤。

    当该值为`NonNegativeInt`时，会过滤等级权重小于该值的消息。

- **`self.levels: dict[str, Level] = ...`**

    该日志所有的所有消息等级。

- **`self.colorful: bool = True`**

    是否在控制台输出色彩。

    其会对消息内容中的数字以及路径进行可能性的查找，并自动修改样式。

## **默认实例**

默认的日志实例其实是由日志类初始化的，你可以直接获取。

```python
from CheeseLog import logger
```

## **更多实例**

该功能是开发的附属功能，更多的日志实例可能并没有什么卵用...

```python
from CheeseLog import Logger, debug

myLogger = Logger()

debug('Hello World!', logger = myLogger) # [DEBUG] > 2023-07-26 15-47-09-250318 > Hello World!
```
