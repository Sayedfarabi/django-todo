from .models import Task
from .serializers import TaskSerializer

class TaskService:
    @staticmethod
    def get_all_tasks():
        tasks = Task.objects.all()
        return TaskSerializer(tasks, many=True).data

    @staticmethod
    def create_task(data):
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, True
        return serializer.errors, False

    @staticmethod
    def get_task_by_id(pk):
        try:
            task = Task.objects.get(pk=pk)
            return task
        except Task.DoesNotExist:
            return None

    @staticmethod
    def update_task(task_instance, data):
        # partial=True so that PATCH support
        serializer = TaskSerializer(instance=task_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, True
        return serializer.errors, False

    @staticmethod
    def delete_task(task_instance):
        task_instance.delete()
        return True