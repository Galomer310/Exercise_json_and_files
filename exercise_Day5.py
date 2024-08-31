# import random
#
# def get_words_from_file(file_path):
#     with open(file_path, 'r') as file:
#         words = file.read().splitlines()
#     return words
#
# def get_random_sentence(length, words):
#     sentence = ' '.join(random.choices(words, k=length))
#     return sentence.capitalize() + '.'
#
# def main():
#     print("Welcome to the sentence generator app! Please input a number between 2 and 20, and the app will generate a sentence with that length.\n")
#
#     while True:
#         try:
#             length = int(input("Please choose a number between 2 and 20:\n"))
#             if 2 <= length <= 20:
#                 return length
#             else:
#                 print("The number must be between 2 and 20. Try again.")
#         except ValueError:
#             print("Invalid input. Please enter a number between 2 and 20.")
#
#
# words_list = get_words_from_file('sowpods.txt')
# sentence_length = main()
# sentence = get_random_sentence(sentence_length, words_list)
# print(f"Generated sentence: {sentence}")


# 🌟 Exercise 2: Working with JSON
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
# print(data)

salary = data['company']['employee']['payable']['salary']
print(f"Salary: {salary}")

date_of_birth = data['company']['employee']['birth_date'] = '1991-16-09'
print(date_of_birth)

with open('updated_employee.json', 'w') as json_file:
    json.dump(data, json_file, indent=3)

with open('updated_employee.json', 'r') as json_file:
    print(json_file.read())
print("JSON data saved to 'updated_employee.json' .")
