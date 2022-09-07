class Node:
  def __init__(self, val, prev = None, next = None):
    self.val = val
    self.prev = prev
    self.next = next

class BrowserHistory(object):
  # Initializes browser hisotry from new tab. 
  # By default the starting URL will be an empty string.
  def __init__(self, homepage): 
      self.head = None
      self.tail = None
      self.visit( homepage )
  
  # Returns the url of the current page.
  def current_page(self):
      return self.url
  
  # Navigates to the "page" from the current page. 
  # Nagivating forward should overwrite all previous forward browser history.
  def visit(self, page): 
      new_node = Node( page )
      if self.head is not None:
        self.add_to_front_of_tail( self.head )
      self.head = new_node
  
  # Navigates to the previous page visited.
  # After navigating return the URL of the current page.
  def go_back(self):
      curr = self.tail
      curr = curr.prev
      if curr is None:
          return
      self.tail = curr
      return curr.val
    
  # Navigates to the page ahead in browser history.
  # If there is no page ahead, do nothing.
  # After navigating return the URL of the current page.
  def go_forward(self):
      curr = self.head
      #   if curr.next is None:
      #       return
      curr = curr.next
      if curr is None:
          return
      self.head = curr
      return curr.val
  
  # Navigates backwards N pages in browser history.
  # If there are not N pages behind, then return the new tab URL which is an empty string.
  # After navigating return the URL of the current page.
  def back(self, N):
      if self.tail is None:
          return
      curr = self.tail
      for i in range( N ):
          if curr.prev is None:
              return ''
          curr = curr.prev
            
    #   if curr is None:
    #       self.tail = None
    #   else:
      self.tail = curr
      return curr.val

  # Navigates forward N pages in browser history.
  # If there are not N pages ahead, then go as far as you can.
  # After navigating return the URL of the current page.
  def forward(self, N):
      if self.head is None:
            return
      curr = self.head
      tailend = self.tail
      for i in range( N ):
          self.add_to_front_of_tail( curr )
          if curr.next is None:
              break          
          curr = curr.next
              
    #   if curr is None:
        #   self.head = None
    #   else:
      self.head = curr.next
      return curr.val

  def add_to_front_of_tail(self, val):
      new_node = Node( val )
      new_node.prev = self.tail
      self.tail = new_node
      
  def add_to_front_of_front(self, node):
      temp = self.head
      new_node = node
      new_node.next = self.head
      self.head = new_node


  def asList(self):
    lst = []
    deux = []
    head = self.head
    tail = self.tail
    while head:
        lst.append( head.val )
        head = head.next
    while tail:
        deux.append( tail.val )
        tail = tail.next
    return [ lst, deux ]

if __name__ == '__main__':
    browserHistory = BrowserHistory("leetcode.com")
    print( browserHistory.asList() )
    print( browserHistory.visit("google.com") )

    print( browserHistory.asList() )
    print( browserHistory.visit("facebook.com") )
    print( browserHistory.asList() )
    print( browserHistory.visit("youtube.com") )
    print( browserHistory.asList() )
    print( browserHistory.back(1) )
    print( browserHistory.asList() )
    print( browserHistory.back(1) )
    print( browserHistory.asList() )
    print( browserHistory.forward(1) )
    print( browserHistory.asList() )
    browserHistory.visit("linkedin.com")
    print( browserHistory.asList() )
    print( browserHistory.forward(2) )
    print( browserHistory.asList() )
    print( browserHistory.back(2) )
    print( browserHistory.asList() )
    print( browserHistory.back(7) )
    print( browserHistory.asList() )
