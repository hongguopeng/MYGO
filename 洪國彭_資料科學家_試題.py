input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}

output_value = {}
value = list(input_value.keys())[0]
input_value = input_value.pop(list(input_value.keys())[0])
output_value[list(input_value.keys())[0]] = value

while True:
    drop_key = list(input_value.keys())[0]
    input_value = input_value.pop(drop_key)
    if type(input_value) is dict:
        value = list(input_value.keys())[0]
    elif type(input_value) is str:
        value = input_value
    temp = output_value.copy()
    output_value = {}
    output_value[value] = temp
    if type(input_value) is str:
        break

