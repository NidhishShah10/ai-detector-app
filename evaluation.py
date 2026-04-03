import pandas as pd
from detector import detect_ai

CSV_PATH = "data/ai_human.csv"
TEXT_COLUMN = "text"
LABEL_COLUMN = "label"
MAX_SAMPLES = 10


def load_dataset():
    df = pd.read_csv(CSV_PATH)
    sample_size = min(MAX_SAMPLES, len(df))
    df = df.sample(n=sample_size, random_state=42)
    return df


def evaluate():
    df = load_dataset()

    correct = 0
    total = 0
    skipped = 0

    results = []

    true_human_pred_human = 0
    true_human_pred_ai = 0
    true_ai_pred_human = 0
    true_ai_pred_ai = 0

    for _, row in df.iterrows():
        text = str(row[TEXT_COLUMN])[:2000]
        label_value = row[LABEL_COLUMN]

        if label_value == "AI-generated":
            true_label_str = "AI Generated"
        else:
            true_label_str = "Human Written"

        result = detect_ai(text)

        # Skip if detector did not return a usable score
        if result["score"] is None:
            skipped += 1
            print(f"[{row['id']}] Skipped: {result['label']}")

            results.append({
                "id": row["id"],
                "true_label": true_label_str,
                "pred_label": None,
                "score": None,
                "status": result["label"]
            })
            continue

        pred_label = result["label"]
        score = result["score"]
        total += 1

        if pred_label == true_label_str:
            correct += 1

        if true_label_str == "Human Written" and pred_label == "Human Written":
            true_human_pred_human += 1
        elif true_label_str == "Human Written" and pred_label == "AI Generated":
            true_human_pred_ai += 1
        elif true_label_str == "AI Generated" and pred_label == "Human Written":
            true_ai_pred_human += 1
        elif true_label_str == "AI Generated" and pred_label == "AI Generated":
            true_ai_pred_ai += 1

        results.append({
            "id": row["id"],
            "true_label": true_label_str,
            "pred_label": pred_label,
            "score": score,
            "status": "ok"
        })

        print(f"[{row['id']}] True: {true_label_str} | Pred: {pred_label} | Score: {score:.2f}")

    accuracy = (correct / total) if total > 0 else 0

    print("\nFinal Results")
    print("-------------------")
    print(f"Evaluated samples: {total}")
    print(f"Skipped samples: {skipped}")
    print(f"Accuracy: {accuracy:.2%}")

    print("\nConfusion Matrix")
    print("-------------------")
    print(f"True Human  → Pred Human: {true_human_pred_human}")
    print(f"True Human  → Pred AI:    {true_human_pred_ai}")
    print(f"True AI     → Pred Human: {true_ai_pred_human}")
    print(f"True AI     → Pred AI:    {true_ai_pred_ai}")

    results_df = pd.DataFrame(results)
    results_df.to_csv("results/detection_results.csv", index=False)

    print("\nResults saved to results/detection_results.csv")


if __name__ == "__main__":
    evaluate()