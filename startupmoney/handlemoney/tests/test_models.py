from django.test import TestCase
from handlemoney.models import Project, Category, Expense

class TestModels(TestCase):
    def setUp(self):
        self.prj = Project.objects.create(name='Project 1', budget=1000)

    def test_project_save_slug(self):
        self.assertEquals(self.prj.slug, "project-1") # slug behavior

    def test_project_budget_left(self):
        cat = Category.objects.create(project=self.prj, name="Development")
        exp = Expense.objects.create(project=self.prj, title='Dev Mode', amount=100, category=cat)
        self.assertEquals(self.prj.budget_left, 900)

    def test_project_total_transactions(self):
        prj2 = Project.objects.create(name='Project 2', budget=2000)
        cat  = Category.objects.create(project=self.prj, name="Development")
        exp  = Expense.objects.create(project=self.prj, title='Dev Mode', amount=100, category=cat)
        exp2 = Expense.objects.create(project=prj2, title='Dev Mode', amount=300, category=cat)
        exp3 = Expense.objects.create(project=prj2, title='Dev Mode', amount=300, category=cat)

        self.assertEquals(self.prj.total_transactions, 1)
        self.assertEquals(prj2.total_transactions, 2)
