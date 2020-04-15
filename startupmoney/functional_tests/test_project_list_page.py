from selenium import webdriver
from handlemoney.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.chrome.options import Options
import os
import time

class TestProjectListPage(StaticLiveServerTestCase):

    SHORT  = 5
    MEDIUM = 10
    LONG   = 20
    EVER   = 60

    def setUp(self):
        # before every function

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        if os.name == 'nt':
            # for windows Chrome
            self.browser = webdriver.Chrome(os.path.join('functional_tests', 'chromedriver.exe'), chrome_options=chrome_options)
        else:
            # for non-windows (aka Ubuntu-Linux) use headless gecko
            self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def tearDown(self):
        # after every function
        self.browser.close()

    def test_hello_world(self):
        # testing
        self.assertEquals(0, 0)


    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)

        # take some time to see it visually


        # The user requests the page for the first time
        """
        this can be found by using the inspect button on the browser.
        Once you start inspecting, just rollover the mouse on the visual objects
        you will find the class name and the tag names
        """
        alert = self.browser.find_element_by_class_name('noproject-wrapper')
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text,
            "Sorry, you don't have any projects, yet."
        )


    def test_no_projects_alert_button_redirects_to_add_page(self):
        self.browser.get(self.live_server_url)

        # The user requests the page for the first time
        add_url = self.live_server_url + reverse('add')
        # time.sleep(self.LONG)
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )


    def test_user_sees_project_list(self):
        prj = Project.objects.create(name='test', budget=1000,)
        self.browser.get(self.live_server_url)

        # user should see a project
        # time.sleep(self.SHORT)
        self.assertEquals(
            self.browser.find_element_by_tag_name('h5').text,
            "test"
        )
        # time.sleep(self.SHORT)

    def test_user_click_visit_button(self):
        prj = Project.objects.create(name='Test Project', budget=1000,)
        self.browser.get(self.live_server_url)
        # user should see a project and clicks visit and hence redirected to detail page
        detail_url = self.live_server_url+reverse('detail', args=[prj.slug])
        self.browser.find_element_by_link_text('VISIT').click()
        self.assertEquals(
            self.browser.current_url,
            detail_url
        )
        # time.sleep(self.SHORT)
