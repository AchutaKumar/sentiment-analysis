from django.shortcuts import render
from textblob import TextBlob


def home(request):

    result = None
    polarity = None
    subjectivity = None
    polarity_score_10 = None
    subjectivity_score_10 = None
    polarity_width = None
    subjectivity_width = None

    if request.method == "POST":

        text = request.POST.get("text")

        analysis = TextBlob(text)

        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity

        # Convert to 1-10 scale
        polarity_score_10 = (polarity + 1) * 4.5 + 1  # -1 to 1 becomes 1 to 10
        subjectivity_score_10 = subjectivity * 9 + 1  # 0 to 1 becomes 1 to 10

        # Calculate progress bar widths
        polarity_width = (polarity_score_10 - 1) * 10  # Convert 1-10 to 0-100 for width
        subjectivity_width = (subjectivity_score_10 - 1) * 10  # Convert 1-10 to 0-100 for width

        if polarity > 0:
            result = "Positive 😊"

        elif polarity < 0:
            result = "Negative 😞"

        else:
            result = "Neutral 😐"

    return render(request, "index.html", {
        "result": result,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "polarity_score_10": polarity_score_10,
        "subjectivity_score_10": subjectivity_score_10,
        "polarity_width": polarity_width,
        "subjectivity_width": subjectivity_width
    })