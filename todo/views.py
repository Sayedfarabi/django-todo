from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import TaskService 

@api_view(['GET', 'POST'])
def task_list(request):
    # Get all tasks
    if request.method == 'GET':
        data = TaskService.get_all_tasks()
        return Response(data)

    # Create new task
    if request.method == 'POST':
        data, success = TaskService.create_task(request.data)
        if success:
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def task_detail(request, pk):
    task = TaskService.get_task_by_id(pk)
    
    if not task:
        return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    # 1. Single Get
    if request.method == 'GET':
        from .serializers import TaskSerializer
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # 2. Update (PUT/PATCH)
    elif request.method in ['PUT', 'PATCH']:
        data, success = TaskService.update_task(task, request.data)
        if success:
            return Response(data)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    # 3. Delete
    elif request.method == 'DELETE':
        TaskService.delete_task(task)
        return Response({'message': 'Task deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)