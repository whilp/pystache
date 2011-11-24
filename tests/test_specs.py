# encoding: utf-8

import glob
import json
import os
import unittest
import pystache

class MetaSpecTest(type):
    """Build tests for the official Mustache specification.
    
    Classes that use this metaclass must have a *spec* attribute available at
    compile time. This is the name (excluding extension) of the spec file,
    relative to *specdir*, used for the test (eg "comments"). This file is then
    parsed and methods for each test described in the file are created and added
    to the new class' dictionary.

    Classes that use this metaclass must also define a *do_test* method that
    takes a dictionary and uses it to test the template engine.
    """

    specdir = os.environ.get("MUSTACHE_SPEC_DIR", "./spec/specs")
    """Path to the specs.

    The official spec repository can be found here:

        https://github.com/mustache/spec

    By default, simply checking the spec repository out while in the root of the
    pystache repository should do The Right Thing.
    """

    testprefix = "test_"
    """Prefix for test methods."""

    specext = ".json"
    """Spec filename extension, including a dot (if any)."""

    loader = json.load
    """Function to parse test data from a file-like stream."""
    
    def __new__(cls, name, bases, dct):
        spec = dct.get("spec")
        if spec:
            dct.update(cls.load(spec))
        return super(MetaSpecTest, cls).__new__(cls, name, bases, dct)

    @classmethod
    def load(cls, spec):
        """Load tests from specfile *spec*.

        *spec* is the basename of a file in the official Mustache spec
        repository.
        """
        spec = os.path.join(cls.specdir, spec + cls.specext)
        with open(spec) as f:
            data = cls.loader(f)

        for test in data["tests"]:
            name, fn = cls.build(test)
            data[cls.testprefix + name] = fn

        return data

    @classmethod
    def build(cls, data):
        """Build a Mustache specification test method.

        The test method calls a *do_test* method on the test class, passing it
        *data* as its sole argument.
        """
        name = data["name"].lower().replace(" ", "_")
        def test(self):
            self.do_test(data)

        return name, test

class BaseSpecTest(unittest.TestCase):
    __metaclass__ = MetaSpecTest

    def do_test(self, data):
        """Run a Mustache specification test.

        *data* is a dictionary that defines the test with *template*, *data* and
        *expected* keys. *do_test* calls the pystache renderer and raises an
        assertion error if the rendered result doesn't match the expected value.
        """
        result = pystache.render(data["template"], data["data"])
        self.assertEquals(data["expected"], result)
        
# The specification test cases.
class TestComments(BaseSpecTest):
    spec = "comments"

class TestInterpolation(BaseSpecTest):
    spec = "interpolation"

class TestInverted(BaseSpecTest):
    spec = "inverted"

class TestPartials(BaseSpecTest):
    spec = "partials"

class TestSections(BaseSpecTest):
    spec = "sections"

class TestLambdas(BaseSpecTest):
    spec = "~lambdas"
