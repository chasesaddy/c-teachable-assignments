class Node:
  def __init__(self, val, prev = None, next = None):
    self.val = val
    self.prev = prev
    self.next = next

class BrowserHistory:
  # Initializes browser hisotry from new tab. 
  # By default the starting URL will be an empty string.
  def __init__(self, homepage): 
      self.curr = ''
  
  # Returns the url of the current page.
  def current_page(self):
      return self.curr.val
  
  # Navigates to the "page" from the current page. 
  # Nagivating forward should overwrite all previous forward browser history.
  def go_to(self, page): 
      tmp = self.curr
      new_node = Node( page )
      # the old/current pointer
      self.curr.next = new_node  
      # now this is the new_node at pointer
      self.curr = new_node
      # setting new_node's and now the pointer prev
      self.curr.prev = tmp
  
  # Navigates to the previous page visited.
  # After navigating return the URL of the current page.
  def go_back(self):
      self.curr = self.curr.prev
      return self.curr.val
    
  # Navigates to the page ahead in browser history.
  # If there is no page ahead, do nothing.
  # After navigating return the URL of the current page.
  def go_forward(self):
      if self.curr.next is not None:
        self.curr = self.curr.next
        return self.curr.val
  
  # Navigates backwards N pages in browser history.
  # If there are not N pages behind, then return the new tab URL which is an empty string.
  # After navigating return the URL of the current page.
  def skip_backward(self, N):
      for i in range( N ):
          if self.curr.prev is None:
              return ''
          self.curr = self.curr.prev
      return self.curr.val

  def skip_backward_instructions(self, N):
      for i in range( N ):
          if self.curr.prev is None:
              break
          self.curr = self.curr.prev
      return self.curr.val

  # Navigates forward N pages in browser history.
  # If there are not N pages ahead, then go as far as you can.
  # After navigating return the URL of the current page.
  def skip_forward(self, N):
      for i in range( N ):
          if self.curr.next is None:
              break
          self.curr = self.curr.next
      return self.curr.val

__name__ = '__main__':
    history = BrowserHistory()
    history.go_to("leetcode.com") 
    history.go_to("google.com")                # You are in "leetcode.com". Visit "google.com"
    history.go_to("facebook.com")              # You are in "google.com". Visit "facebook.com"
    history.go_to("youtube.com")               # You are in "facebook.com". Visit "youtube.com"
    history.go_back()                          # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    history.go_back()                          # You are in "facebook.com", move back to "google.com" return "google.com"
    history.go_forward()                       # You are in "google.com", move forward to "facebook.com" return "facebook.com"
    history.go_to("linkedin.com")              # You are in "facebook.com". Visit "linkedin.com"
    history.skip_forward(2)                    # You are in "linkedin.com", you cannot move forward any steps.
    history.skip_backward(2)                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    history.skip_backward(7)                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
