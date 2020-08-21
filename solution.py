import random
text = []
def generate_sentence(start_token, filenames):
  token_dict = {}
  for filename in filenames:                  #read files
      file = open(filename, "r")
      lines = file.readlines()
      file.close()
      tokens_raw = ""
      for line in lines:
        tokens_raw += line                  #readLines puts each line as list element, so fuse them
      tokens_raw = tokens_raw.lower()                      #lowercase lines
      tokens = tokens_raw.split()
      token_last = ""
      for token in tokens:
        if not len(token_last) == 0:
          if not token_last in token_dict:
              token_dict[token_last] = [token]
          else:
              token_dict[token_last].append(token)
        token_last = token
  token_prev = ""
  output = ""
  output_length = 0
  stop = False
  token_prev = start_token.lower()
  output += token_prev + " "
  while not stop:                             #Generate tokens untill stop is given
    if not token_prev in token_dict:        #If we don't know the token, stop
      stop = True
      continue                            #Return to start to stop
    if len(token_dict[token_prev]) == 0:    #If token has no next token, stop
      stop = True
      continue
    if output_length > 198:                #If length is bigger or equal to 200, stop
      stop = True
      continue
    if token_prev == ".":                   #if last token was full stop, stop
      stop = True
      continue
    possiblenexttokens = token_dict[token_prev]
    token = random.choice(possiblenexttokens)
    output += token + " " #Space so there is spacing
    token_prev = token
    output_length = output_length +1
    output = output.lower()
  return output[:-1]

if __name__ == '__main__':
  # The random number generator is initialised to zero here purely
  # for your own testing so that each time you run your code during
  # development, you will get the same output. Remove this to get 
  # different output each time you run your code with the same input.
  random.seed(0)
  
  # Run the examples in the question.
  for i in range(4):
    print(generate_sentence('There', ['single.txt']))
  print('=' * 80)
  for i in range(4):
    print(generate_sentence('the', ['jab.txt']))
  print('=' * 80)
  for i in range(4):
    print(generate_sentence('It', ['dracula.txt', 'pandp.txt']))
  print('=' * 80)
  for i in range(10):
    print(generate_sentence('Once', ['dracula.txt', 'jb.txt', 'pandp.txt', 'totc.txt']))
