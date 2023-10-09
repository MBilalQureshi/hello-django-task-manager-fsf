from django.test import TestCase
from .forms import ItemForm

# 1.	run all test in every file
# python3 manage.py test
# 2.	run specific file for test
# python3 manage.py test todo.test_forms
# 3.	run specific class of specific file
# python3 manage.py test todo.test_forms.TestItemForm
# 4.	run specific class of specific file of specific test
# python3 manage.py test todo.test_forms.TestItemForm.
# test_fields_are_explicit_in_form_metaclass


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
