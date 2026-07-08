# ==========================================================
# DecodeLabs AI Internship
# Project 3 - Smart Movie Recommendation System
# Developed by: Kshama Jain
# ==========================================================

print("=" * 65)
print("🤖 Welcome to Smart Movie Recommendation System")
print("=" * 65)

name = input("Enter your name: ")

print(f"\nHello {name}! 👋")
print("I will recommend movies based on your preferences.")

movies = [
    {"name":"Avengers: Endgame","genre":"action","mood":"exciting"},
    {"name":"John Wick","genre":"action","mood":"dark"},
    {"name":"Mission Impossible","genre":"action","mood":"exciting"},
    {"name":"3 Idiots","genre":"comedy","mood":"happy"},
    {"name":"The Mask","genre":"comedy","mood":"fun"},
    {"name":"Free Guy","genre":"comedy","mood":"fun"},
    {"name":"The Conjuring","genre":"horror","mood":"scary"},
    {"name":"Insidious","genre":"horror","mood":"dark"},
    {"name":"Titanic","genre":"romance","mood":"emotional"},
    {"name":"The Notebook","genre":"romance","mood":"emotional"},
    {"name":"Interstellar","genre":"science fiction","mood":"thoughtful"},
    {"name":"Inception","genre":"science fiction","mood":"mind blowing"},
    {"name":"Avatar","genre":"science fiction","mood":"exciting"},
    {"name":"Coco","genre":"animation","mood":"family"},
    {"name":"Toy Story","genre":"animation","mood":"fun"},
]

while True:

    print("\n" + "=" * 65)
    print("🎬 MOVIE GENRES")
    print("=" * 65)
    print("1. Action")
    print("2. Comedy")
    print("3. Horror")
    print("4. Romance")
    print("5. Science Fiction")
    print("6. Animation")
    print("7. Exit")

    genre_choice = input("\nChoose a genre (1-7): ")

    if genre_choice == "7":
        print(f"\n👋 Goodbye {name}! Thanks for using the Recommendation System.")
        break

    genre_map = {
        "1":"action",
        "2":"comedy",
        "3":"horror",
        "4":"romance",
        "5":"science fiction",
        "6":"animation"
    }

    if genre_choice not in genre_map:
        print("❌ Invalid choice.")
        continue

    genre = genre_map[genre_choice]

    print("\n😊 HOW ARE YOU FEELING TODAY?")
    print("=" * 65)
    print("1. Excited")
    print("2. Happy")
    print("3. Fun")
    print("4. Emotional")
    print("5. Scared")
    print("6. Thoughtful")
    print("7. Dark")
    print("8. Family Time")

    mood_choice = input("\nChoose your mood (1-8): ")

    mood_map = {
        "1":"exciting",
        "2":"happy",
        "3":"fun",
        "4":"emotional",
        "5":"scary",
        "6":"thoughtful",
        "7":"dark",
        "8":"family"
    }

    if mood_choice not in mood_map:
        print("❌ Invalid choice.")
        continue

    mood = mood_map[mood_choice]

    recommendations = []

    for movie in movies:

        score = 0

        if movie["genre"] == genre:
            score += 2

        if movie["mood"] == mood:
            score += 1

        if score > 0:
            recommendations.append((score, movie["name"]))

    recommendations.sort(reverse=True)

    print("\n" + "=" * 65)
    print("🎯 RECOMMENDED MOVIES FOR YOU")
    print("=" * 65)

    if recommendations:

        for score, movie in recommendations:
            print(f"⭐ {movie:<30} Match Score: {score}/3")

    else:
        print("Sorry! No recommendation found.")

    print("\nWould you like another recommendation?")
    print("1. Yes")
    print("2. No")

    again = input("Enter your choice: ")

    if again != "1":
        print(f"\n😊 Thank you, {name}!")
        print("Hope you enjoy your movie recommendations.")
        print("👋 Have a wonderful day!")
        break