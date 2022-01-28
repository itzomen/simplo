from unicodedata import category
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.db.models import Q
from .models import Category
from .serializers import CategorySerializer


@api_view(["POST"])
def create(request):
    """Gets data and Create New Category"""
    data = request.data
    try:
        category = Category.objects.create(
            name=data["name"],
            description=data["description"]
        )

        image = request.FILES.get("image")

        if image:
            category.image = image
            category.save()

        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
def update(request, pk):
    """Gets data and Update Category"""
    try:
        category = Category.objects.get(id=pk)
        data = request.data
        category.name = data.get('name')
        category.description = data.get('description')

        image = request.FILES.get("image")
        if image:
            category.image = image
            category.save()
        
        category.save()
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def delete(request,pk):
    try:
        category = Category.objects.get(id=pk)       
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'details': f"{e}"},status=status.HTTP_204_NO_CONTENT)