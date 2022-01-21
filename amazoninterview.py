#Variations of this script were reported to have been asked to be done live at interviews with Amazon.

def stats_finder(array):
  # Calculate the mean
  mean = sum(array)/len(array)
  #Make frequency table
  freq = {}
  #Make a list for modes
  modes = []
  #Make a list for output
  output = []
  #go through each number of input
  for num1 in array:
    #record frequency in a dict
    if num1 in freq.keys() : 
      freq[num1] = freq[num1] + 1 
    else: 
      freq[num1] = 1 #initiate

  #define the highest frequency
  modevalue = max(freq.values()) 

  #compare each number for equality
  for key in freq:
    if freq.get(key) == modevalue:
      modes.append(key) #add to modes
  
  mode = min(modes) #take the smaller key
  output.append(mean)
  output.append(mode)
  return(output)

print(stats_finder([500, 400, 400, 375, 300, 350, 325, 300]))