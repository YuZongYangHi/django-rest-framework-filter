
## 功能
配合Django-Rest-Framework框架使用， 拦截地方在关键函数``get_query()``, 进行调用

## 使用
可进行前段自定义字段传入， 后端进行一对一匹配字段进行渲染匹配

## views.py


```python
from filter import Filter 

def get_queryset(self):
	filter_instance = Filter(
		request=self.request, model=models.FaultType,
		name='name__contains')
	return filter_instance.filter('-id')
```

### Filter里面除了model和request是固定语法外， 其余均是请求的参数， key为参数，value为具体渲染的Django Field
