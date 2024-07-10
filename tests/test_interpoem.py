import unittest
from interpoem.parser import parser
from interpoem.interpreter import interpret_poem

class TestInterpoem(unittest.TestCase):
    def test_parser(self):
        data = '''
        poem {
          title: "Test Poem";
          author: "Tester";

          stanza {
            line {
              text: "This is a test line.";
              on: hover {
                change_text: "Hovered!";
              }
            }
          }
        }
        '''
        parsed_poem = parser.parse(data)
        self.assertEqual(parsed_poem['title'], "Test Poem")
        self.assertEqual(parsed_poem['author'], "Tester")
        self.assertEqual(parsed_poem['stanzas'][0][0]['text'], "This is a test line.")
        self.assertEqual(parsed_poem['stanzas'][0][0]['events']['hover'][0]['change_text'], "Hovered!")

    def test_interpreter(self):
        parsed_poem = {
            'title': "Test Poem",
            'author': "Tester",
            'stanzas': [
                [
                    {
                        'text': "This is a test line.",
                        'events': {'hover': [{'change_text': "Hovered!"}]}
                    }
                ]
            ]
        }
        html_output = interpret_poem(parsed_poem)
        self.assertIn("This is a test line.", html_output)
        self.assertIn("Hovered!", html_output)

if __name__ == '__main__':
    unittest.main()
