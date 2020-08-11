# Ripetizioni di Python

[moodle](https://elearning.dei.unipd.it/course/view.php?id=4707)

## Argomenti da rivedere:

- Try except 
  ```python
  try:
      x = 1/0
  except ZeroDivisionError:
      print('Attempt to divide by zero')
  except:
      print('Something else went wrong')
  else:
      print('No exceptions here!')
  finally:
      print('This will always be executed!')
  ```
  Altro esempio:
  ```python
  class FancyException(Exception):
      pass

  try:
      raise FancyException
  except FancyException:
      print('Raised a fancy exception')
  ```
- Dictionaries
- Sets

