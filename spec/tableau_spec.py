from tableau import *
from expects import *

with describe(Tableau):
  with it('can make a Tableau'):
    expect(lambda: Tableau([1], [1])).not_to(raise_error(Exception))

  with context('invalid arguments'):
    with it('raises'):
      expect(lambda: Tableau([])).to(raise_error(Exception))

with describe(TableauRows):
  with it('can make a TableauRows'):
    expect(lambda: TableauRows([2, 2, 1])).not_to(raise_error(Exception))

  with context('invalid arguments'):
    with it('raises'):
      expect(lambda: TableauRows([1, 2, 1])).to(raise_error(Exception))

with describe(is_corner):
  with context('for a row-end'):
    with context('that is a corner'):
      with it('returns True'):
        expect(is_corner(3, [4, 2, 1])).to(be_true)
        expect(is_corner(5, [4, 2, 1])).to(be_true)
        expect(is_corner(6, [4, 2, 1])).to(be_true)

    with context('that is not a corner'):
      with it('returns False'):
        expect(is_corner(1, [2, 2, 2])).to(be_false)
        expect(is_corner(3, [2, 2, 2])).to(be_false)

  with context ('not at a row-end'):
    with it('returns False'):
      for i in xrange(3):
        expect(is_corner(i, [4, 2, 1])).to(be_false)
      expect(is_corner(4, [4, 2, 1])).to(be_false)

      for i in xrange(0, 6, 2):
        expect(is_corner(i, [2, 2, 2])).to(be_false)

with describe(hook_number):
  with context('known tableau'):
    with it('is correct'):
      for i, expected in enumerate([6, 4, 2, 1, 3, 1, 0]):
        expect(hook_number(i, [4, 2, 1])).to(equal(expected))

  with context('for corners'):
    with it('returns 1'):
      for i in [3, 5, 6]:
        expect(hook_number(i, [4, 2, 1])).to(equal(expected))

with describe(coordinates):
  with context('known tableau'):
    with it('is correct'):
      expect(coordinates(0, [4, 2, 1])).to(equal((0, 0)))
      expect(coordinates(2, [4, 2, 1])).to(equal((0, 2)))
      expect(coordinates(4, [4, 2, 1])).to(equal((1, 0)))
      expect(coordinates(5, [4, 2, 1])).to(equal((1, 1)))
      expect(coordinates(6, [4, 2, 1])).to(equal((2, 0)))

