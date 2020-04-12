from django.test import SimpleTestCase
from django.urls import reverse, resolve
from handlemoney.views import project_list, project_detail, ProjectCreateView

class TestUrls(SimpleTestCase):
    def test_list(self):
        url = reverse('list')
        # prints: ResolverMatch(func=handlemoney.views.project_list, args=(), kwargs={}, url_name=list, app_names=[], namespaces=[], route=)
        # print(resolve(url))
        self.assertEquals(resolve(url).func, project_list)

    def test_add(self):
        url = reverse('add')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_detail(self):
        url = reverse('detail', args=['some-arg',])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, project_detail)
