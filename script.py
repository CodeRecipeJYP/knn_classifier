from loadData import loadBatch, loadTest
from solution import suggestLabelWithKnn

batchX, batchY = loadBatch()
testX, testY = loadTest()
data = (batchX, batchY)

print("batchX = {}, batchY = {}".format(batchX.shape, batchY.shape))
print("testX = {}, testY = {}".format(testX.shape, testY.shape))


image = testX[1]
label = testY[1]
print("X = {}, Y = {}".format(image.shape, label))




suggestedLabel = suggestLabelWithKnn(image, data)

if label == suggestedLabel:
  print("correct")
else:
  print("wrong")