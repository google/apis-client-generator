#!/usr/bin/python2.7
"""Tests for ordered_set.py."""

from google.apputils import basetest

from googleapis.codegen.utilities import ordered_set


class OrderedSetTest(basetest.TestCase):

  def testFrozenSet(self):
    s = ordered_set.FrozenOrderedSet(range(5))
    self.assertLen(s, 5)
    self.assertTrue(4 in s)
    self.assertEqual([x for x in range(5)], list(s))

  def testMutableSet(self):
    s = ordered_set.MutableOrderedSet()
    for i in range(5):
      s.add(i)
    self.assertLen(s, 5)
    self.assertTrue(4 in s)
    self.assertEqual([x for x in range(5)], list(s))

    s.remove(3)
    self.assertEqual([0, 1, 2, 4], list(s))
    s.clear()
    self.assertEmpty(s)


if __name__ == '__main__':
  basetest.main()
