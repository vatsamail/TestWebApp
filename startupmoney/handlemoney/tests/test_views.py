from django.test import TestCase, Client
# Can use request factory objects

from django.urls import reverse
from handlemoney.models import Project, Category, Expense

import json

class TestViews(TestCase):
    # the setUp name is important, acts like init
    def setUp(self):
        self.cli              = Client()
        self.list_url         = reverse('list')
        self.detail_url       = reverse('detail', args=['test_project'])
        self.test_project     = Project.objects.create(name='test_project', budget=10001, category='Operations')
        self.add_url          = reverse('add')

    def test_project_list_GET(self):
        # test code
        response = self.cli.get(self.list_url)

        # assert code
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_project_detail_GET(self):
        # test code
        response = self.cli.get(self.detail_url)

        # assert code
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')

    def test_project_detail_POST_add_expense(self):
        Category.objects.create(project=self.test_project, name='Development',)
        response = self.cli.post(self.detail_url,
            {
                'title': 'Test Expense',
                'amount': 1000,
                'category' : 'Development',
            }
        )
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.test_project.expenses.first().title, "Test Expense")

    def test_project_detail_POST_no_data(self):
        response = self.cli.post(self.detail_url, {})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.test_project.expenses.count(), 0)

    def test_project_detail_DELETE_delete_expense(self):
        test_cat = Category.objects.create(project=self.test_project, name='Development',)
        test_exp = Expense.objects.create(
            project   = self.test_project,
            title     = 'Test Expense',
            amount    = 1000,
            category  = test_cat,
        )

        response = self.cli.delete(self.detail_url, json.dumps({
            'id': test_exp.id,
        }))
        self.assertEquals(response.status_code, 204)
        self.assertEquals(self.test_project.expenses.count(), 0)

    def test_project_detail_DELETE_delete_no_id(self):
        test_cat = Category.objects.create(project=self.test_project, name='Development',)
        test_exp = Expense.objects.create(
            project   = self.test_project,
            title     = 'Test Expense',
            amount    = 1000,
            category  = test_cat,
        )

        response = self.cli.delete(self.detail_url)
        self.assertEquals(response.status_code, 404)
        self.assertEquals(self.test_project.expenses.count(), 1) # The existing data is not deleted

    def test_ProjectCreateView_POST(self):
        response = self.cli.post(self.add_url,
            {
            'name'             : 'Second Project',
            'budget'           : 20000,
            'categoriesString' : 'Design,Development,MVP',
            }
        )
        second_project = Project.objects.get(id=2)
        self.assertEquals(second_project.name, "Second Project")

        first_category = Category.objects.get(id=1)
        self.assertEquals(first_category.project, second_project)
        self.assertEquals(first_category.name, "Design")
        
        third_category = Category.objects.get(id=3)
        self.assertEquals(third_category.project, second_project)
        self.assertEquals(third_category.name, "MVP")
