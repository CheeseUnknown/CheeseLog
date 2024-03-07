# **Level**

消息等级，它是该系统的核心。

```python
from CheeseLog import Level
```

## **`def __init__(self, weight: int, messageTemplate: str | None = None, timerTemplate: str | None = None, styledMessageTemplate: str | None = None)`**

- **weight**

    权重。更高的权重意味着更危险的信息。

- **messageTemplate**

    消息模版，未设置时默认为`logger.messageTemplate`。

- **timerTemplate**

    日期模版，未设置时默认为`logger.timerTemplate`。

- **styledMessageTemplate**

    消息样式模版，未设置时默认为`logger.styledMessageTemplate`。

## **11种默认消息等级**

```python
{
    'DEBUG': Level(10),
    'INFO': Level(20, styledMessageTemplate = '(<green>%l</green>) <black>%t</black> > %c'),
    'STARTING': Level(20, styledMessageTemplate = '(<green>%l</green>) <black>%t</black> > %c'),
    'ENDING': Level(20, styledMessageTemplate = '(<green>%l</green>) <black>%t</black> > %c'),
    'LOADING': Level(20, styledMessageTemplate = '(<blue>%l</blue>) <black>%t</black> > %c'),
    'LOADED': Level(20, styledMessageTemplate = '(<cyan>%l</cyan>) <black>%t</black> > %c'),
    'HTTP': Level(20, styledMessageTemplate = '(<blue>%l</blue>) <black>%t</black> > %c'),
    'WEBSOCKET': Level(20, styledMessageTemplate = '(<blue>%l</blue>) <black>%t</black> > %c'),
    'WARNING': Level(30, styledMessageTemplate = '(<yellow>%l</yellow>) <black>%t</black> > %c'),
    'DANGER': Level(40, styledMessageTemplate = '(<red>%l</red>) <black>%t</black> > %c'),
    'ERROR': Level(50, styledMessageTemplate = '(<magenta>%l</magenta>) <black>%t</black> > %c')
}
```
