model = keras.models.Sequential()
model.add(layers.LSTM(512, input_shape=(maxlen, len(chars)),return_sequences=True))
model.add(layers.LSTM(512, input_shape=(maxlen, len(chars))))
model.add(layers.Dense(len(chars), activation='softmax'))

optimizer = keras.optimizers.Adam(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)