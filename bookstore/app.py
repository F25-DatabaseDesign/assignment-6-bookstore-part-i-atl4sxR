from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
categories = [
    {"id": 1, "name": "Epic Fantasy"},
    {"id": 2, "name": "Science Fiction"},
    {"id": 3, "name": "Translated"},
    {"id": 4, "name": "LGBTQ+"}
]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
books = [
    # Epic Fantasy (categoryId = 1)
    {
        "bookId": 1,
        "categoryId": 1,
        "title": "Assassin’s Apprentice",
        "author": "Robin Hobb",
        "isbn": "9780553573398",
        "price": 14.99,
        "image": "assassinsApprentice.gif",
        "readNow": 1
    },
    {
        "bookId": 2,
        "categoryId": 1,
        "title": "The Way of Kings",
        "author": "Brandon Sanderson",
        "isbn": "9780765365279",
        "price": 19.99,
        "image": "wayOfKings.gif",
        "readNow": 0
    },
    {
        "bookId": 3,
        "categoryId": 1,
        "title": "Empire of the Vampire",
        "author": "Jay Kristoff",
        "isbn": "9781250246516",
        "price": 17.99,
        "image": "empireOfVampire.gif",
        "readNow": 1
    },
    {
        "bookId": 4,
        "categoryId": 1,
        "title": "The Priory of the Orange Tree",
        "author": "Samantha Shannon",
        "isbn": "9781635570304",
        "price": 18.99,
        "image": "prioryOrangeTree.gif",
        "readNow": 0
    },

    # Science Fiction (categoryId = 2)
    {
        "bookId": 5,
        "categoryId": 2,
        "title": "Illuminae",
        "author": "Jay Kristoff",
        "isbn": "9780553499117",
        "price": 12.99,
        "image": "illuminae.jpg",
        "readNow": 1
    },
    {
        "bookId": 6,
        "categoryId": 2,
        "title": "Red Rising",
        "author": "Pierce Brown",
        "isbn": "9780345539809",
        "price": 13.99,
        "image": "redRising.jpg",
        "readNow": 0
    },
    {
        "bookId": 7,
        "categoryId": 2,
        "title": "To Sleep in a Sea of Stars",
        "author": "Christopher Paolini",
        "isbn": "9781250762924",
        "price": 21.99,
        "image": "toSleepInASeaOfStars.jpg",
        "readNow": 1
    },
    {
        "bookId": 8,
        "categoryId": 2,
        "title": "Eye of the World",
        "author": "Robert Jordan",
        "isbn": "9781250251466",
        "price": 16.99,
        "image": "eyeOfTheWorld.gif",
        "readNow": 0
    },

    # Translated (categoryId = 3)
    {
        "bookId": 9,
        "categoryId": 3,
        "title": "Vita Nostra",
        "author": "Sergey Dyachenko",
        "isbn": "9780063054158",
        "price": 15.99,
        "image": "vitaNostra.gif",
        "readNow": 1
    },
    {
        "bookId": 10,
        "categoryId": 3,
        "title": "Before the Coffee Gets Cold",
        "author": "Toshikazu Kawaguchi",
        "isbn": "9781335430991",
        "price": 11.99,
        "image": "beforeCoffeeCold.gif",
        "readNow": 0
    },
    {
        "bookId": 11,
        "categoryId": 3,
        "title": "The Neverending Story",
        "author": "Michael Ende",
        "isbn": "9780140074314",
        "price": 14.49,
        "image": "9780140386332.gif",
        "readNow": 1
    },
    {
        "bookId": 12,
        "categoryId": 3,
        "title": "Memory of Water",
        "author": "Emmi Itäranta",
        "isbn": "9780007529919",
        "price": 13.49,
        "image": "memoryWater.gif",
        "readNow": 0
    },

    # LGBTQ+ Fantasy (categoryId = 4)
    {
        "bookId": 13,
        "categoryId": 4,
        "title": "A Marvellous Light",
        "author": "Freya Marske",
        "isbn": "9781250831798",
        "price": 15.49,
        "image": "marvellousLight.gif",
        "readNow": 1
    },
    {
        "bookId": 14,
        "categoryId": 4,
        "title": "Girls of Paper and Fire",
        "author": "Natasha Nagan",
        "isbn": "9780316561358",
        "price": 14.99,
        "image": "girlsPaperFire.gif",
        "readNow": 0
    },
    {
        "bookId": 15,
        "categoryId": 4,
        "title": "Gideon the Ninth",
        "author": "Tamsyn Muir",
        "isbn": "9781250313188",
        "price": 16.49,
        "image": "gideonNinth.gif",
        "readNow": 1
    },
    {
        "bookId": 16,
        "categoryId": 4,
        "title": "She Who Became the Sun",
        "author": "Shelly Parker-Chan",
        "isbn": "9781250621818",
        "price": 15.99,
        "image": "sheWhoBecameSun.gif",
        "readNow": 0
    }
]



# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template('index.html', categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    selectedCategory = int(request.args.get('categoryId'))

    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = [b for b in books if b["categoryId"] == selectedCategory]
    
    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template('category.html',
                           selectedCategory=selectedCategory,
                           categories=categories,
                           books=selected_books)

@app.route('/search')
def search():
    #Link to the search results page.
    query = request.args.get('q', "").lower()
    results = [
        b for b in books
        if query in b["title"].lower() or query in b["author"].lower()
    ]
    return render_template('search.html', query=query, results=results, categories=categories)

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
