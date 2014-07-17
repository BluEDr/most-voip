'''
Created on 24/giu/2014

@author: crs4
'''


class ICall:
    
    
    def get_local_uri(self):
        """
        :returns: the uri of the local sip account
        """
        raise NotImplementedError
    
    def get_remote_uri(self):
        """
        :returns: the uri of the remote sip account
        """
        raise NotImplementedError
    
    def get_state(self):
        """
        :returns: the current state of this call
        """
        raise NotImplementedError
    
    
class IBuddy:
    def get_state(self):
        """
        :returns: the current state of this call
        """
        raise NotImplementedError
       
    def get_uri(self):
        """
        :returns: the sip uri of this buddy
        """
        raise NotImplementedError
    
    def get_extension(self):
        """
        :returns: the sip extension of this buddy
        """
        raise NotImplementedError
   
    def get_status_text(self):
        """
        :returns: a textual description of the current status of this buddy
        """
        raise NotImplementedError
   
    def refresh_status(self):
        """
        Refreshes the current status of this buddy
        """
        raise NotImplementedError 
    
    
    
    
class IServer:
    def get_state(self):
        """
        :returns: the current status of the sip server
        """
        raise NotImplementedError
    
    def get_ip(self):
        """
        :returns: the ip address of the sip server
        """
        raise NotImplementedError


class IAccount:
    def get_uri(self):
        """
        :returns: the sip uri of this account
        """
        raise NotImplementedError
    
    def get_state(self):
        """
        :returns: the current state of this account
        """
        raise NotImplementedError
    
    def add_buddy(self, extension):
        """
        Add the specified buddy to this account (so its current state can be notified)
        :param extension: the extension related to the buddy to add
        """
        raise NotImplementedError
        
    def remove_buddy(self, extension):
        """
        Remove the specified buddy from this account
        :param extension: the extension related to the buddy to remove
        """
        raise NotImplementedError
        
    def get_buddy(self, extension):
        """
        Get the buddy with the given extension
        :param extension: the extension of the buddy
        :returns: IBuddy -- the buddy with the specified extension
        """
        raise NotImplementedError
    
    def get_buddies(self):
        """
        Get the list of buddies of the current registered account
        :returns:  the list of the buddies of the currently registered account
        """
        raise NotImplementedError
   

 
    
