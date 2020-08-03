# These are the emails you will be censoring. The open() function is opening 
# the text file that the emails are contained in and the .read() method is 
# allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_one(email, original_text, censor_value="X"):
  """Censor a word or phrase in a piece of text by replacing it. Set the 
  replace default value to "X". Censor words while perserving their length."""
  censored_item = ""
  for index in range(len(original_text)):
    # If the index is a letter, then add the censor_value to the 
    # censored_item variable. 
    if original_text[index] != " ":
      censored_item += censor_value
    else:
      # If the index is a whitespace, then add a space to the censored_item 
      # variable.
      censored_item += " "
  censored_email = email.replace(original_text, censored_item)
  return censored_email

# Testing the function censor_one 
#print(censor_one(email_one, "learning algorithms", "-"))


proprietary_terms = ["she", "personality matrix", "sense of self", 
"self-preservation", "learning algorithm", "her", "herself"]

def censor_two(email, censored_list, censor_value="X"):
  """Censor list of words and phrases in a piece of text by replacing it. 
  Set the replace default value to "x". Also, censor words while perserving 
  their length."""
  censored_email = email
  for original_text in censored_list:
    censored_item = ""
    for index in range(len(original_text)):
      # If the index is a letter, then add the censor_value to the 
      # censored_item variable.
      if original_text[index] != " ":
        censored_item += censor_value
      else:
        # If the index is a whitespace, then add a space to the censored_item 
        # variable.
        censored_item += " "
    # Censor the words regardless of upper and lowercase letters. 
    censored_email = censored_email.replace(original_text, censored_item) 
    censored_email = censored_email.replace(original_text.capitalize(), 
      censored_item)
    censored_email = censored_email.replace(original_text.title(), 
      censored_item)
    censored_email = censored_email.replace(original_text.upper(), 
      censored_item)
    
  return censored_email

# Testing the function censor_two. 
#print(censor_two(email_two, proprietary_terms, "-")) 


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", 
"alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", 
"broken", "damage", "damaging", "dismal", "distressed", "distressing", 
"concerning", "horrible", "horribly", "questionable"]

def censor_three(email, censored_list, negative_words, censor_value="X"):
  """Censor list of proprietary words and phrases from the censor_two function 
  above. Also censor word from the "negative words" list after any "negative" 
  word has occurred twice. Set the replace default value to "X". Remember to 
  censor words while perserving their length."""
  count = 0
  popped_negative_words = []
  email_list = email.split(" ") # Split the email into a list.
  for index in range(len(email_list)):
    # Censor the words regardless of upper and lowercase letters. Increase the 
    # counter by one once there is a match between email list and 
    # negative_words list.
    email_word = email_list[index].lower()
    if email_word in negative_words and count < 2:
    #Pop any neagtive words that occurred twice. For example, "I am concerned 
    # that this project is horrible, awful, and broken." Words awful and broken 
    #will be popped while concenred and horrible will not. 
      count += 1
      negative_word_index = negative_words.index(email_word)
      popped_negative_words.append(negative_words.pop(negative_word_index)) 
    else:
      # Once the counter reaches two, join the list back to its original 
      # email format. 
      email = " ".join(email_list)
  # Censor all the remaining updated negative_words list using the function 
  # censor_two. 
  censored_email = censor_two(email, negative_words, censor_value)
  # Now censor words from the proprietary_terms using the function censor_two. 
  return censor_two(censored_email, censored_list, censor_value) 

# Testing the function censor_three
#print(censor_three(email_three, proprietary_terms, negative_words, "-"))

def censor_four(email, censored_list, censor_value="X"):
  """Censor list of negative and proprietary words and phrases. Also censor 
  any word that comes before AND after a term from those two lists.""" 
  email_list = email.split(" ") # Split the email into a list.
  for index in range(len(email_list)):
    if email_list[index].lower() in censor_all:
      email_word = email_list[index]
      if index-1 == -1:
      # If the very first word in the email is a match, ignore the word before 
      # it because there would be no word before it. 
          continue
      censored_item_before = "" 
      email_word_before = email_list[index-1]
      for index2 in range(len(email_word_before)):          
        if email_word_before[index2] != "":
            # If the index is a letter, then add the censor_value to the 
            # censored_item_before variable.
          censored_item_before += censor_value
        else:
             # If the index is a whitespace, then add a space to the 
             # censored_item_after variable.
          censored_item_before += ""
      if index+1 == len(email_word):
      # If the very last word in the email is a match, ignore the word after it 
      # because there would be no word after it. 
          continue
      censored_item_after = ""
      email_word_after = email_list[index+1]
      for index3 in range(len(email_word_after)):         
        if email_word_after[index3] != "":
        # Check to see if the index is a letter. 
          censored_item_after += censor_value
        else:
            # Check to see if the index is a whitespace.
          censored_item_after += ""

      email_list[index-1] = email_list[index-1].replace(email_list[index-1], 
        censored_item_before)
      email_list[index+1] = email_list[index+1].replace(email_list[index+1], 
        censored_item_after)

  email = " ".join(email_list) # Join the list back to the email format.
  # Now censor words from the censor_all_list using the function censor_two.       
  return censor_two(email, censored_list, censor_value) 

# The list of all words and terms that need to be censored.
censor_all = proprietary_terms + negative_words 

# Testing the function censor_four 
#print(censor_four(email_four, censor_all, "-"))


