# coding=UTF-8
from game import *
from user import *

class group(object):

  """
   
  :version:
  :author:
  """

  """ ATTRIBUTES
   
  adminList  (private)
   
  memberList  (private)
   
  banList  (private)
   
  groupName  (protected)
   
  games  (protected)
   
  waitList  (private)
  """
  def __init__(self, nameIn):
      global adminList = []
      global memberList = []
      global banList = []
      global groupName = nameIn
      global games = []
      global waitList = []
      
  def _launchGame(self, gameToLaunch):
    """
     
    @param game gameToLaunch : 
    @return bool :
    @author
    """
    pass

  def _banPlayer(self, badPerson):
    """
     
    @param user badPerson : 
    @return bool :
    @author
    """
    if badPerson in memberList:
        memberList.remove(badPerson)
        banList.add(badPerson)
        return True
    else:
        return False

  def _addPlayer(self, player):
    """
     
    @param user player : 
    @return bool :
    @author
    """
    if player in waitlist:
        memberList.add(player)
        return True
    else:
        return False
    pass

  def _addAdmin(self, player):
    """
     
    @param user player : 
    @return bool :
    @author
    """
    if player in memberList:
      adminList.add(player)
      return True
    else:
      return False

  def _setAttributes(self,player,name,genre):
    """
     
    @param user player : 
    @return bool :
    @author
    """
    if player in adminList:
      groupName = name
      games.setGenre(genre)
      return True 
    else: 
      return False
