import onnxruntime as ort
import numpy as np

model_path = r"C:\Users\minhd\Downloads\adde9455d3054c7682196165fecc4e46.ONNX"

session = ort.InferenceSession(model_path)

print("Model inputs:", session.get_inputs())
print("Model outputs:", session.get_outputs())

input_ids = np.array([[101, 2023, 2003, 1037, 7099, 102]])
attention_mask = np.array([[1, 1, 1, 1, 1, 1]])

inputs = {
    'input_ids': input_ids.astype(np.int64),
    'attention_mask': attention_mask.astype(np.int64)
}

outputs = session.run(None, inputs)
logits = outputs[0]

predicted_intent_id = np.argmax(logits)
print("Predicted intent ID:", predicted_intent_id)

