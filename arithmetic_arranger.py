def arithmetic_arranger(problems, ans = False):
  arrange_problem = []
  n = len(problems)
  if n>5:
    return "Error: Too many problems."
  
  first, operator, second = [], [], []

  f,s, len_f, len_s = 0,0,0,0
  
  for problem in problems:
    words = problem.split()
  
    try:
      f = int(words[0])
      s = int(words[-1])
    except ValueError:
      return "Error: Numbers must only contain digits."

    len_f = len(words[0])
    len_s = len(words[-1])

    if len_f > 4 or len_s > 4:
      return "Error: Numbers cannot be more than four digits."

    if words[1] not in ['+','-']:
      return "Error: Operator must be '+' or '-'."

    first.append(words[0])
    second.append(words[-1])
    operator.append(words[1])

  # print(first, second, operator,sep = '\n') --ALL Fine till here

  num = []

# printing first operand

  ans_first =""
  ans_second = ""
  ans_third = ""
  ans_fourth = ""
  
  for i in range(n):
    len_f,len_s = len(first[i]), len(second[i])
    
    if len_f > len_s:
      num.append(len_f + 2)
    else: 
      num.append(len_s + 2)

    if i == n-1:
      ans_first+=(' '*(num[i]-len_f)+first[i])
      break
    ans_first+=(' '*(num[i]-len_f)+first[i]+'    ')

# printing second operand 
    
  for i in range(n):
    if i == n-1:
      ans_second+=(operator[i] +' '+ ' '*(num[i]-2-len(second[i])) + second[i])
      break
    ans_second+=(operator[i] +' '+ ' '*(num[i]-2-len(second[i]))+second[i]+'    ')

# printing ------ 
  for i in range(n):
    if i == n-1:
      ans_third+=('-'*num[i])
      break
      
    ans_third+=('-'*num[i]+'    ')

  # print("let's see")
  if ans == True:
    for i in range(n):
      if operator[i] == '+':
        answer = int(first[i]) + int(second[i])
      else:
        answer = int(first[i]) - int(second[i])

      str_ans = str(answer)
      l = len(str_ans)
      if i==n-1:
        ans_fourth+=(' '*(num[i]-l)+str_ans)
        break
      ans_fourth+=(' '*(num[i]-l)+str_ans+'    ')
      
  arrange_problem = [ans_first,ans_second,ans_third,ans_fourth]

  if ans==True:
    return '\n'.join(arrange_problem)
  return '\n'.join(arrange_problem[:3])
  
    
  

  

  
  
  
     
  


    # return arranged_problems