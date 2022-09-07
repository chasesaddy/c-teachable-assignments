class Node:
  def __init__(self, val, prev = None, next = None):
    self.val = val
    self.prev = prev
    self.next = next

class BrowserHistory:
  # Initializes browser hisotry from new tab. 
  # By default the starting URL will be an empty string.
  def __init__(self, homepage): 
      self.deque = Node( homepage )
  
  # Returns the url of the current page.
  def current_page(self):
      return self.deque.val
  
  # Navigates to the "page" from the current page. 
  # Nagivating forward should overwrite all previous forward browser history.
  def visit(self, page): 
      tmp = self.deque
      new_node = Node( page )
      self.deque.next = new_node      
      self.deque = new_node
      self.deque.prev = tmp
  
  # Navigates to the previous page visited.
  # After navigating return the URL of the current page.
  def go_back(self):
      self.deque = self.deque.prev      
      return self.deque.val
    
  # Navigates to the page ahead in browser history.
  # If there is no page ahead, do nothing.
  # After navigating return the URL of the current page.
  def go_forward(self):
      if self.deque.next is not None:
        self.deque = self.deque.next
        return self.deque.val
  
  # Navigates backwards N pages in browser history.
  # If there are not N pages behind, then return the new tab URL which is an empty string.
  # After navigating return the URL of the current page.
  def back(self, N):
      for i in range( N ):
          if self.deque.prev is None:
              # coachable
              return ''
              # leetcode
            #   break
          self.deque = self.deque.prev
      return self.deque.val

  # Navigates forward N pages in browser history.
  # If there are not N pages ahead, then go as far as you can.
  # After navigating return the URL of the current page.
  def forward(self, N):
      for i in range( N ):
          if self.deque.next is None:
              break
          self.deque = self.deque.next
      return self.deque.val

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
