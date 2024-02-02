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
logger.destroy()
```

## **`self.weightFilter: int = 0`**

权重过滤，优先级最高。

## **`self.levelFilter: Set[str] = set()`**

指定消息等级过滤，优先级其次。

## **`self.moduleFilter: Dict[str, int | Set[str]] = {}`**

指定模块的消息等级过滤，优先级再次。

```python
from CheeseLog import logger

# 两者只能选其一
# 指定模块的消息等级权重过滤
logger.moduleFilter['Xxx'] = 20
# 指定模块的指定消息等级过滤
logger.moduleFilter['Xxx'] = set([ 'DEBUG', 'WARNING' ])
```

## **`self.contentFilter: Set[re.Match] = set()`**

对匹配的内容进行过滤，优先级最低。

## **`self.logger_weightFilter: int = 0`**

同`self.weightFilter`，在其之后进行日志过滤。

## **`self.logger_levelFilter: Set[str] = set([ 'LOADING' ])`**

同`self.levelFilter`，在其之后进行日志过滤。

## **`self.logger_moduleFilter: Dict[str, int | Set[str]] = {}`**

同`self.moduleFilter`，在其之后进行日志过滤。

## **`self.logger_contentFilter: Set[re.Match] = set()`**

同`self.contentFilter`，在其之后进行日志过滤。

## **`self.styled: bool = True`**

控制台是否打印样式。

## **`self.filePath: str | None = None`**

该值不为`None`时，尝试将消息输出到日志文件中。

## **`def destroy(self)`**

在程序结束后若有未记录的日志信息，则会等待记录完毕。

## **`def default(self, level: str, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

默认的输出函数。如果使用的是自定义消息等级，请使用该函数手动输入等级。

- **refreshed**

    为`True`时会将当前行覆盖。

## **`def debug(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为DEBUG的输出函数。

## **`def info(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为INFO的输出函数。

## **`def starting(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为STARTING的输出函数。

## **`def ending(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为ENDING的输出函数。

## **`def warning(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为WARNING的输出函数。

## **`def danger(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为DANGER的输出函数。

## **`def websocket(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为WEBSOCKET的输出函数。

## **`def http(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为HTTP的输出函数。

## **`def loaded(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为LOADED的输出函数。

## **`def loading(self, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为LOADING的输出函数。

## **`def encode(self, message: str) -> str`**

当消息中有`'<'`和`'>'`字符时，容易与样式格式产生冲突。使用该函数对冲突部分进行加密，可以防止冲突。
