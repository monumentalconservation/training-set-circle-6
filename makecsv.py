

# get 25 images of each
# download them
# construst csv with them on

import csv 
import pandas as pd
import urllib.request

images = pd.read_csv('tag-report-circle-6-2020-10-16.csv', index_col=False)
images.columns = ['id', 'date', 'url', 'tag']

def quantify_none(row):
  if row['tag'] == 'none':
    val = 1
  else:
    val = 0
  return val

def quantify_some(row):
  if row['tag'] == 'some':
    val = 1
  else:
    val = 0
  return val

def quantify_alot(row):
  if row['tag'] == 'a lot':
    val = 1
  else:
    val = 0
  return val

def quantify_substantial(row):
  if row['tag'] == 'substantial':
    val = 1
  else:
    val = 0
  return val

def quantify_extensive(row):
  if row['tag'] == 'extensive':
    val = 1
  else:
    val = 0
  return val

def save_image(row):
  print("saving image")
  urllib.request.urlretrieve("https://monument-monitor.herokuapp.com" + row['url'], 'testing-images/' + str(row['id']) + '.jpg')

images['none'] = images.apply(quantify_none, axis=1)
images['some'] = images.apply(quantify_some, axis=1)
images['a lot'] = images.apply(quantify_alot, axis=1)
images['substantial'] = images.apply(quantify_substantial, axis=1)
images['extensive'] = images.apply(quantify_extensive, axis=1)



# none = images.loc[images['none'] == 1][-25:]
# some = images.loc[images['some'] == 1][-25:]
# alot = images.loc[images['a lot'] == 1][-25:]
# substantial = images.loc[images['substantial'] == 1][-25:]
# extensive = images.loc[images['extensive'] == 1][-25:]

# images = pd.concat([none, some, alot, substantial, extensive])
# # save all the images
# images.apply(save_image, axis=1)

# images = images.drop(columns = ['date','url','tag'])
# images.to_csv('image-list.csv', index=False)




# Get some testing images
none = images.loc[images['none'] == 1][:5]
some = images.loc[images['some'] == 1][:5]
alot = images.loc[images['a lot'] == 1][:5]
substantial = images.loc[images['substantial'] == 1][:5]
extensive = images.loc[images['extensive'] == 1][:5]

test_images = pd.concat([none, some, alot, substantial, extensive])
# save all the images
# test_images.apply(save_image, axis=1)

test_images = test_images.drop(columns = ['date','url','tag'])
test_images.to_csv('testing-image-list.csv', index=False)
