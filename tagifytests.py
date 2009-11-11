import unittest
from tagify import tagify

class TagifyTestCase(unittest.TestCase):
		
	def testTextNotEmpty(self):
		"""
		  Verify text returns content, if text is provided and not null
		"""
		tagified = tagify('This is a test')
		assert tagified
		
	def testTextEmpty(self):
	  """
	    Verify sending no text returns nothing
	  """
	  tagified = tagify('')
	  assert tagified
	  
	def testTagsNotEmpty(self):
	  """
	    Verify that tags are returned
	  """
	  tagified = ('This is a test with other valid taggable items', '', True)
	  assert tagified
	  
if __name__ == "__main__":
    unittest.main()