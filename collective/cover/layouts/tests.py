# -*- coding: utf-8 -*-

from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
# from Testing import ZopeTestCase as ztc
# from zope.component import testing
# from zope.testing import doctestunit

import collective.cover.layouts
import unittest

ptc.setupPloneSite()


class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             collective.cover.layouts)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        # doctestunit.DocFileSuite(
        #     'README.txt', package='collective.cover.layouts',
        #     setUp=testing.setUp, tearDown=testing.tearDown),

        # doctestunit.DocTestSuite(
        #     module='collective.cover.layouts.mymodule',
        #     setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        # ztc.ZopeDocFileSuite(
        #     'README.txt', package='collective.cover.layouts',
        #     test_class=TestCase),

        # ztc.FunctionalDocFileSuite(
        #     'browser.txt', package='collective.cover.layouts',
        #     test_class=TestCase),
    ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
