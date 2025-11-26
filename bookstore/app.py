from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
categories = [
    [1, "Epic Fantasy"],
    [2, "Science Fiction"],
    [3, "Translated"],
    [4, "LGBTQ+"]
]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
books = [
    # Epic Fantasy (categoryId = 1)
    [1, 1, "Assassin’s Apprentice", "Robin Hobb", "9780553573398", 14.99, "assassinsApprentice.gif", 1],
    [2, 1, "The Way of Kings", "Brandon Sanderson", "9780765365279", 19.99, "wayOfKings.gif", 0],
    [3, 1, "Empire of the Vampire", "Jay Kristoff", "9781250246516", 17.99, "empireOfVampire.gif", 1],
    [4, 1, "The Priory of the Orange Tree", "Samantha Shannon", "9781635570304", 18.99, "prioryOrangeTree.gif", 0],

    # Science Fiction (categoryId = 2)
    [5, 2, "Illuminae", "Jay Kristoff", "9780553499117", 12.99, "illuminae.jpg", 1],
    [6, 2, "Red Rising", "Pierce Brown", "9780345539809", 13.99, "redRising.jpg", 0],
    [7, 2, "To Sleep in a Sea of Stars", "Christopher Paolini", "9781250762924", 21.99, "toSleepInASeaOfStars.jpg", 1],
    [8, 2, "Eye of the World", "Robert Jordan", "9781250251466", 16.99, "eyeOfTheWorld.gif", 0],

    # Translated (categoryId = 3)
    [9, 3, "Vita Nostra", "Sergey Dyachenko", "9780063054158", 15.99, "vitaNostra.gif", 1],
    [10, 3, "Before the Coffee Gets Cold", "Toshikazu Kawaguchi", "9781335430991", 11.99, "beforeCoffeeCold.gif", 0],
    [11, 3, "The Neverending Story", "Michael Ende", "9780140074314", 14.49, "9780140386332.gif", 1],
    [12, 3, "Memory of Water", "Emmi Itäranta", "9780007529919", 13.49, "memoryWater.gif", 0],

    # LGBTQ+ Fantasy (categoryId = 4)
    [13, 4, "A Marvellous Light", "Freya Marske", "9781250831798", 15.49, "marvellousLight.gif", 1],
    [14, 4, "Girls of Paper and Fire", "Natasha Nagan", "9780316561358", 14.99, "girlsPaperFire.gif", 0],
    [15, 4, "Gideon the Ninth", "Tamsyn Muir", "9781250313188", 16.49, "gideonNinth.gif", 1],
    [16, 4, "She Who Became the Sun", "Shelly Parker-Chan", " 9781250621818", 15.99, "sheWhoBecameSun.gif", 0]
]


# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template()

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable

    # Create a new list called selected_books containing a list of books that have the selected category

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template()

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
