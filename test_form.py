import os
import unittest

class TestStudentRegistrationForm(unittest.TestCase):
    
    def setUp(self):
        self.filepath = 'index.html'

    def test_file_exists(self):
        """Test if the HTML file exists in the directory."""
        self.assertTrue(os.path.exists(self.filepath), f"File '{self.filepath}' does not exist.")

    def test_form_elements_exist(self):
        """Test if the HTML file contains the core form elements."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            
        # Core structure checks
        self.assertIn('<form', content, "HTML file is missing a <form> tag.")
        self.assertIn('<input', content, "HTML file is missing <input> tags.")
        self.assertIn('<label', content, "HTML file is missing <label> tags.")
        self.assertTrue('type="submit"' in content or '<button type="submit"' in content, "HTML file is missing a submit button.")

    def test_specific_input_fields(self):
        """Test if all the required student registration fields exist."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Specific fields check based on our UI design
        self.assertIn('name="firstName"', content, "Missing 'firstName' input field.")
        self.assertIn('name="lastName"', content, "Missing 'lastName' input field.")
        self.assertIn('name="email"', content, "Missing 'email' input field.")
        self.assertIn('name="course"', content, "Missing 'course' select dropdown.")

    def test_page_metadata(self):
        """Test if the HTML page has proper metadata and title."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read().lower()

        self.assertIn('<!doctype html>', content, "Missing DOCTYPE declaration.")
        self.assertIn('<title>', content, "Missing <title> tag.")
        self.assertIn('student registration', content, "Title does not contain 'Student Registration'.")

if __name__ == '__main__':
    unittest.main()
