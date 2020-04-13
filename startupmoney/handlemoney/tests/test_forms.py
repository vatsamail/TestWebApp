from handlemoney.forms import ExpenseForm
from django.test import SimpleTestCase

class TestForms(SimpleTestCase):
    def test_expense_form_validator(self):
        form = ExpenseForm(data={
            'title':'some_expense',
            'amount':1001,
            'category':'Tea-Coffee',
        })
        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form = ExpenseForm()
        self.assertFalse(form.is_valid())
