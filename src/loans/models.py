from django.db import models

LOAN_STATUSES = [
    ('paid', ("Paid")),
    ('pending', ('Pending')),
    ('approved', ('Approved')),
    ('rejected', ('Rejected')),
    ('overdue', ('Overdue')),
    ]

PAYMENT_FREQUENCY = [
    ('daily', ("Daily")),
    ('weekly', ("Weekly")),
    ('monthly', ("Monthly")),
    ('quarterly', ("Quarterly")),
]

PAYMENT_MODES = [
    ('mpesa', ('Mpesa')),
    ('airtel_money', ('Airtel Money')),  
    ('t-cash', ('T-Cash')),
    ('cash', ('Cash')),
    ('bank', ('Bank')),
]

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=15, decimal_places=2)
    date_applied = models.DateTimeField( auto_now=True)
    due_date = models.DateTimeField(blank=True)
    loan_term = models.ForeignKey(LoanTerm, on_delete=models.CASCADE, related_name="loans")
    status = model.models.CharField(choices=LOAN_STATUSES, max_length=50)
    loan_terms = models.ForeignKey(LoanTerms, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ['-date_applied']

class LoanTerms(models.Model):
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_payment_amount = models.DecimalField(max_digits=15, decimal_places=2)
    loan_payment_from = models.DateTimeField()
    loan_payment_due_date = models.models.DateTimeField()
    loan_payment_frequency = models.CharField(choices=PAYMENT_FREQUENCY, max_length=50)
    terms_conditions = models.TextField()


class LoanPayments(models.Model):
    payment_refence = models.CharField(max_length=150)
    loan = model.models.ForeignKey(Loan, on_delete=models.CASCADE)
    mode_of_payment = models.CharField(choices=PAYMENT_MODES, max_length=50)
    date_of_payment = models.DateTimeField()
    amount_of_payment = models.DecimalField(max_digits=15, decimal_places=2)
    loan_balance = models.models.DecimalField(max_digits=15, decimal_places=2)
    remarks = models.TextField()

     class Meta:
        ordering = ['-date_of_payment']

    @property
    def total():
        # payment = LoanPaymen.objects.get(id=<>)
        # payment.total
        pass