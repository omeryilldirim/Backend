from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


@api_view()
def home(request):
    return Response(
        {'message': 'Hello, World!'},
    )

# -------------------------------------------------------------------
'''
    HTTP Request Types:
        GET -> Public verilerdir. Listeleme/Görüntüleme işlemlerinde kullanılır.
        POST -> Private verilerdir. Kayıt oluşturma işlemlerinde kullanılır. (ID'ye ihtiyaç duymaz.)
        * PUT -> Kayıt güncelleme işlemlerinde kullanılır. (Veri bir bütün olarak güncellenir.) (ID'ye ihtiyaç duyar.)
        * PATCH -> Kayıt güncelleme işlemlerinde kullanılır. (Verinin sadece ilgili kısmı güncellenir.) (ID'ye ihtiyaç duyar.)
        * DELETE -> Kayıt silme işlemlerinde kullanılır. (ID'ye ihtiyaç duyar.)
'''
# -------------------------------------------------------------------


@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(instance=students, many=True)
    # print(dir(serializer))
    # print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
        'message': 'Student created successfully!'
    }, status=status.HTTP_201_CREATED )
    else:
        return Response({
            'message':"Data is not valid",
            'data':serializer.data,
        }, status=status.HTTP_400_BAD_REQUEST )
    

from django.shortcuts import get_object_or_404

@api_view(['GET'])
def student_detail(request, pk):
    #student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student)
    return Response(serializer.data)

@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
        'message': 'Student updated successfully!'
    }, status=status.HTTP_202_ACCEPTED )
    else:
        return Response({
            'message':"Data is not valid",
            'data':serializer.data,
        }, status=status.HTTP_400_BAD_REQUEST )
    
@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    print(student)
    student.delete()
    return Response({
        'message': f'{student} deleted successfully!'
    }, status=status.HTTP_204_NO_CONTENT )

# -------------------------------------------------------------------

# Create or List

@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'message': 'Student created successfully!'
        }, status=status.HTTP_201_CREATED )
        else:
            return Response({
                'message':"Data is not valid",
                'data':serializer.data,
            }, status=status.HTTP_400_BAD_REQUEST )
        

# Retrieve or Update or Delete

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    # if request.method == 'GET':
    #     serializer = StudentSerializer(instance=student)
    #     return Response(serializer.data)
    # elif request.method == 'PUT':
    #     serializer = StudentSerializer(instance=student, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #         'message': 'Student updated successfully!'
    #     }, status=status.HTTP_202_ACCEPTED )
    #     else:
    #         return Response({
    #             'message':"Data is not valid",
    #             'data':serializer.data,
    #         }, status=status.HTTP_400_BAD_REQUEST )
    # elif request.method == 'DELETE':
    #     student.delete()
    #     return Response({
    #         'message': f'{student} deleted successfully!'
    #     }, status=status.HTTP_204_NO_CONTENT )
    match request.method:
        case 'GET':
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)
        case 'PUT':
            serializer = StudentSerializer(instance=student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                'message': 'Student updated successfully!'
            }, status=status.HTTP_202_ACCEPTED )
            else:
                return Response({
                    'message':"Data is not valid",
                    'data':serializer.data,
                }, status=status.HTTP_400_BAD_REQUEST )
        case 'DELETE':
            student.delete()
            return Response({
                'message': f'{student} deleted successfully!',
                'data': serializer.data, 
            }, status=status.HTTP_204_NO_CONTENT )