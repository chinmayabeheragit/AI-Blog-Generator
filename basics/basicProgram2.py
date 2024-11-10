def missingCharacters(s):
  # Create a list to store character counts (ASCII values)
  char_counts = [0] * 123

  # Count characters in the input string
  for char in s:
    char_code = ord(char)
    char_counts[char_code] += 1

  # Build the result string
  result = ""
  for char_code in range(48, 58):  # Add missing digits (48-57 represent 0-9)
    if char_counts[char_code] == 0:
      result += chr(char_code)

  for char_code in range(97, 123):  # Add missing lowercase letters (97-122 represent a-z)
    if char_counts[char_code] == 0:
      result += chr(char_code)

  return result

if __name__ == '__main__':
  s = input()
  result = missingCharacters(s)
  print(result)