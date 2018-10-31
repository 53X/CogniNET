x_train = np.load('Train_X.npy')
y_train = np.load('Train_Y.npy')
x_test = np.load('Val_X.npy')
y_test = np.load('Val_Y.npy')

# defining the recurrent(LSTM) model for classification

import keras
from keras.layers import Input, Dense, LSTM
from keras.models import Model


def lstm_model(output_dim=300, num_classes=40):

    input_layer  = Input(shape=(430, 128))
    lstm1 = LSTM(output_dim, return_sequences=False)(input_layer)
    dense1 = Dense(128, activation='tanh')(lstm1)  
    output = Dense(num_classes, activation='softmax')(dense1)
    model = Model(inputs=input_layer, outputs=output)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

#one-hot-encoding the labels of classes

from keras.utils import to_categorical
y_train = to_categorical(y_train, num_classes=40)
y_test = to_categorical(y_test, num_classes=40)

# defining the keras callbacks to be used while training the network

from keras.callbacks import ModelCheckpoint, EarlyStopping
modelcheckpoint = ModelCheckpoint('lstm_model.h5', save_best_only=True, monitor='val_acc', verbose=1)
earlystopping = EarlyStopping(monitor='val_acc', verbose=1, patience=10)


# creating the model object and putting the model to training and testing  
# we use validation data as test data and vice versa because we are not performing any kind of model selection 

model = lstm_model(output_dim=300, num_classes=40)
print('MODEL TRAINING BEGINNING------------->')
model.fit(x_train, y_train, batch_size=16, epochs=2000, callbacks=[modelcheckpoint, earlystopping], validation_data=(x_test, y_test))
print('EVALUATING MODEL ON TEST SET------------>')
print(model.evaluate(x_test, y_test))