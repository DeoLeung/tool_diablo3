import unittest

import diablo3_api

"""
{u'timePlayed': {u'crusader': 0.0, u'wizard': 0.0, u'monk': 0.0, u'barbarian': 1.0, u'witch-doctor': 0.0, u'demon-hunter': 0.0}, u'progression': {u'act1': True, u'act2': True, u'act3': True, u'act4': True, u'act5': True}, u'kills': {u'hardcoreMonsters': 32675, u'monsters': 69644, u'elites': 5830}, u'paragonLevelHardcore': 112, u'fallenHeroes': [], u'lastHeroPlayed': 41685101, u'lastUpdated': 1399557132, u'paragonLevel': 49, u'heroes': [{u'name': u'Deo', u'level': 70, u'gender': 0, u'dead': False, u'class': u'barbarian', u'paragonLevel': 112, u'hardcore': True, u'id': 41685101, u'last-updated': 1399557132}, {u'name': u'Deo', u'level': 70, u'gender': 0, u'dead': False, u'class': u'barbarian', u'paragonLevel': 49, u'hardcore': False, u'id': 38422378, u'last-updated': 1399153882}], u'battleTag': u'Deo#2188'}
"""
class Diablo3APITest(unittest.TestCase):

  def setUp(self):
    self.battle_tag = 'Deo#2188'
    self.d3 = diablo3_api.Diable3API('eu.battle.net')

  def test_get_career(self):
    self.assertTrue(self.d3.get_career(self.battle_tag))


if __name__ == '__main__':
  unittest.main()
