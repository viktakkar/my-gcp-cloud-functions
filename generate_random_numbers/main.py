'''
Google Cloud Function to generate random number
'''
import random
def generate_random_numbers(request):
    request_json = request.get_json(silent=True)
    dict_of_numbers = {}
    if request_json and 'numbers_to_generate' in request_json:
      numbers_to_generate = request_json['numbers_to_generate']
      for idx in range(int(numbers_to_generate)):
          dict_of_numbers[idx]=(random.randint(10, 20))

    return dict_of_numbers,200
