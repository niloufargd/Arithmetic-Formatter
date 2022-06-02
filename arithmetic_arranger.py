
def arithmetic_arranger(problems, answer=False):
  #Error: Too many problems. if more than 5 arguments are given
  #problem1=0, problem2=0, problem3=0, problem4=0, problem5=0
 #Error: Too many problems. if more than 5 arguments are given
  if len(problems) > 5:
    return 'Error: Too many problems.'

  solution = []
  for problem in problems:
  #for index, problem in enumerate(problems):
      arranger = problem.split(" ")

      #Error: Operator must be '+' or '-'.
      if arranger[1] != '+' and arranger[1] != '-':
          return "Error: Operator must be '+' or '-'."

      #Error: Numbers must only contain digits.
      if arranger[0].isdigit() == False or arranger[2].isdigit() == False:
          return 'Error: Numbers must only contain digits.'
      
      #Error: Numbers cannot be more than four digits.    
      if len(arranger[0]) > 4 or len(arranger[2]) > 4:
          return 'Error: Numbers cannot be more than four digits.'

      #Finding how many spaces/dashes will be needed, to right 
      longest_val = max(len(arranger[0]), len((arranger[2])))
      width = longest_val + 2

      #Right align the numbers

      first_line = f"{arranger[0]:>{width}}"
      second_line = arranger[1] + f'{arranger[2]:>{width - 1}}'
      third_line = '-' * width

    
      if arranger[1] == '+':
          fourth_line = f"{f'{int(arranger[0]) + int(arranger[2])}':>{width}}"
      else:
          fourth_line =f"{f'{int(arranger[0]) - int(arranger[2])}':>{width}}"
      #fourth_line = f"{arranger[2]:>{width}}"
      
      if answer == False:
        try:
          solution[0] += (" " * 4) + first_line
        except IndexError:
          solution.append(first_line)
        
        try:
          solution[1] += (" " * 4) + second_line
        except IndexError:
          solution.append(second_line)
        
        try:
          solution[2] += (" " * 4) + third_line
        except IndexError:
          solution.append(third_line)
        
      else:
        
        try:
          solution[0] += (" " * 4) + first_line
        except IndexError:
          solution.append(first_line)
        
        try:
          solution[1] += (" " * 4) + second_line
        except IndexError:
          solution.append(second_line)
        
        try:
          solution[2] += (" " * 4) + third_line
        except IndexError:
          solution.append(third_line)
        try:
          solution[3] += (" " * 4) + fourth_line
        except IndexError:
          solution.append(fourth_line)
          
  if answer == True:
    return f"{solution[0]}\n{solution[1]}\n{solution[2]}\n{solution[3]}"
  else:
    return f"{solution[0]}\n{solution[1]}\n{solution[2]}"
