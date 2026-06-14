from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

# Load pretrained ResNet50 model
model = ResNet50(weights='imagenet')

# Load image
img_path = 'sample.jpg'   # replace with your image name
img = image.load_img(img_path, target_size=(224, 224))

# Convert image to array
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Predict image contents
preds = model.predict(x)

# Decode predictions
predictions = decode_predictions(preds, top=3)[0]

print("\nImage Predictions:")
for pred in predictions:
    print(pred[1], ":", round(pred[2] * 100, 2), "%")

# Generate simple caption
best_caption = predictions[0][1]

print("\nGenerated Caption:")
print("This image contains a", best_caption)