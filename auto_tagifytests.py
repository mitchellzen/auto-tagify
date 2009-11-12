import unittest
from auto_tagify import AutoTagify

class AutoTagifyTestCase(unittest.TestCase):
		
	def testTextNotEmpty(self):
		"""
		  Verify text returns content, if text is provided and not null
		"""
		a = AutoTagify()
		a.text = 'This is a test'
		a.css = "taggable"
		self.assertEqual(a.generate(), 'This is a <a href="/test" class="taggable">test</a> ')
		
	def testTextEmpty(self):
	  """
	    Verify sending no text returns nothing
	  """
	  a = AutoTagify()
	  self.assertEqual(a.generate(), ' ')
	  
	def testTagsNotEmpty(self):
	  """
	    Verify that tags are returned
	  """
	  a = AutoTagify()
	  a.text = 'This is a test with other valid taggable items'
	  test_array = []
	  test_array.append('test')
	  test_array.append('other')
	  test_array.append('valid')
	  test_array.append('taggable')
	  test_array.append('items')
	  self.assertEqual(a.tag_list(), test_array)
	  
if __name__ == "__main__":
    unittest.main()