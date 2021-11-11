from rest_framework import serializers
from loans.models import Loan, LoanPayments, LoanTerms, CustomerAccount

class LoanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loan
        fields = ['user', 'loan_amount', 'status']


class LoanPayementsSerializer(serializers.ModelSerializer):
    # total = serializers.ReadOnlyField(source="total")
    
    class Meta:
        model = LoanPayments
        fields = "__all__"

class LoanTermsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LoanTerms
        fields = ['interest_rate', 'loan_payment_amount', '']


class CustomerAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAccount
        fields = ['pk', 'email', 'username', 'occupation']