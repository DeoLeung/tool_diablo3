import unittest

import diablo3_api


class Diablo3APITest(unittest.TestCase):

  def setUp(self):
    self.battle_tag = 'Deo#2188'
    self.d3 = diablo3_api.Diable3API('eu.battle.net')

  def test_get_career_orig(self):
    golden = 'http://eu.battle.net/api/d3/profile/Deo-2188/'
    self.assertEqual(golden,
                     self.d3.get_career._original(self.d3, self.battle_tag))

  def test_get_hero_orig(self):
    golden = 'http://eu.battle.net/api/d3/profile/Deo-2188/hero/41685101'
    self.assertEqual(
        golden,
        self.d3.get_hero._original(self.d3, self.battle_tag, 41685101))

  def test_get_data_orig(self):
    golden = 'http://eu.battle.net/api/d3/data/item/veiled-crystal'
    self.assertEqual(
        golden,
        self.d3.get_data._original(self.d3, 'item/veiled-crystal'))

  def test_get_artisan_orig(self):
    golden = 'http://eu.battle.net/api/d3/data/artisan/mystic'
    self.assertEqual(
        golden,
        self.d3.get_artisan._original(self.d3, 'mystic'))

  def test_get_follower_orig(self):
    golden = 'http://eu.battle.net/api/d3/data/follower/templar'
    self.assertEqual(
        golden,
        self.d3.get_follower._original(self.d3, 'templar'))

  def test_get_item_orig(self):
    item_id = (
        'CoEBCO3YwpQMEgcIBBUYpf4THTsnbyQdZiMGUB2bBgDLHTp12owdS7X5Sx1yjh0hMI8CO'
        'N0BQABIFVASWARglQJqKwoMCAAQ2NWI24CAgOAaEhsIqMKEhgoSBwgEFRif2KswjwI4AE'
        'ABWASQAQClATp12oytAYGBxsS4AaWfv78GwAECGLCU9b8CUAJYAKABsJT1vwKgAcrLz_AG'
    )
    golden = (
        'http://eu.battle.net/api/d3/data/item/'
        'CoEBCO3YwpQMEgcIBBUYpf4THTsnbyQdZiMGUB2bBgDLHTp12owdS7X5Sx1yjh0hMI8CO'
        'N0BQABIFVASWARglQJqKwoMCAAQ2NWI24CAgOAaEhsIqMKEhgoSBwgEFRif2KswjwI4AE'
        'ABWASQAQClATp12oytAYGBxsS4AaWfv78GwAECGLCU9b8CUAJYAKABsJT1vwKgAcrLz_AG'
    )
    self.assertEqual(
        golden,
        self.d3.get_item._original(self.d3, item_id))

  # TODO: mock out the server to boost the tests.
  def test_get_career(self):
    self.assertTrue(self.d3.get_career(self.battle_tag))

  def test_get_hero(self):
    self.assertTrue(self.d3.get_hero(self.battle_tag, 41685101))

  def test_get_data(self):
    self.assertTrue(self.d3.get_data('item/veiled-crystal'))

  def test_get_artisan(self):
    self.assertTrue(self.d3.get_artisan('mystic'))

  def test_get_follower(self):
    self.assertTrue(self.d3.get_follower('templar'))

  def test_get_item(self):
    item_id = (
        'CoEBCO3YwpQMEgcIBBUYpf4THTsnbyQdZiMGUB2bBgDLHTp12owdS7X5Sx1yjh0hMI8CO'
        'N0BQABIFVASWARglQJqKwoMCAAQ2NWI24CAgOAaEhsIqMKEhgoSBwgEFRif2KswjwI4AE'
        'ABWASQAQClATp12oytAYGBxsS4AaWfv78GwAECGLCU9b8CUAJYAKABsJT1vwKgAcrLz_AG'
    )
    self.assertTrue(self.d3.get_item(item_id))


if __name__ == '__main__':
  unittest.main()
