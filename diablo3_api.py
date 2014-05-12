"""wrapper of Blizzard diablo3 web api."""
import json
import logging
import urllib2

import utils


class Diable3API(object):

  def __init__(self, battle_net_host):
    self.host = battle_net_host
    self.career_url = 'http://%s/api/d3/profile/%%s/' % self.host
    self.hero_url = '%shero/%%d' % self.career_url
    self.data_url = 'http://%s/api/d3/data/%%s' % self.host
    self.follower_types = ('enchantress', 'templar', 'scoundrel')
    self.artisan_types = ('blacksmith', 'jeweler', 'mystic')

  def get_url(func):
    def decorated(*args, **kwargs):
      url = func(*args, **kwargs)
      result = urllib2.urlopen(url)
      if result.getcode() == 200:
        return json.loads(result.read())
      # TODO: handle non-200 errors
    decorated._original = func
    return decorated

  @get_url
  def get_career(self, battle_tag):
    return self.career_url % utils.battle_tag_to_url(battle_tag)

  @get_url
  def get_hero(self, battle_tag, hero_id):
    return self.hero_url % (utils.battle_tag_to_url(battle_tag), hero_id)

  @get_url
  def get_data(self, tooltip_params):
    return self.data_url % tooltip_params

  @get_url
  def get_follower(self, follower_type):
    if follower_type not in self.follower_types:
      raise ValueError(
          '%s is not a valid follower type %s'
          % (follower_type, '|'.join(self.follower_types)))
    return self.data_url % ('follower/%s' % follower_type)

  @get_url
  def get_artisan(self, artisan_type):
    if artisan_type not in self.artisan_types:
      raise ValueError(
          '%s is not a valid artisan type %s'
          % (artisan_type, '|'.join(self.artisan_types)))
    return self.data_url % ('artisan/%s' % artisan_type)

  @get_url
  def get_item(self, item_id):
    return self.data_url % ('item/%s' % item_id)
