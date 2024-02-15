# **Progress Bar**

CheeseLog提供了一个自定义的进度条，配合loading可以达到更好的使用效果。

```python
import time

from CheeseLog import logger, ProgressBar

progressBar = ProgressBar()
for i in range(101):
    message, styledMessage = progressBar(i / 100)
    logger.loading(message, styledMessage)
    time.sleep(0.1)
logger.destroy()
```

## **`class ProgressBar`**

### **`def __init__(self, length: PositiveInt = 20, template: str = '%b%l%r%b %p', *, boundaryStr: str = '|', leftStr: str = '█', rightStr: str = '-')`**

- **length**

    进度条的长度。

- **template**

    模版，通过占位符匹配内容：

    | key | description |
    | - | - |
    | %b | 边界字符 |
    | %l | 左侧完成的进度 |
    | %r | 右侧未完成的进度 |
    | %p | 百分数 |

- **boundaryStr**

    边界字符。

- **leftStr**

    完成的进度字符。

- **rightStr**

    未完成的进度字符。

### **`def __call__(self, value: NonNegativeFloat) -> Tuple[str, str]`**

- **value**

    百分数。
