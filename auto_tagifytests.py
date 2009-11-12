import unittest
from auto_tagify import auto_tagify

class AutoTagifyTestCase(unittest.TestCase):
		
	def testTextNotEmpty(self):
		"""
		  Verify text returns content, if text is provided and not null
		"""
		a = auto_tagify()
		a.text = 'This is a test'
		assert a.generate()
		
	def testTextEmpty(self):
	  """
	    Verify sending no text returns nothing
	  """
	  a = auto_tagify()
	  assert a.generate()
	  
	def testTagsNotEmpty(self):
	  """
	    Verify that tags are returned
	  """
	  a = auto_tagify()
	  a.text = 'This is a test with other valid taggable items'
	  assert a.tag_list
	  
if __name__ == "__main__":
    unittest.main()