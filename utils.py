"""Useful utilities for diablo3 tool."""


def join_battle_tag(name, code):
  """Combine a user name and its number to be a battle tag.

  Args:
    name: a string of user name.
    code: a string of number.
  Returns:
    a '#' joined battle tag string.
  """
  return '%s#%s' % (name, number)


def split_battle_tag(battle_tag):
  """Split battle tag into name and code.

  Args:
    battle_tag: a string of '#' separated battle tag.
  Returns:
    (name, code) tuple of battle tag separated by '#'.
  """
  # TODO: handle exception for incorrect input
  name, code = battle_tag.split('#')
  return (name, code)


def battle_tag_to_url(battle_tag):
  """Turn the '#' in battle tag into '-'.

  Args:
    battle_tag: a str of battle_tag.
  Returns:
    a url part with '#' replaced by '-'.
  """
  return battle_tag.replace('#', '-')
