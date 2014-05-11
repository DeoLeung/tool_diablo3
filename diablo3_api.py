"""wrapper of Blizzard diablo3 web api."""
import json
import os
import urllib2

import utils


class Diable3API(object):

  def __init__(self, battle_net_host):
    self.host = battle_net_host
    self.career_url = 'http://%s/api/d3/profile/%%s/' % self.host

  def get_career(self, battle_tag):
    url = self.career_url % utils.battle_tag_to_url(battle_tag)
    result = urllib2.urlopen(url)
    if result.getcode() == 200:
      return json.loads(result.read())
    # TODO: handle non-200 errors
