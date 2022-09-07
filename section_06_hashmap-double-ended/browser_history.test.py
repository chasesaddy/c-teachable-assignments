import unittest

from browser_history import BrowserHistory

class TestK1( unittest.TestCase ):
    def setUp( self ):
      self.history = BrowserHistory()

    def step_1( self ):        
      self.assertEqual( 
        self.history.current_page(), 
        '' 
      )
        
    def step_2( self ):
      result = history.go_to("leetcode.com") 
      self.assertEqual( 
        self.history.current_page(), 
        'leetcode.com' 
      )

    def step_3( self ):
      result = history.go_to("google.com") 
      self.assertEqual( 
        self.history.current_page(), 
        'leetcode.com' 
      )

    def step_4( self ):        
      result = history.go_to("facebook.com") 
      self.assertEqual( 
        self.history.current_page(), 
        'facebook.com' 
      )

    def step_5( self ):
      result = history.go_to("youtube.com") 
      self.assertEqual( 
        self.history.current_page(), 
        'youtube.com' 
      )

    def step_6( self ):
      result = history.go_back()
      self.assertEqual( 
        self.history.current_page(), 
        'facebook.com' 
      )

    def step_7( self ):
      result = history.go_back()
      self.assertEqual( 
        self.history.current_page(), 
        'google.com' 
      )

    def step_8( self ):
      result = history.go_forward()
      self.assertEqual( 
        self.history.current_page(), 
        'facebook.com' 
      )

    def step_9( self ):
      result = history.go_to("linkedin.com") 
      self.assertEqual( 
        self.history.current_page(), 
        'linkedin.com' 
      )

    def step_10( self ):
      result = history.skip_forward( 2 )
      self.assertEqual( 
        result, 
        'google.com' 
      )

    def step_11( self ):
      result = history.skip_backward( 2 )
      self.assertEqual( 
        result, 
        'google.com' 
      )

    def step_12( self ):
      result = history.skip_backward( 7 )
      self.assertEqual( 
        result, 
        '' 
      )

    def step_12_instructions( self ):
      result = history.skip_backward_instructions( 7 )
      self.assertEqual( 
        result, 
        'leetcode.com' 
      )

if __name__ == '__main__':
  unittest.main()
