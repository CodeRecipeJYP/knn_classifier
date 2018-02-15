from __future__ import absolute_import
from loadData import loadBatch, loadTest
from solution import suggestLabelWithKnn

def __init__(self):
  self.testX =
def main():
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


if __name__ == '__main__':
