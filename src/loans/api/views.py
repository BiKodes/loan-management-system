from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.viewsets import ModelViewset
from loans.models import Loan, LoanPayments, LoanTerms, CustomerAccount
from loans.api.serializers import LoanSerializer







@api_view(['POST',])
def loan_create_view(request, pk):
    
    loan = Loan.objects.get(pk=pk)

    loan_user = Loan(user=loan)

    if request.method == "POST":
        serializer = Loan(loan_user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def loan_detail_veiw(request, pk):
    try:
        loan_details = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanSerializer(loan_details)
        return Response(serializer.data)

@api_view(['PUT',])
def loan_update_detail_view(request, pk):
    try:
        loan_details = LoanSerializer.objects.get(pk=pk)
    except Loan.DoesNotEXist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = LoanSerializer(loan_details, data=request.data)

        data = {}

        if serializer.is_valid():
            serializer.save()
            data["success"] = "Loan details updated successfuly!"

            return Response(data=data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def loan_delete_details_view(request, pk):
    try:
        loan_details = LoanSerializer.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = loan_details.delete()
        data = {}

        if operation:
            data["success"] = "Loan details deleted successfuly!."

        else:
            data["failure"] = "Delete failed!!!"
        
        return Response(data=data)


