def PalindromeCreator(strParam):

  #to find palindromes, the input must be at least 3 letters long
  if len(strParam) > 3:

    ###check if it is palindrome already
    output = check_pali_already(strParam)

    if output !="palindrome": #do the other checks only if it is not already a palindrome

      #remove 1 character and check if it is a palindrome
      output = remove_1_charac_make_pali(strParam) 

      #if no palindrome found, then remove 2 characters and check again
      if len(output) > 1:
        output = remove_2_characs_make_pali(strParam)

      #output the letter or pair of letters only if palindrome has minimum length 3
      output = check_pali_length_3(strParam,output)


  else: #if input length is less than 3, then no palindromes at least 3 long can be found
    output = "not possible"

  return output

def check_pali_length_3(strParam,cut_letters):
  #inputs: cut_letters is either the letters cut out from palis, or it is the full 'strParam' if no palis were found
  #output the letter or pair of letters only if palindrome has minimum length 3
  pali_length = len(strParam) - len(cut_letters)
  if pali_length < 3:
    output = "not possible" #not possible if palindrome is too short
  else:
    output = cut_letters
  
  return output
  

def remove_2_characs_make_pali(strParam):
  # remove 2 characters and check if it is a palindrome
  length = len(strParam)

  #remove every possible pair of letters and check if palindrome
  for k in range (length):
    for m in range (length):
      if (k < m) or (k > m): #we dont want to remove the same letter twice
        if len(strParam) > 2: #go only if we havent yet discovered a palindrome from the string
          smaller_strParam = ''.join([strParam[n] for n in range(len(strParam)) if n not in (k, m)]) #remove kth and mth indexes

          flipped_small = flip_word_around(smaller_strParam) #flip the letters

          if flipped_small == smaller_strParam: #if it is a palindrome
            strParam = strParam[k] + strParam[m] #output both the letters which are removed

  return strParam 


def remove_1_charac_make_pali(strParam):
  #remove 1 character and check if it is a palindrome
  length = len(strParam)

  for j in range (length): #loop through each letter
    if len(strParam) > 1: #go only if we havent yet discovered a palindrome from the string
      smaller_strParam =  strParam[:j] + strParam[j+1:] #remove 1 letter

      flipped_small = flip_word_around(smaller_strParam)

      if flipped_small == smaller_strParam: #if it is a palindrome
        strParam = strParam[j] #output is the letter which is removed
        
  
  return strParam

def flip_word_around(strParam):
  ##flip the word around
  length = len(strParam)

  #create the word flipped around
  flipped_strParam = []
  for i in range (length):
    flipped_strParam.append(strParam[length - i - 1])
  #convert to string
  flipped_strParam2 = [''.join(flipped_strParam)][0]

  return flipped_strParam2

def check_pali_already(strParam):
  flipped_strParam2 = flip_word_around(strParam)

  if flipped_strParam2 == strParam: #make it "palindrome if it is"
    strParam = "palindrome"

  return strParam


# keep this function call here 
print(PalindromeCreator("abjchba"))