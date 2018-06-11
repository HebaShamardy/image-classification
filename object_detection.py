
# coding: utf-8

# In[1]:


from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.preprocessing.image import ImageDataGenerator


# In[2]:


classifier = Sequential()


# In[3]:


classifier.add(Conv2D(32, (3,3), input_shape=(64,64,3),activation='relu'))


# In[4]:


classifier.add(MaxPooling2D(pool_size = (2,2)))


# In[5]:


classifier.add(Flatten())


# In[6]:


classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dropout(0.5))


# In[7]:


classifier.add(Dense(units = 1, activation = 'sigmoid'))


# In[8]:


classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                   metrics = ['accuracy'])


# In[9]:


train_datagen = ImageDataGenerator(rotation_range=40,
width_shift_range=0.2,
height_shift_range=0.2,
rescale=1./255,
shear_range=0.2,
zoom_range=0.2,
horizontal_flip=True,
fill_mode='nearest')
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('CNN_Data/training_set',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')
test_set = test_datagen.flow_from_directory('CNN_Data/test_set',
target_size = (64, 64),
batch_size = 32,
class_mode = 'binary')


# In[10]:


classifier.fit_generator(training_set,
steps_per_epoch = 8000,
epochs = 25,
validation_data = test_set,
validation_steps = 2000)


# In[14]:


import numpy as np
from keras.preprocessing import image
test_image = image.load_img('cat_or_dog_1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
prediction = ''
print(result)
if result[0][0] == 1:
    prediction = 'dog'
else:
    prediction = 'cat'

print(prediction)



