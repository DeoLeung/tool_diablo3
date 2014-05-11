"""wrapper of Blizzard diablo3 web api."""
import json
import urllib2

import utils


class Diable3API(object):

  def __init__(self, battle_net_host):
    self.host = battle_net_host
    self.career_url = 'http://%s/api/d3/profile/%%s/' % self.host
    self.hero_url = '%shero/%%d' % self.career_url
    self.item_url = 'http://%s/api/d3/data/%%s' % self.host
    self.follower_type = ('enchantress', 'templar', 'scoundrel')
    self.artisan_type = ('blacksmith', 'jeweler', 'mystic')

  def get_career(self, battle_tag):
    url = self.career_url % utils.battle_tag_to_url(battle_tag)
    result = urllib2.urlopen(url)
    if result.getcode() == 200:
      return json.loads(result.read())
    # TODO: handle non-200 errors

  def get_hero(self, battle_tag, hero_id):
    url = self.hero_url % (utils.battle_tag_to_url(battle_tag), hero_id)
    result = urllib2.urlopen(url)
    if result.getcode() == 200:
      return json.loads(result.read())
    # TODO: handle non-200 errors

  def get_data(self, tooltip_params):
    url = self.item_url % tooltip_params
    result = urllib2.urlopen(url)
    if result.getcode() == 200:
      return json.loads(result.read())
    # TODO: handle non-200 errors

  def get_follower(self, follower_type):
    if follower_type not in self.follower_type:
      raise ValueError(
          '%s is not a valid follower type %s'
          % (follower_type, '|'.join(self.follower_type)))
    return self.get_data('follower/%s' % follower_type)

  def get_artisan(self, artisan_type):
    if artisan_type not in self.artisan_type:
      raise ValueError(
          '%s is not a valid artisan type %s'
          % (artisan_type, '|'.join(self.artisan_type)))
    return self.get_data('artisan/%s' % artisan_type)

  def get_item(self, item_id):
    return self.get_data('item/%s' % item_id)
