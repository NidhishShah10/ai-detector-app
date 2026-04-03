from flask import Flask, render_template, request
from detector import detect_ai
from rephraser import rewrite_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def get_difference_score(original, rewritten):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([original, rewritten])
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    difference = round((1 - similarity) * 100, 2)
    return difference

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    rewritten = None
    difference = None
    conclusion = None
    essay = None

    if request.method == "POST":
        essay = request.form.get("essay")
        action = request.form.get("action")

        if essay and essay.strip():
            if action == "detect":
                result = detect_ai(essay)

            elif action == "rephrase":
                result = detect_ai(essay)
                rewritten = rewrite_text(essay)
                difference = get_difference_score(essay, rewritten)

                if difference > 60:
                    conclusion = "Text was rewritten and differs significantly from the original."
                elif difference > 30:
                    conclusion = "Text was rewritten with notable changes."
                else:
                    conclusion = "Text was rewritten with minor changes."

    return render_template(
        "index.html",
        essay=essay,
        result=result,
        rewritten=rewritten,
        difference=difference,
        conclusion=conclusion
    )

if __name__ == "__main__":
    app.run(debug=True)