# ...existing code...
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, date

app = Flask(__name__)
# WARNING: replace with a secure random secret key in production
app.secret_key = "Devops-assignment2"

# Dummy data (in-memory) - added image and desc for UI
# ...existing code...
shows = [
    {"id": 1, "title": "RRR", "time": "7:00 PM", "price": 300,
     "desc": "Epic Telugu action drama by S.S. Rajamouli.",
     "image": "https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=1200&auto=format&fit=crop"},
    {"id": 2, "title": "Pushpa: The Rise", "time": "9:00 PM", "price": 280,
     "desc": "Mass action entertainer starring Allu Arjun.",
     "image": "https://images.unsplash.com/photo-1505685296765-3a2736de412f?q=80&w=1200&auto=format&fit=crop"},
    {"id": 3, "title": "Baahubali 2: The Conclusion", "time": "6:30 PM", "price": 350,
     "desc": "Grand historical epic directed by S.S. Rajamouli.",
     "image": "https://images.unsplash.com/photo-1519985176271-adb1088fa94c?q=80&w=1200&auto=format&fit=crop"}
]
# ...existing code...
bookings = []

@app.route('/')
def home():
    featured = shows[:3]
    return render_template('index.html', featured=featured)

@app.route('/book/<int:show_id>', methods=['GET', 'POST'])
def book(show_id):
    show = next((s for s in shows if s['id'] == show_id), None)
    if not show:
        flash('Show not found', 'danger')
        return redirect(url_for('home'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        seats = request.form.get('seats')
        date_str = request.form.get('date')

        # simple validation
        if not all([name, email, seats, date_str]):
            flash('Please fill in all fields', 'danger')
            return redirect(url_for('book', show_id=show_id))

        try:
            seats = int(seats)
            if seats <= 0 or seats > 10:
                raise ValueError
        except ValueError:
            flash('Seats must be a number between 1 and 10', 'danger')
            return redirect(url_for('book', show_id=show_id))

        total = seats * show['price']
        booking_ref = f"BK-{int(datetime.utcnow().timestamp())}"
        booking = {
            "ref": booking_ref,
            "name": name,
            "email": email,
            "show": show['title'],
            "time": show['time'],
            "seats": seats,
            "date": date_str,
            "total": total,
            "image": show.get('image')
        }
        bookings.append(booking)
        return render_template('confirmation.html', booking=booking)

    # pass minimum date (today) to template for date input
    min_date = date.today().isoformat()
    return render_template('book.html', show=show, min_date=min_date)

@app.route('/bookings')
def view_bookings():
    return render_template('bookings.html', bookings=bookings)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
# ...existing code...