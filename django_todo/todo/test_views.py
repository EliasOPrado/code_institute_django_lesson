from django.test import TestCase
from .models import Item

class TestViews(TestCase):

    #will check if the home page is settled to the template and if is ok
    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'todo_list.html')

    #will check the /add pagination and whether it is settled to the right template
    def test_get_add_item_page(self):
        page = self.client.get('/add')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'item_form.html')

    #will check if items are being retrieved on the pagination based on template and http response
    def test_get_edit_item_page(self):
        item = Item(name='Create a Test')
        item.save()
        page = self.client.get('/edit/{0}'.format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'item_form.html')

    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get('/edit/1')
        self.assertEqual(page.status_code, 404)
        