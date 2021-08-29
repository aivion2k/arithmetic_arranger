def arithmetic_arranger(problems, a = False):
  # print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
  giga_list =[]
  if len(problems) > 5:
    return 'Error: Too many problems.'
  
  for problem in problems:
    ls=problem.split(' ')
    print(ls)
    # nie większe od 4
    szybka_lista=[]
    
    try:
      szybka_lista.append(int(ls[0]))
    except:
      return 'Error: Numbers must only contain digits.'
    
    try:
      szybka_lista.append(int(ls[2]))

    except:
      return 'Error: Numbers must only contain digits.'
    
    if max(szybka_lista) == szybka_lista[0]:
      l = 0
    else:
      l = 2

    if len(ls[l]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    # max znaków
    
    giga_list.append(len(ls[l])+2)

    # nie inty
    try:
      giga_list.append(int(ls[0]))
    except:
      return 'Error: Numbers must only contain digits.'
    
    
    try:
      giga_list.append(int(ls[2]))
    except:
      return 'Error: Numbers must only contain digits.'
    
    
    # znak działania
    giga_list.append(ls[1])

    # nie + i -
    if ls[1] =='+':
      wynik = int(ls[0]) + int(ls[2])
    elif ls[1] =='-':
      wynik = int(ls[0]) - int(ls[2])
    else:
      return "Error: Operator must be '+' or '-'."
    giga_list.append(wynik)

  max_dl = giga_list[::5]
  liczba_a = giga_list[1::5]
  liczba_b = giga_list[2::5]
  znak = giga_list[3::5]
  wynikab = giga_list[4::5]

  # print(liczba_a)
 
  # [3, 32, 698, '+', 730, 4, 3801, 2, '-', 3799, 2, 45, 43, '+', 88, 2, 123, 49, '+', 172]
  
  kupa = ''
  l_1=''
  l_2=''
  l_3=''
  l_4=''
  print(max_dl)
  
  for i in range(len(problems)):
    l_1 += ' '*(max_dl[i]-len(str(liczba_a[i]))) + str(liczba_a[i]) + 4*' '
    l_2 += znak[i] + ' '*(max_dl[i]-len(str(liczba_b[i]))-1) + str(liczba_b[i]) + 4*' '
    l_3 += '-'*(max_dl[i]) + 4*' '
  l_1 = l_1[:len(l_1)-4]  
  l_2 = l_2[:len(l_2)-4]  
  l_3= l_3[:len(l_3)-4] 
  l_1 = l_1+'\n'
  l_2 = l_2+'\n'
  
  print(giga_list)
  kupa = l_1+l_2+l_3
  if a==True:
    for i in range(len(problems)):
      l_4 += ' '*(max_dl[i]-len(str(wynikab[i]))) + str(wynikab[i]) + 4*' '
    l_4 = l_4[:len(l_4)-4]
    l_3 = l_3+'\n'
    kupa =l_1+l_2+l_3+l_4
    return kupa
  else:
    return kupa

  


  

