# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.test import TestCase
from django.utils.translation import ugettext_lazy
from django.core.urlresolvers import resolve, reverse, NoReverseMatch

from seoutils.models import Meta
from seoutils.utils import get_meta_for_request


class DummyRequest(object):
    def __init__(self, path_info='/'):
        self.path_info = path_info

    @property
    def META(self):
        return {
            'PATH_INFO': self.path_info
        }


class SeoUtilsTestBase(TestCase):
    urls = 'seoutils.testurls'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def mock_meta(self, path_info, title='Test title', desc='Test desc', keywords='Test keywords', extra_js=None):
        return {
            'path_info': path_info,
            'title': title,
            'desc': desc,
            'keywords': keywords,
            'extra_js': extra_js,
        }


class SeoUtilsTest(SeoUtilsTestBase):
    """Basic tests for the seoutils application."""

    def test_unconfigured(self):
        self.failUnlessEqual(None, get_meta_for_request(DummyRequest(path_info='/')))

    def test_hard_url(self):
        mt = Meta.objects.create(**self.mock_meta('/'))
        rs = get_meta_for_request(DummyRequest(path_info='/'))

        self.failUnless(isinstance(rs, Meta))
        self.failUnlessEqual(rs.title, 'Test title')
        self.failUnlessEqual(rs.desc, 'Test desc')
        self.failUnlessEqual(rs.keywords, 'Test keywords')

    def test_named_url(self):
        mt = Meta.objects.create(**self.mock_meta('test-home'))
        rs = get_meta_for_request(DummyRequest(path_info='/'))

        self.failUnless(isinstance(rs, Meta))
        self.failUnlessEqual(rs.title, 'Test title')
        self.failUnlessEqual(rs.desc, 'Test desc')
        self.failUnlessEqual(rs.keywords, 'Test keywords')

    def test_fallbacks_negative(self):
        m1 = Meta.objects.create(**self.mock_meta('test-home'))
        m2 = Meta.objects.create(**self.mock_meta('test-contact', title='Test title2', desc='Test desc2', keywords='Test keywords2'))
        rs = get_meta_for_request(DummyRequest(path_info='/contact/'))

        self.failUnless(isinstance(rs, Meta))
        self.failUnlessEqual(rs.title, 'Test title2')
        self.failUnlessEqual(rs.desc, 'Test desc2')
        self.failUnlessEqual(rs.keywords, 'Test keywords2')

    def test_fallbacks_positive(self):
        m1 = Meta.objects.create(**self.mock_meta('test-home'))
        m2 = Meta.objects.create(**self.mock_meta('test-contact', title=None, desc=None, keywords=None))
        rs = get_meta_for_request(DummyRequest(path_info='/contact/'))

        self.failUnless(isinstance(rs, Meta))
        self.failUnlessEqual(rs.title, 'Test title')
        self.failUnlessEqual(rs.desc, 'Test desc')
        self.failUnlessEqual(rs.keywords, 'Test keywords')
