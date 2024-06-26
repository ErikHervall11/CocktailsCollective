from app.models import db, Cocktail, CocktailIngredient, User, Ingredient, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_cocktails():
    
    users = User.query.filter(User.id.in_([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])).all()
    ingredients = Ingredient.query.all()

    cocktails = [
        {
            "name": "Mojito",
            "description": "A refreshing minty cocktail",
            "instructions": "Muddle mint leaves with sugar and lime juice. Add rum and top with club soda. Garnish with mint sprig.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/MojitoSeed.jpg",
            "created_by": users[0].id,
            "ingredients": [
                {"name": "Mint Leaves", "amount": "10", "unit": "leaves"},
                {"name": "Sugar Syrup", "amount": "1", "unit": "oz"},
                {"name": "Lime Juice", "amount": "1", "unit": "oz"},
                {"name": "Rum", "amount": "2", "unit": "oz"},
                {"name": "Club Soda", "amount": "Top up", "unit": ""},
            ],
        },
        {
            "name": "Cosmopolitan",
            "description": "A tangy and fruity cocktail",
            "instructions": "Shake vodka, triple sec, cranberry juice, and lime juice with ice. Strain into a chilled glass and garnish with orange twist.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/CosmoSeed.jpg",
            "created_by": users[1].id,
            "ingredients": [
                {"name": "Vodka", "amount": "1.5", "unit": "oz"},
                {"name": "Triple Sec", "amount": "1", "unit": "oz"},
                {"name": "Cranberry Juice", "amount": "1", "unit": "oz"},
                {"name": "Lime Juice", "amount": "0.5", "unit": "oz"},
            ],
        },
        {
            "name": "Pina Colada",
            "description": "A sweet tropical cocktail",
            "instructions": "Blend rum, pineapple juice, and coconut cream with ice. Pour into a glass and garnish with pineapple slice.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/PinaColadaSeed.jpg",
            "created_by": users[2].id,
            "ingredients": [
                {"name": "Rum", "amount": "2", "unit": "oz"},
                {"name": "Pineapple Juice", "amount": "3", "unit": "oz"},
                {"name": "Coconut Cream", "amount": "1", "unit": "oz"},
            ],
        },
        {
            "name": "Margarita",
            "description": "A classic Mexican cocktail",
            "instructions": "Shake tequila, triple sec, and lime juice with ice. Strain into a glass with a salted rim and garnish with lime wedge.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/MargaritaSeed.jpg",
            "created_by": users[3].id,
            "ingredients": [
                {"name": "Tequila", "amount": "2", "unit": "oz"},
                {"name": "Triple Sec", "amount": "1", "unit": "oz"},
                {"name": "Lime Juice", "amount": "1", "unit": "oz"},
            ],
        },
        {
            "name": "Old Fashioned",
            "description": "A classic whiskey cocktail",
            "instructions": "Muddle sugar and bitters with a splash of water. Add whiskey and ice. Stir and garnish with orange twist and cherry.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/OldSeed.jpg",
            "created_by": users[4].id,
            "ingredients": [
                {"name": "Whiskey", "amount": "2", "unit": "oz"},
                {"name": "Angostura Bitters", "amount": "2", "unit": "dashes"},
                {"name": "Sugar Syrup", "amount": "1", "unit": "tsp"},
                {"name": "Water", "amount": "Splash", "unit": ""},
            ],
        },
        {
            "name": "Gin and Tonic",
            "description": "A simple and refreshing cocktail",
            "instructions": "Pour gin into a glass with ice. Top with tonic water and garnish with lime wedge.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/GTSeed.jpg",
            "created_by": users[5].id,
            "ingredients": [
                {"name": "Gin", "amount": "2", "unit": "oz"},
                {"name": "Tonic Water", "amount": "Top up", "unit": ""},
            ],
        },
        {
            "name": "Negroni",
            "description": "A bitter and balanced cocktail",
            "instructions": "Stir gin, sweet vermouth, and Campari with ice. Strain into a glass and garnish with orange twist.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/NegroniSeed.jpg",
            "created_by": users[6].id,
            "ingredients": [
                {"name": "Gin", "amount": "1", "unit": "oz"},
                {"name": "Sweet Vermouth", "amount": "1", "unit": "oz"},
                {"name": "Campari", "amount": "1", "unit": "oz"},
            ],
        },
        {
            "name": "Whiskey Sour",
            "description": "A tangy and smooth cocktail",
            "instructions": "Shake whiskey, lemon juice, and sugar syrup with ice. Strain into a glass and garnish with cherry and orange slice.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/WhiskeySourSeed.jpg",
            "created_by": users[7].id,
            "ingredients": [
                {"name": "Whiskey", "amount": "2", "unit": "oz"},
                {"name": "Lemon Juice", "amount": "1", "unit": "oz"},
                {"name": "Sugar Syrup", "amount": "0.5", "unit": "oz"},
            ],
        },
        {
            "name": "Tequila Sunrise",
            "description": "A colorful and fruity cocktail",
            "instructions": "Pour tequila and orange juice into a glass with ice. Add grenadine and let it settle. Garnish with orange slice and cherry.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/TequilaSunriseSeed.jpg",
            "created_by": users[8].id,
            "ingredients": [
                {"name": "Tequila", "amount": "2", "unit": "oz"},
                {"name": "Orange Juice", "amount": "4", "unit": "oz"},
                {"name": "Grenadine", "amount": "0.5", "unit": "oz"},
            ],
        },
        {
            "name": "Mai Tai",
            "description": "A tropical and exotic cocktail",
            "instructions": "Shake rum, lime juice, triple sec, and orgeat syrup with ice. Strain into a glass with ice and garnish with mint sprig.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/MaiTaiSeed.jpg",
            "created_by": users[9].id,
            "ingredients": [
                {"name": "Rum", "amount": "1.5", "unit": "oz"},
                {"name": "Lime Juice", "amount": "0.75", "unit": "oz"},
                {"name": "Triple Sec", "amount": "0.5", "unit": "oz"},
                {"name": "Orgeat Syrup", "amount": "0.5", "unit": "oz"},
            ],
        },
    {
            "name": "Long Island Iced Tea",
            "description": "A strong and refreshing cocktail",
            "instructions": "Combine vodka, gin, rum, tequila, triple sec, lemon juice, and cola. Serve over ice and garnish with a lemon wedge.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/longislandicedteaseed.jpeg",
            "created_by": users[9].id,
            "ingredients": [
                {"name": "Vodka", "amount": "0.5", "unit": "oz"},
                {"name": "Gin", "amount": "0.5", "unit": "oz"},
                {"name": "Rum", "amount": "0.5", "unit": "oz"},
                {"name": "Tequila", "amount": "0.5", "unit": "oz"},
                {"name": "Triple Sec", "amount": "0.5", "unit": "oz"},
                {"name": "Lemon Juice", "amount": "1", "unit": "oz"},
                {"name": "Cola", "amount": "Top up", "unit": ""},
                {"name": "Lemon Wedge", "amount": "1", "unit": "wedge"},
            ],
        },
        {
            "name": "Aperol Spritz",
            "description": "A light and bubbly cocktail",
            "instructions": "Combine Aperol, prosecco, and soda water in a glass with ice. Garnish with an orange slice.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/aperolspritzseed.jpg",
            "created_by": users[0].id,
            "ingredients": [
                {"name": "Aperol", "amount": "3", "unit": "oz"},
                {"name": "Prosecco", "amount": "3", "unit": "oz"},
                {"name": "Soda Water", "amount": "1", "unit": "oz"},
                {"name": "Orange Slice", "amount": "1", "unit": "slice"},
            ],
        },
        {
            "name": "Bloody Mary",
            "description": "A savory cocktail with tomato juice",
            "instructions": "Mix vodka, tomato juice, lemon juice, Worcestershire sauce, hot sauce, salt, and pepper. Garnish with celery stick and lemon wedge.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/bloodymaryseed.jpg",
            "created_by": users[0].id,
            "ingredients": [
                {"name": "Vodka", "amount": "1.5", "unit": "oz"},
                {"name": "Tomato Juice", "amount": "3", "unit": "oz"},
                {"name": "Lemon Juice", "amount": "0.5", "unit": "oz"},
                {"name": "Worcestershire Sauce", "amount": "2", "unit": "dashes"},
                {"name": "Hot Sauce", "amount": "2", "unit": "dashes"},
                {"name": "Salt", "amount": "Pinch", "unit": ""},
                {"name": "Pepper", "amount": "Pinch", "unit": ""},
                {"name": "Celery Stick", "amount": "1", "unit": "stick"},
                {"name": "Lemon Wedge", "amount": "1", "unit": "wedge"},
            ],
        },
        {
            "name": "Daiquiri",
            "description": "A sweet and sour rum cocktail",
            "instructions": "Shake rum, lime juice, and simple syrup with ice. Strain into a chilled glass.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/Daiquiriseed.jpg",
            "created_by": users[1].id,
            "ingredients": [
                {"name": "Rum", "amount": "2", "unit": "oz"},
                {"name": "Lime Juice", "amount": "1", "unit": "oz"},
                {"name": "Simple Syrup", "amount": "0.75", "unit": "oz"},
            ],
        },
        {
            "name": "Manhattan",
            "description": "A classic whiskey cocktail",
            "instructions": "Stir whiskey, sweet vermouth, and bitters with ice. Strain into a chilled glass and garnish with cherry.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/manhattanseed.jpg",
            "created_by": users[2].id,
            "ingredients": [
                {"name": "Whiskey", "amount": "2", "unit": "oz"},
                {"name": "Sweet Vermouth", "amount": "1", "unit": "oz"},
                {"name": "Angostura Bitters", "amount": "2", "unit": "dashes"},
                {"name": "Cherry", "amount": "1", "unit": ""},
            ],
        },
        {
            "name": "Martini",
            "description": "A classic gin cocktail",
            "instructions": "Stir gin and dry vermouth with ice. Strain into a chilled glass and garnish with olive or lemon twist.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/martiniseed.jpg",
            "created_by": users[3].id,
            "ingredients": [
                {"name": "Gin", "amount": "2", "unit": "oz"},
                {"name": "Dry Vermouth", "amount": "0.5", "unit": "oz"},
                {"name": "Olive", "amount": "1", "unit": ""},
                {"name": "Lemon Twist", "amount": "1", "unit": ""},
            ],
        },
        {
            "name": "Moscow Mule",
            "description": "A spicy and refreshing cocktail",
            "instructions": "Combine vodka, lime juice, and ginger beer in a mug filled with ice. Garnish with lime wedge.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/muleseed.jpg",
            "created_by": users[4].id,
            "ingredients": [
                {"name": "Vodka", "amount": "2", "unit": "oz"},
                {"name": "Lime Juice", "amount": "0.5", "unit": "oz"},
                {"name": "Ginger Beer", "amount": "Top up", "unit": ""},
                {"name": "Lime Wedge", "amount": "1", "unit": "wedge"},
            ],
        },
        {
            "name": "Sangria",
            "description": "A fruity and refreshing wine cocktail",
            "instructions": "Combine red wine, brandy, orange juice, and chopped fruit. Chill and serve over ice.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/sangriaseed.jpg",
            "created_by": users[5].id,
            "ingredients": [
                {"name": "Red Wine", "amount": "1", "unit": "bottle"},
                {"name": "Brandy", "amount": "0.25", "unit": "cup"},
                {"name": "Orange Juice", "amount": "1", "unit": "cup"},
                {"name": "Chopped Fruit", "amount": "1", "unit": "cup"},
            ],
        },
        {
            "name": "Mimosa",
            "description": "A light and bubbly cocktail",
            "instructions": "Combine equal parts champagne and orange juice in a glass.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/mimosaseed.jpg",
            "created_by": users[6].id,
            "ingredients": [
                {"name": "Champagne", "amount": "0.5", "unit": "cup"},
                {"name": "Orange Juice", "amount": "0.5", "unit": "cup"},
            ],
        },
        {
            "name": "Irish Coffee",
            "description": "A warm and creamy cocktail",
            "instructions": "Combine hot coffee, Irish whiskey, sugar, and top with whipped cream.",
            "image_url": "https://cocktail-collective.s3.us-west-1.amazonaws.com/irishcoffeeseed.jpg",
            "created_by": users[7].id,
            "ingredients": [
                {"name": "Hot Coffee", "amount": "1", "unit": "cup"},
                {"name": "Irish Whiskey", "amount": "1.5", "unit": "oz"},
                {"name": "Sugar", "amount": "1", "unit": "tsp"},
                {"name": "Whipped Cream", "amount": "Top", "unit": ""},
            ],
        },
    ]

    for cocktail_data in cocktails:
        cocktail = Cocktail(
            name=cocktail_data["name"],
            description=cocktail_data["description"],
            instructions=cocktail_data["instructions"],
            image_url=cocktail_data["image_url"],
            created_by=cocktail_data["created_by"],
        )
        db.session.add(cocktail)
        db.session.commit()

        for ingredient_data in cocktail_data["ingredients"]:
            ingredient = Ingredient.query.filter_by(name=ingredient_data["name"]).first()
            if ingredient is None:
                ingredient = Ingredient(name=ingredient_data["name"])
                db.session.add(ingredient)
                db.session.commit()

            cocktail_ingredient = CocktailIngredient(
                cocktail_id=cocktail.id,
                ingredient_id=ingredient.id,
                amount=ingredient_data["amount"],
                unit=ingredient_data["unit"],
            )
            db.session.add(cocktail_ingredient)

    db.session.commit()

def undo_cocktails():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cocktails RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cocktails"))
        
    db.session.commit()
