from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from base.serializers import StudentSerializer
from base.models import Student


class TestView(APIView):

    permission_classes = (IsAuthenticated)

    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        # single record
        # student = qs.first()
        # serializer = StudentSerializer(student)
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
