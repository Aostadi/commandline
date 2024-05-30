import sys
from io import StringIO

from career.models import Company
from django.core import management
from django.test import TestCase


class AddTests(TestCase):

    def test_success_add_sample(self):
        err = StringIO()
        sys.stdin = StringIO('Snap\nSnap@email.com\n09122201202\nOnline Taxi\n')
        management.call_command('addCompany', stderr=err)
        seven_learn = Company.objects.get(name='Snap')
        self.assertEqual(seven_learn.email, 'Snap@email.com')
        self.assertEqual(seven_learn.phone, '09122201202')
        self.assertEqual(seven_learn.description, 'Online Taxi')
        self.assertEqual(err.getvalue(), '')


class EditTest(TestCase):
    def setUp(self):
        Company.objects.create(name='7learn', email="7learn@email.com", phone="09122201202",
                               description="a place for programmers")

    def test_success_edit(self):
        try:
            management.call_command('editCompany', '7learn', name='7learn', email="7learn@email.com",
                                    phone="+989112201202", description="Coding Competition")
        except:
            self.fail("unexpected CommandError!")
        seven_learn = Company.objects.get(name="7learn")
        self.assertEqual(seven_learn.email, "7learn@email.com")
        self.assertEqual(seven_learn.phone, "+989112201202")
        self.assertEqual(seven_learn.description, "Coding Competition")


class RemoveTest(TestCase):
    def setUp(self):
        self.seven_learn = Company.objects.create(name='7learn', email="7learn@email.com", phone="09122201202",
                                            description="a place for programmers")
        self.yektanet = Company.objects.create(name='yektanet', email="Yektanet@email.com", phone="09122201203")
        self.snap = Company.objects.create(name='snap', email="snap@email.com", phone="09122201204")

    def test_remove_all(self):
        try:
            err = StringIO()
            management.call_command('rmCompany', stderr=err, all=True)
        except:
            self.fail("unexpected CommandError!")
        self.assertEqual(Company.objects.all().count(), 0)
        self.assertEqual(err.getvalue(), '')
