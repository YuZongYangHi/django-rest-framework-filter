

# views.py

def get_queryset(self):
	filter_instance = Filter(
		request=self.request, model=models.FaultType,
		name='name__contains')
	return filter_instance.filter('-id')
