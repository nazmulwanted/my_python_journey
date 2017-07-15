def find_average_list(number_list):
  result = 0
  count=0
  for number in number_list:
    result += number
    count += 1
  avg = result / count
  return avg

average = find_average_list([10, 20, 30, 40])
print(average)
