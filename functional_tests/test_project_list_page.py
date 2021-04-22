from selenium import webdriver
from budgetApp.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self) -> None:
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element_by_class_name('noproject-wrapper')
        self.assertEqual(alert.find_element_by_tag_name('h3').text, "Sorry, you don't have any projects, yet.")
        time.sleep(1)

    def test_no_projects_add_button_redirect_to_add_page(self):
        self.browser.get(self.live_server_url)
        add_page_url = self.live_server_url + reverse('add')
        self.browser.find_element_by_tag_name('a').click()
        self.assertEqual(self.browser.current_url, add_page_url)
        time.sleep(1)

    def test_user_saw_project_list(self):
        Project.objects.create(name='testProject', budget=1000)
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.find_element_by_tag_name('h5').text, 'testProject')
        time.sleep(1)

    def test_user_reirected_to_prject_details(self):
        test_project = Project.objects.create(name='testProject', budget=1000)
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.find_element_by_tag_name('h5').text, 'testProject')
        detail_page_url = self.live_server_url + reverse('detail', args=[test_project.slug])
        self.browser.find_element_by_link_text('VISIT').click()
        self.assertEqual(self.browser.current_url, detail_page_url)
        time.sleep(1)

