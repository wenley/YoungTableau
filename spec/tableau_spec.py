from tableau import *
from expects import *

with describe('Tableau'):
  with it('can make a Tableau'):
    expect(lambda: Tableau([1], [1])).not_to(raise_error(Exception))
