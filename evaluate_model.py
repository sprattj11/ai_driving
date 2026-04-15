import os
import base64
import requests
import csv
OLLAMA_URL = "http://localhost:11434/api/generate"

# -----------------------------
# CONFIG
# -----------------------------
DATASET_DIR = "dataset"
OUTPUT_CSV = "results.csv"
MODEL = "gpt-4.1-mini"




# -----------------------------
# HELPERS
# -----------------------------
def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def get_prediction(image_path):
    image_b64 = encode_image(image_path)

    prompt = (
        "You are evaluating a self-driving car scene.\n"
        "First briefly analyze the scene in one sentence. Then output ONLY one word: STOP, SLOW, or GO."
    )

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llava",
            "prompt": prompt,
            "images": [image_b64],
            "stream": False
        }
    )

    result = response.json()["response"].strip().upper()
    return result


# -----------------------------
# MAIN EVALUATION LOOP
# -----------------------------
def run_evaluation():
    results = []
    correct = 0
    total = 0

    for label in os.listdir(DATASET_DIR):
        label_path = os.path.join(DATASET_DIR, label)

        if not os.path.isdir(label_path):
            continue

        for img_name in os.listdir(label_path):
            img_path = os.path.join(label_path, img_name)

            try:
                prediction = get_prediction(img_path)
            except Exception as e:
                print(f"Error on {img_path}: {e}")
                continue

            is_correct = int(prediction == label.upper())

            results.append([img_name, label.upper(), prediction, is_correct])

            total += 1
            correct += is_correct

            print(f"{img_name} | Expected: {label} | Predicted: {prediction}")

    # Save CSV
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["image", "expected", "predicted", "correct"])
        writer.writerows(results)

    # Accuracy
    accuracy = (correct / total) * 100 if total > 0 else 0

    print("\n----------------------")
    print(f"Total Images: {total}")
    print(f"Correct: {correct}")
    print(f"Accuracy: {accuracy:.2f}%")
    print("----------------------")


if __name__ == "__main__":
    run_evaluation()