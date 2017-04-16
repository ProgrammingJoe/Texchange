from selenium import webdriver
from django.core.management.base import BaseCommand
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Command(BaseCommand):

    # Main function to call all the methods
    def handle(self, *args, **options):
        driver = webdriver.Chrome()
        driver.get("https://shop.bookstore.ubc.ca/courselistbuilder.aspx")
        assert "UBC Bookstore" in driver.title

        # wait = WebDriverWait(driver, 10)
        # By.xpath("(//div[@id='brandSlider']/div[1]
        schoolbox = Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.xpath("(//select[@id='clCampusSelectBox']/option[0])")))))
        schools = schoolbox.options
        for index in range(0, len(schools) - 1):
            schoolbox.select_by_index(index)
            # classtypebox = Select(driver.find_element_by_id("clDeptSelectBox"))
            classtypebox = Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "clDeptSelectBox"))))
            # wait.until(EC.element_to_be_clickable(classtypebox.select_by_index(0)))
            classtypes = classtypebox.options
            for index in range(0, len(classtypes) - 1):
                classtypebox.select_by_index(index)
                # classnumberbox = Select(driver.find_element_by_id("clCourseSelectBox"))
                classnumberbox = Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "clCourseSelectBox"))))
                classnumbers = classnumberbox.options
                for index in range(0, len(classnumbers) - 1):
                    classnumberbox.select_by_index(index)
                    # classsectionbox = Select(driver.find_element_by_id("clSectionSelectBox"))
                    classsectionbox = Select(WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "clSectionSelectBox"))))
                    classsections = classsectionbox.options
                    for index in range(0, len(classsections) - 1):
                        classsectionbox.select_by_index(index)

        element = driver.find_element_by_link_text("CHOOSE BOOKS")
        element.location_once_scrolled_into_view
        element.click()

        books = driver.find_elements_by_class_name("book-info-wrapper")
        print(len(books))
        # driver.execute_script("arguments[0].scrollIntoView();", element)
        # driver.find_element_by_link_text("CHOOSE BOOKS").click()
        # things = driver.find_elements_by_xpath("//div[@class='clSelectedCourse']")
        # print(len(things))

        # driver.close()
