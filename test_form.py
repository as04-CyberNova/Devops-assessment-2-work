import os
import unittest

class TestStudentRegistrationForm(unittest.TestCase):
    
    def setUp(self):
        self.filepath = 'index.html'

    def test_file_exists(self):
        """Test if the HTML file exists in the directory."""
        self.assertTrue(os.path.exists(self.filepath), f"File '{self.filepath}' does not exist.")

    def test_form_elements_exist(self):
        """Test if the HTML file contains required form elements."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Basic checks to see if the required HTML tags exist
        self.assertIn('<form', content, "HTML file is missing a <form> tag.")
        self.assertIn('<input', content, "HTML file is missing <input> tags.")
        self.assertIn('type="submit"', content.lower()) or self.assertIn('<button type="submit"', content.lower(), "HTML file is missing a submit button.")
        self.assertIn('<label', content, "HTML file is missing <label> tags.")

if __name__ == '__main__':
    unittest.main()
