import unittest

import utils


class UtilTest(unittest.TestCase):

  def test_join_battle_tag(self):
    name, code = 'Deo', '2188'
    battle_tag = 'Deo#2188'
    self.assertEqual(battle_tag, utils.join_battle_tag(name, code))

  def test_join_battle_tag(self):
    name, code = 'Deo', '2188'
    battle_tag = 'Deo#2188'
    self.assertEqual((name, code), utils.split_battle_tag(battle_tag))

  def test_battle_tag_to_url(self):
    battle_tag = 'Deo#2188'
    url_part = 'Deo-2188'
    self.assertEqual(url_part, utils.battle_tag_to_url(battle_tag))


if __name__ == '__main__':
  unittest.main()
