#CI/CD test change
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            people = int(request.form["people"])
            days = int(request.form["days"])
            nights = int(request.form["nights"])

            transport = float(request.form["transport"])
            hotel = float(request.form["hotel"])
            food = float(request.form["food"])
            activities = float(request.form["activities"])

            if people < 1 or days < 1 or nights < 0:
                raise ValueError

            if min(transport, hotel, food, activities) < 0:
                raise ValueError

            transport_total = transport
            hotel_total = hotel * nights
            food_total = food * people * days
            activities_total = activities

            total = (
                transport_total
                + hotel_total
                + food_total
                + activities_total
            )

            result = {
                "transport": transport_total,
                "hotel": hotel_total,
                "food": food_total,
                "activities": activities_total,
                "total": total,
                "per_person": total / people
            }

        except (ValueError, TypeError):
            error = "Enter valid numbers. People and days must be positive."

    return render_template(
        "index.html", result=result, error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
