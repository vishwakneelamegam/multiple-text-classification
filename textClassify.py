
classes = {
    "year" : ["2001","2002"],
    "make" : ["bmw","benz"],
    "model" : ["cl","el"],
}

#list of keys
keys = list(classes.keys())

#append data of all classes
whole = []
for data in keys:
  whole = whole + classes[str(data)]


#find probability of each word
def findProbEachWord():
  opProb = {}
  for ke in keys:
    opProb[ke] = {"totalProb": 1/len(keys)}
  #print(opProb)
  for data in whole:
    #print(data)
    for ke in keys:
      if data in classes[ke]:
        op = (1 + 1) / (len(classes[ke]) + len(whole))
        opProb[ke][data] = op
      else:
        op = (0 + 1) / (len(classes[ke]) + len(whole))
        opProb[ke][data] = op
  return opProb
findProbEachWord()
