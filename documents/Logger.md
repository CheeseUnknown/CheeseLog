# **Logger**

日志系统的主体。

```python
from CheeseAPI import logger
```

## **`logger.messageTemplate: str = '(%l) %t > %c'`**

消息模版，使用占位符替换内容：

| key | description |
| - | - |
| %l | 消息等级的key |
| %t | 时间模版 |
| %c | 消息内容 |

该模版是默认模版。

## **`logger.styledMessageTemplate: str = '(<black>%l</black>) <black>%t</black> > %c'`**

消息样式模版，与`logger.messageTemplate`相同。仅在`logger.styled == True`时生效。

该模版是默认模版。

## **`logger.timerTemplate: str = '%Y-%m-%d %H:%M:%S.%f'`**

使用`strftime`进行日期处理。

该模版是默认模版。

## **`logger.levels: Dict[str, Level] = ...`**

【只读】 创建一个自定义的消息等级并打印：

```python
from CheeseLog import logger, Level

logger.levels['MY_LEVEL'] = Level(40, styledMessageTemplate = '(<green>%l</green>) <black>%t</black> > %c')
logger.default('MY_LEVEL', 'Hello World')
```

更多的请查看[Level]('./Level.md')。

## **`logger.weightFilter: int = 0`**

权重过滤，优先级最高。

## **`logger.levelFilter: Set[str] = set()`**

指定消息等级过滤，优先级其次。

## **`logger.moduleFilter: Dict[str, int | Set[str]] = {}`**

指定模块的消息等级过滤，优先级再次。

```python
from CheeseLog import logger

# 两者只能选其一
# 指定模块的消息等级权重过滤
logger.moduleFilter['Xxx'] = 20
# 指定模块的指定消息等级过滤
logger.moduleFilter['Xxx'] = set([ 'DEBUG', 'WARNING' ])
```

## **`logger.contentFilter: Set[str] = set()`**

对匹配的内容进行过滤，优先级最低。

## **`logger.logger_weightFilter: int = 0`**

同`logger.weightFilter`，在其之后进行日志过滤。

## **`logger.logger_levelFilter: Set[str] = set([ 'LOADING' ])`**

同`logger.levelFilter`，在其之后进行日志过滤。

## **`logger.logger_moduleFilter: Dict[str, int | Set[str]] = {}`**

同`logger.moduleFilter`，在其之后进行日志过滤。

## **`logger.logger_contentFilter: Set[str] = set()`**

同`logger.contentFilter`，在其之后进行日志过滤。

## **`logger.styled: bool = True`**

控制台是否打印样式。

## **`logger.filePath: str = ''`**

该值不为`''`时，尝试将消息输出到日志文件中。

支持日期字符串模板，会动态的更改输出的日志文件。

该参数请在最后设置，若该值不为`''`，则会创建日志输出进程。

## **`logger.fileExpire: datetime.timedelta = datetime.timedelta(seconds = 0)`**

日志的过期时间，超过该期限的日志将被删除，仅在日志名为日期模板时生效。

请设置以天或月为最小单位的值，并保证日志名称的最小间隔为该过期时间，如以day为最小日期的日志名称模板必须以day为过期时间。

## **`logger.default(level: str, message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

默认的输出函数。如果使用的是自定义消息等级，请使用该函数手动输入等级。

- **refreshed**

    为`True`时会将当前行覆盖。

## **`logger.debug(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为DEBUG的输出函数。

## **`logger.info(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为INFO的输出函数。

## **`logger.starting(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为STARTING的输出函数。

## **`logger.ending(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为ENDING的输出函数。

## **`logger.warning(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为WARNING的输出函数。

## **`logger.danger(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为DANGER的输出函数。

## **`logger.websocket(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为WEBSOCKET的输出函数。

## **`logger.http(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为HTTP的输出函数。

## **`logger.loaded(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = False)`**

消息等级为LOADED的输出函数。

## **`logger.loading(message: str, styledMessage: str | None = None, *, end: str = '\n', refreshed: bool = True)`**

消息等级为LOADING的输出函数。

注意，该命令是覆盖的。

## **`logger.encode(message: str) -> str`**

当消息中有`'<'`和`'>'`字符时，容易与样式格式产生冲突。使用该函数对冲突部分进行加密，可以防止冲突。

## **`logger.destroy()`**

若设置了`logger.filePath`，请在程序结束前一定使用该函数以摧毁所有log程序。

若未设置，调用它并不不会发生什么事。
