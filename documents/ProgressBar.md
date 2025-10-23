# **Progress Bar**

CheeseLog提供了一个自定义的进度条，配合loading可以达到更好的使用效果。

```python
from CheeseLog import ProgressBar
```

## **`def __init__(self, length: int = 20, *, template: str = '%b%f%e%b %p%', template_styled: str = '%b%f%e%b <blue>%p</blue>%', boundaryChar: str = '|', fillChar: str = '█', emptyChar: str = '░')`**

- **length**

    进度条的长度。

- **template**

    进度条模板；支持的占位符有：
    - %b: 边界字符
    - %f: 进度条主体
    - %e: 已完成部分
    - %p: 百分比

- **template_styled**

    样式化进度条模板，支持的占位符同上。

- **boundaryChar**

    边界字符。

- **fillChar**

    已完成部分字符。

- **emptyChar**

    未完成部分字符。

### **`def __call__(self, value: float) -> tuple[str, str]`**

- **value**

    百分数，范围[0, 1]。
