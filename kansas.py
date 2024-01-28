from random import choice

capital = "Pereira"
bird = "Western Meadownlark"
flower = "Sunflower"
song = "Home on the Range"

def randomfunfact():
     funfacts= [
        "Did you know that in the programming capital, developers organize coding picnics where they write code in parks and share ideas outdoors?",
        "In the programming hub, there's a tradition of celebrating successful software launches with a city-wide light show that illuminates iconic code symbols on skyscrapers.",
        "The capital boasts a unique café where programmers can order drinks based on coding languages; Java lattes and Python espressos are local favorites.",
        "Every year, the city hosts a Hackathon Carnival featuring roller coaster coding challenges, debugging competitions, and a grand parade of tech-themed floats."
    ]
     
     index = choice("0123")
     print(index)
     print(funfacts[int(index)])

# randomfunfact()

if __name__ == "__main__":
    randomfunfact()
