import json

from hamcrest import assert_that, equal_to, is_in
from selene.api import s, by, query

from my_task_8 import get_db, add_zone


class DbPage:
    main_page_url = 'https://my-json-server.typicode.com/IlyaKnysh/fake_db'
    db_url = 'https://my-json-server.typicode.com/IlyaKnysh/fake_db/db'
    db_ad_zones_url = "https://my-json-server.typicode.com/IlyaKnysh/fake_db/ad_zones"
    db_info_link = s(by.xpath("//a[normalize-space()='db_info']"))
    app_ids_link = s(by.xpath("//a[normalize-space()='app_ids']"))
    ad_zones_link = s(by.xpath("//a[normalize-space()='ad_zones']"))
    networks_link = s(by.xpath("//a[normalize-space()='networks']"))
    db_link = s(by.xpath("//a[normalize-space()='db']"))
    db_info = s(by.xpath("//sup[normalize-space()='object']"))
    app_ids = s(by.xpath("//li[2]//sup[1]"))
    ad_zones = s(by.xpath("//li[3]//sup[1]"))
    networks = s(by.xpath("//li[4]//sup[1]"))
    db_page = s(by.xpath("//pre"))


class DbPageSteps:
    def __init__(self, browser_):
        self.browser = browser_
        self.db_page = DbPage()
        self.api_response = get_db(self.db_page.db_url).json()

    def open(self):
        self.browser.open(self.db_page.main_page_url)

    def post_new_zone(self):
        return add_zone(self.db_page.db_ad_zones_url)

    @staticmethod
    # extracting the text content of a web element and converting it to a Python object (a dictionary)
    def get_text(selector):
        return json.loads(selector.get(query.text))

    def click_db_link(self):
        self.db_page.db_link.click()

    def compare_db_name(self, get_resource_text):
        assert_that(get_resource_text.get('db_name')), equal_to(self.api_response.get('db_info').get('db_name'))

    def compare_db_author(self, get_resource_text):
        assert_that(get_resource_text.get('author')), equal_to(self.api_response.get('db_info').get('author'))

    def compare_resources_amount(self, get_resource_text):
        assert_that(len(get_resource_text), equal_to(len(self.api_response)))

    def verify_resource_type(self):
        for resource in self.api_response:
            near_object_element = getattr(self.db_page, resource)
            near_object_text = near_object_element.get(query.text)
            if isinstance(self.api_response[resource], list):
                assert_that(int(near_object_text), equal_to(len(self.api_response[resource])))
            else:
                assert_that(near_object_text, equal_to('object'))

    def click_db_info_link(self):
        self.db_page.db_info_link.click()

    def compare_db_info_objects(self, actual):
        expected = self.api_response["db_info"]
        assert_that(expected, equal_to(actual))

    def click_app_ids_link(self):
        self.db_page.app_ids_link.click()

    def compare_app_ids_objects(self, actual):
        expected = self.api_response["app_ids"]
        assert_that(expected, equal_to(actual))

    def click_ad_zones_link(self):
        self.db_page.ad_zones_link.click()

    def compare_ad_zones_objects(self, actual):
        expected = self.api_response["ad_zones"]
        assert_that(expected, equal_to(actual))

    def click_networks_link(self):
        self.db_page.networks_link.click()

    def compare_networks_objects(self, actual):
        expected = self.api_response["networks"]
        assert_that(expected, equal_to(actual))

    def compare_new_zone(self, db_page_text):
        db_ad_zones = db_page_text['ad_zones']
        new_zone = add_zone(self.db_page.db_ad_zones_url).json()
        assert_that(new_zone, is_in(db_ad_zones))

    def compare_increased_number(self):
        near_object = self.db_page.ad_zones.get(query.text)
        assert_that(int(near_object), equal_to(4))


def test_db_name_and_author(browser_):
    step = DbPageSteps(browser_)
    step.open()
    step.click_db_info_link()
    step.compare_db_name(step.get_text(DbPage.db_page))
    step.compare_db_author(step.get_text(DbPage.db_page))


def test_resources_amount(browser_):
    step = DbPageSteps(browser_)
    step.open()
    step.click_db_link()
    step.compare_resources_amount(step.get_text(DbPage.db_page))


def test_resource_types(browser_):
    step = DbPageSteps(browser_)
    step.open()
    step.verify_resource_type()


def test_db_info_page(browser_):
    step = DbPageSteps(browser_)
    step.open()
    step.click_db_info_link()
    step.compare_db_info_objects(step.get_text(DbPage.db_page))


def test_app_ids_page(browser_):
    step = DbPageSteps(browser_)
    step.open()
    step.click_app_ids_link()
    step.compare_app_ids_objects(step.get_text(DbPage.db_page))


def test_ad_zones_page(browser_):
    step = DbPageSteps(browser_)
    step.open()
    step.click_ad_zones_link()
    step.compare_ad_zones_objects(step.get_text(DbPage.db_page))


def test_networks_page(browser_):
    step = DbPageSteps(browser_)
    step.open()
    step.click_networks_link()
    step.compare_networks_objects(step.get_text(DbPage.db_page))


def test_new_zone(browser_):
    step = DbPageSteps(browser_)
    step.post_new_zone()
    step.open()
    step.click_db_link()
    step.compare_new_zone(step.get_text(DbPage.db_page))
    step.compare_increased_number()

