from flask import Flask, render_template, redirect, url_for, jsonify
import json

app =Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/keyword.json")
def stuff2():
    
    data={
            "name": "Keywords",
            "children": [
                {
                    "name": "Food",
                    "children": [
                        {
                            "name": "Restaurants",
                            "children": [
                                {
                                    "name": "Karims Restaurant",
                                    "size": 10
                                },
                                {
                                    "name": "Paradise Restaurant",
                                    "size": 10
                                },
                                {
                                    "name": "Wow! Momo",
                                    "size": 10
                                },
                                {
                                    "name": "Bikanervala",
                                    "size": 10
                                },
                                {
                                    "name": "Haldiram",
                                    "size": 10
                                },
                                {
                                    "name": "Radisson Hotel",
                                    "size": 10
                                },
                                {
                                    "name": "Smokin' Joes Pizzeria",
                                    "size": 10
                                },
                                {
                                    "name": "Barbeque Nation",
                                    "size": 10
                                },
                                {
                                    "name": "Shiv Sagar",
                                    "size": 10
                                },
                                {
                                    "name": "Nirula's Restaurant",
                                    "size": 10
                                },
                                {
                                    "name": "Fassos Food Company",
                                    "size": 10
                                },
                                {
                                    "name": "Saravana Bhavan",
                                    "size": 10
                                },
                                {
                                    "name": "Sagar Ratna",
                                    "size": 10
                                },
                                {
                                    "name": "Parsa's- Food For all",
                                    "size": 10
                                },
                                {
                                    "name": "Jumbo King",
                                    "size": 10
                                },
                                {
                                    "name": "Ratna Cafe",
                                    "size": 10
                                },
                                {
                                    "name": "Kaati Zone",
                                    "size": 10
                                },
                                {
                                    "name": "MTR Foods",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Ice Cream",
                            "children": [
                                {
                                    "name": "Mother Dairy",
                                    "size": 10
                                },
                                {
                                    "name": "Vadilal",
                                    "size": 10
                                },
                                {
                                    "name": "Cream Stone",
                                    "size": 10
                                },
                                {
                                    "name": "Cream Bell",
                                    "size": 10
                                },
                                {
                                    "name": "Natural Ice Cream",
                                    "size": 10
                                },
                                {
                                    "name": "Amul Ice Cream",
                                    "size": 10
                                },
                                {
                                    "name": "Kwality Wall's",
                                    "size": 10
                                },
                                {
                                    "name": "Havmor",
                                    "size": 10
                                },
                                {
                                    "name": "Cream and Fudge",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Chocolate",
                            "children": [
                                {
                                    "name": "Dairy Milk",
                                    "size": 10
                                },
                                {
                                    "name": "5 Star",
                                    "size": 10
                                },
                                {
                                    "name": "Hershey",
                                    "size": 10
                                },
                                {
                                    "name": "Alpenlibe",
                                    "size": 10
                                },
                                {
                                    "name": "Cadbury Gems",
                                    "size": 10
                                },
                                {
                                    "name": "Kacha Mango Bite",
                                    "size": 10
                                },
                                {
                                    "name": "Perk",
                                    "size": 10
                                },
                                {
                                    "name": "Melody",
                                    "size": 10
                                },
                                {
                                    "name": "Cadbury Silk",
                                    "size": 10
                                },
                                {
                                    "name": "Kit Kat",
                                    "size": 10
                                },
                                {
                                    "name": "Munch",
                                    "size": 10
                                },
                                {
                                    "name": "Barone",
                                    "size": 10
                                },
                                {
                                    "name": "Milky Bar",
                                    "size": 10
                                },
                                {
                                    "name": "Ferrero Rocher",
                                    "size": 10
                                },
                                {
                                    "name": "Raffaello",
                                    "size": 10
                                },
                                {
                                    "name": "Snickers",
                                    "size": 10
                                },
                                {
                                    "name": "Mars",
                                    "size": 10
                                },
                                {
                                    "name": "M&M's",
                                    "size": 10
                                },
                                {
                                    "name": "ChocOn ",
                                    "size": 10
                                },
                                {
                                    "name": "Eclairs",
                                    "size": 10
                                },
                                {
                                    "name": "kismi",
                                    "size": 10
                                },
                                {
                                    "name": "Toffichoo",
                                    "size": 10
                                },
                                {
                                    "name": "Just jelly",
                                    "size": 10
                                },
                                {
                                    "name": "Kopiko",
                                    "size": 10
                                },
                                {
                                    "name": "Kisses",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Cookies",
                            "children": [
                                {
                                    "name": "Parle G",
                                    "size": 10
                                },
                                {
                                    "name": "Krackjack",
                                    "size": 10
                                },
                                {
                                    "name": "Monaco",
                                    "size": 10
                                },
                                {
                                    "name": "20-20 Cookies",
                                    "size": 10
                                },
                                {
                                    "name": "Hide & Seek",
                                    "size": 10
                                },
                                {
                                    "name": "Jim Jam",
                                    "size": 10
                                },
                                {
                                    "name": "Bourbon",
                                    "size": 10
                                },
                                {
                                    "name": "Hide & Seek Fab",
                                    "size": 10
                                },
                                {
                                    "name": "Priya Gold Biscuits",
                                    "size": 10
                                },
                                {
                                    "name": "Butter Bite",
                                    "size": 10
                                },
                                {
                                    "name": "Anmol Biscuits",
                                    "size": 10
                                },
                                {
                                    "name": "Mari Gold",
                                    "size": 10
                                },
                                {
                                    "name": "Dark Fantasy",
                                    "size": 10
                                },
                                {
                                    "name": "Good Day",
                                    "size": 10
                                },
                                {
                                    "name": "Unibic",
                                    "size": 10
                                },
                                {
                                    "name": "Oreo",
                                    "size": 10
                                },
                                {
                                    "name": "Bisk farm",
                                    "size": 10
                                },
                                {
                                    "name": "PriyaGold Cheese cracker",
                                    "size": 10
                                },
                                {
                                    "name": "Sunfeast glucose biscuits",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Chips",
                            "children": [
                                {
                                    "name": "Lay's",
                                    "size": 10
                                },
                                {
                                    "name": "Bingo",
                                    "size": 10
                                },
                                {
                                    "name": "Uncle Chips",
                                    "size": 10
                                },
                                {
                                    "name": "Yellow Diamond",
                                    "size": 10
                                },
                                {
                                    "name": "Haldiram's Chips",
                                    "size": 10
                                },
                                {
                                    "name": "Parle's Wafers",
                                    "size": 10
                                },
                                {
                                    "name": "Balaji Wafers",
                                    "size": 10
                                },
                                {
                                    "name": "Cheetos",
                                    "size": 10
                                },
                                {
                                    "name": "Kurkure",
                                    "size": 10
                                },
                                {
                                    "name": "Crax",
                                    "size": 10
                                },
                                {
                                    "name": "Oyes",
                                    "size": 10
                                },
                                {
                                    "name": "Too Yum",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Gum",
                            "children": [
                                {
                                    "name": "boomer",
                                    "size": 10
                                },
                                {
                                    "name": "Big Babol",
                                    "size": 10
                                },
                                {
                                    "name": "Centre Fruit",
                                    "size": 10
                                },
                                {
                                    "name": "Orbit",
                                    "size": 10
                                },
                                {
                                    "name": "Centre Fresh",
                                    "size": 10
                                },
                                {
                                    "name": "Orbit",
                                    "size": 10
                                },
                                {
                                    "name": "Happydent",
                                    "size": 10
                                },
                                {
                                    "name": "Wrigley\u2019s double mint",
                                    "size": 10
                                },
                                {
                                    "name": "Mentos",
                                    "size": 10
                                },
                                {
                                    "name": "Nicotex",
                                    "size": 10
                                },
                                {
                                    "name": "Trident",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Nuts",
                            "children": [
                                {
                                    "name": "Happilo",
                                    "size": 10
                                },
                                {
                                    "name": "Nutty Grities",
                                    "size": 10
                                },
                                {
                                    "name": "Rostaa",
                                    "size": 10
                                },
                                {
                                    "name": "Nutraj",
                                    "size": 10
                                },
                                {
                                    "name": "Vedaka",
                                    "size": 10
                                },
                                {
                                    "name": "Tulsi Dry Fruits",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Food Delivery Apps",
                            "children": [
                                {
                                    "name": "Zomato",
                                    "size": 10
                                },
                                {
                                    "name": "Swiggy",
                                    "size": 10
                                },
                                {
                                    "name": "Deliveroo",
                                    "size": 10
                                },
                                {
                                    "name": "GrubHub",
                                    "size": 10
                                },
                                {
                                    "name": "Dunzo",
                                    "size": 10
                                },
                                {
                                    "name": "Eatfit",
                                    "size": 10
                                },
                                {
                                    "name": "Eatsure",
                                    "size": 10
                                },
                                {
                                    "name": "Box8",
                                    "size": 10
                                },
                                {
                                    "name": "Oven Story",
                                    "size": 10
                                },
                                {
                                    "name": "FreshMenu",
                                    "size": 10
                                },
                                {
                                    "name": "TravelKhana",
                                    "size": 10
                                },
                                {
                                    "name": "EatSure",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Condiments",
                            "children": [
                                {
                                    "name": "Everest",
                                    "size": 10
                                },
                                {
                                    "name": "Maggi",
                                    "size": 10
                                },
                                {
                                    "name": "MDH",
                                    "size": 10
                                },
                                {
                                    "name": "Goldiee",
                                    "size": 10
                                },
                                {
                                    "name": "Badshah Masala",
                                    "size": 10
                                },
                                {
                                    "name": "Ashok Masala",
                                    "size": 10
                                },
                                {
                                    "name": "Maggi",
                                    "size": 10
                                },
                                {
                                    "name": "Kissan",
                                    "size": 10
                                },
                                {
                                    "name": "Suhana Masala",
                                    "size": 10
                                },
                                {
                                    "name": "Smith and Jones",
                                    "size": 10
                                },
                                {
                                    "name": "Heinz",
                                    "size": 10
                                },
                                {
                                    "name": "Catch Masala",
                                    "size": 10
                                },
                                {
                                    "name": "Chingz",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Food Companies",
                            "children": [
                                {
                                    "name": "Parle Argo",
                                    "size": 10
                                },
                                {
                                    "name": "Nestle",
                                    "size": 10
                                },
                                {
                                    "name": "Britannia",
                                    "size": 10
                                },
                                {
                                    "name": "Cadbury",
                                    "size": 10
                                },
                                {
                                    "name": "Amul",
                                    "size": 10
                                },
                                {
                                    "name": "MTR Foods",
                                    "size": 10
                                },
                                {
                                    "name": "KRBL Limited",
                                    "size": 10
                                },
                                {
                                    "name": "Hindustan Unilever",
                                    "size": 10
                                },
                                {
                                    "name": "McCain",
                                    "size": 10
                                },
                                {
                                    "name": "Kissan",
                                    "size": 10
                                },
                                {
                                    "name": "Godrej Bevrages and Foods Limited",
                                    "size": 10
                                },
                                {
                                    "name": "Pepsico India",
                                    "size": 10
                                },
                                {
                                    "name": "Kwality Dairy India Limited",
                                    "size": 10
                                },
                                {
                                    "name": "Hatsun Argo",
                                    "size": 10
                                },
                                {
                                    "name": "Heritage Foods Limited",
                                    "size": 10
                                },
                                {
                                    "name": "Patanjali",
                                    "size": 10
                                },
                                {
                                    "name": "Sunfeast",
                                    "size": 10
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Drinks",
                    "children": [
                        {
                            "name": "Soda",
                            "children": [
                                {
                                    "name": "Coca Cola",
                                    "size": 10
                                },
                                {
                                    "name": "Pepsi",
                                    "size": 10
                                },
                                {
                                    "name": "ThumbsUp",
                                    "size": 10
                                },
                                {
                                    "name": "Fanta",
                                    "size": 10
                                },
                                {
                                    "name": "Maaza",
                                    "size": 10
                                },
                                {
                                    "name": "7UP",
                                    "size": 10
                                },
                                {
                                    "name": "Sprite",
                                    "size": 10
                                },
                                {
                                    "name": "Mirinda",
                                    "size": 10
                                },
                                {
                                    "name": "Limca",
                                    "size": 10
                                },
                                {
                                    "name": "Mountain Dew",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Alcohol",
                            "children": [
                                {
                                    "name": "Tuborg",
                                    "size": 10
                                },
                                {
                                    "name": "Old Monk Liquor & Alcohol Rum",
                                    "size": 10
                                },
                                {
                                    "name": "Officers Choice Liquor & Alcohol",
                                    "size": 10
                                },
                                {
                                    "name": "McDowell\u2019s No.1 Liquor & Alcohol",
                                    "size": 10
                                },
                                {
                                    "name": "Royal Stag",
                                    "size": 10
                                },
                                {
                                    "name": "Imperial Blue Liquor & Alcohol",
                                    "size": 10
                                },
                                {
                                    "name": "Royal Challenge",
                                    "size": 10
                                },
                                {
                                    "name": "Heineken Beer",
                                    "size": 10
                                },
                                {
                                    "name": "Kingfisher",
                                    "size": 10
                                },
                                {
                                    "name": "Blenders Pride",
                                    "size": 10
                                },
                                {
                                    "name": "Carlsberg",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Water",
                            "children": [
                                {
                                    "name": "Bisleri",
                                    "size": 10
                                },
                                {
                                    "name": "Kinley",
                                    "size": 10
                                },
                                {
                                    "name": "Aquafina",
                                    "size": 10
                                },
                                {
                                    "name": "Bailey",
                                    "size": 10
                                },
                                {
                                    "name": "Kingfisher Mineral Water",
                                    "size": 10
                                },
                                {
                                    "name": "Smartwater",
                                    "size": 10
                                },
                                {
                                    "name": "Himalayan Mineral Water.",
                                    "size": 10
                                },
                                {
                                    "name": "Patanjali Divya jal",
                                    "size": 10
                                },
                                {
                                    "name": "Rail Neer",
                                    "size": 10
                                },
                                {
                                    "name": "Qua Mineral Water",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Coffee",
                            "children": [
                                {
                                    "name": "Bru",
                                    "size": 10
                                },
                                {
                                    "name": "Caf\u00e9 Coffee Day",
                                    "size": 10
                                },
                                {
                                    "name": "Flying Squirrel Coffee",
                                    "size": 10
                                },
                                {
                                    "name": "Indian Coffee House",
                                    "size": 10
                                },
                                {
                                    "name": "Chai Point",
                                    "size": 10
                                },
                                {
                                    "name": "Seven Beans Coffee",
                                    "size": 10
                                },
                                {
                                    "name": "Blue Tokai",
                                    "size": 10
                                },
                                {
                                    "name": "Barista Lavazza",
                                    "size": 10
                                },
                                {
                                    "name": "Indian Bean",
                                    "size": 10
                                },
                                {
                                    "name": "Black Baza Coffee",
                                    "size": 10
                                },
                                {
                                    "name": "Country Bean",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Energy Drinks",
                            "children": [
                                {
                                    "name": "Monster Energy Drink",
                                    "size": 10
                                },
                                {
                                    "name": "Gatorade",
                                    "size": 10
                                },
                                {
                                    "name": "Sting",
                                    "size": 10
                                },
                                {
                                    "name": "Enerzal",
                                    "size": 10
                                },
                                {
                                    "name": "Ocean Energy Drink",
                                    "size": 10
                                },
                                {
                                    "name": "Red Bull",
                                    "size": 10
                                },
                                {
                                    "name": "Caf\u00e9 Cuba",
                                    "size": 10
                                },
                                {
                                    "name": "Glucon-D",
                                    "size": 10
                                },
                                {
                                    "name": "Rockstar Energy Drink",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Juice",
                            "children": [
                                {
                                    "name": "Drunken Monkey",
                                    "size": 10
                                },
                                {
                                    "name": "The Thickshake Factory",
                                    "size": 10
                                },
                                {
                                    "name": "Mazza",
                                    "size": 10
                                },
                                {
                                    "name": "Frooti",
                                    "size": 10
                                },
                                {
                                    "name": "Slice",
                                    "size": 10
                                },
                                {
                                    "name": "Real Fruit Juice",
                                    "size": 10
                                },
                                {
                                    "name": "Rasna",
                                    "size": 10
                                },
                                {
                                    "name": "Roohafza",
                                    "size": 10
                                },
                                {
                                    "name": "Minute Maid",
                                    "size": 10
                                },
                                {
                                    "name": "Paper boat",
                                    "size": 10
                                },
                                {
                                    "name": "Safal Fruit Juice",
                                    "size": 10
                                },
                                {
                                    "name": "Tropicana",
                                    "size": 10
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Cars",
                    "children": [
                        {
                            "name": "Cars",
                            "children": [
                                {
                                    "name": "Maruti Suzuki",
                                    "size": 10
                                },
                                {
                                    "name": "Hyundai",
                                    "size": 10
                                },
                                {
                                    "name": "Tata Motors",
                                    "size": 10
                                },
                                {
                                    "name": "Mahindra",
                                    "size": 10
                                },
                                {
                                    "name": "Hero MotoCorp",
                                    "size": 10
                                },
                                {
                                    "name": "Honda Motor Company",
                                    "size": 10
                                },
                                {
                                    "name": "TVS Motor Company",
                                    "size": 10
                                },
                                {
                                    "name": "Bajaj",
                                    "size": 10
                                },
                                {
                                    "name": "Ford",
                                    "size": 10
                                },
                                {
                                    "name": "Toyota",
                                    "size": 10
                                },
                                {
                                    "name": "Volkswagen",
                                    "size": 10
                                },
                                {
                                    "name": "Skoda",
                                    "size": 10
                                },
                                {
                                    "name": "Renault",
                                    "size": 10
                                },
                                {
                                    "name": "Nisson",
                                    "size": 10
                                },
                                {
                                    "name": "BMW",
                                    "size": 10
                                },
                                {
                                    "name": "Rolls Royce",
                                    "size": 10
                                },
                                {
                                    "name": "Jaguar",
                                    "size": 10
                                },
                                {
                                    "name": "Fiat",
                                    "size": 10
                                },
                                {
                                    "name": "Land Rover",
                                    "size": 10
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Electronics",
                    "children": [
                        {
                            "name": "Phones",
                            "children": [
                                {
                                    "name": "Samsung",
                                    "size": 10
                                },
                                {
                                    "name": "Xiaomi",
                                    "size": 10
                                },
                                {
                                    "name": "One-Plus",
                                    "size": 10
                                },
                                {
                                    "name": "Apple",
                                    "size": 10
                                },
                                {
                                    "name": "Vivo",
                                    "size": 10
                                },
                                {
                                    "name": "Oppo",
                                    "size": 10
                                },
                                {
                                    "name": "Motorola",
                                    "size": 10
                                },
                                {
                                    "name": "LG",
                                    "size": 10
                                },
                                {
                                    "name": "Nokia",
                                    "size": 10
                                },
                                {
                                    "name": "HTC",
                                    "size": 10
                                },
                                {
                                    "name": "Google Mobiles",
                                    "size": 10
                                },
                                {
                                    "name": "Sony",
                                    "size": 10
                                },
                                {
                                    "name": "Micromax",
                                    "size": 10
                                },
                                {
                                    "name": "Lava Mobiles",
                                    "size": 10
                                },
                                {
                                    "name": "Videocon",
                                    "size": 10
                                },
                                {
                                    "name": "Gionee",
                                    "size": 10
                                },
                                {
                                    "name": "Asus",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Service Providers",
                            "children": [
                                {
                                    "name": "BSNL",
                                    "size": 10
                                },
                                {
                                    "name": "Jio",
                                    "size": 10
                                },
                                {
                                    "name": "Airtel",
                                    "size": 10
                                },
                                {
                                    "name": "MTNL",
                                    "size": 10
                                },
                                {
                                    "name": "Tata Teleservices",
                                    "size": 10
                                },
                                {
                                    "name": "Vodafone",
                                    "size": 10
                                },
                                {
                                    "name": "Idea",
                                    "size": 10
                                },
                                {
                                    "name": "Docomo",
                                    "size": 10
                                },
                                {
                                    "name": "Reliance",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Computers",
                            "children": [
                                {
                                    "name": "Dell",
                                    "size": 10
                                },
                                {
                                    "name": "HP",
                                    "size": 10
                                },
                                {
                                    "name": "Asus",
                                    "size": 10
                                },
                                {
                                    "name": "Acer",
                                    "size": 10
                                },
                                {
                                    "name": "Toshiba",
                                    "size": 10
                                },
                                {
                                    "name": "Lenovo",
                                    "size": 10
                                },
                                {
                                    "name": "MI",
                                    "size": 10
                                },
                                {
                                    "name": "MIcrosoft",
                                    "size": 10
                                },
                                {
                                    "name": "Intel",
                                    "size": 10
                                },
                                {
                                    "name": "Sony laptops",
                                    "size": 10
                                },
                                {
                                    "name": "MSI",
                                    "size": 10
                                },
                                {
                                    "name": "Razer Laptops",
                                    "size": 10
                                },
                                {
                                    "name": "Acer Predator",
                                    "size": 10
                                },
                                {
                                    "name": "Dell Alienware",
                                    "size": 10
                                },
                                {
                                    "name": "Apple Computers",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Television Brands",
                            "children": [
                                {
                                    "name": "Samsung TV",
                                    "size": 10
                                },
                                {
                                    "name": "Panasonic TV",
                                    "size": 10
                                },
                                {
                                    "name": "Sony TV",
                                    "size": 10
                                },
                                {
                                    "name": "MI TV",
                                    "size": 10
                                },
                                {
                                    "name": "Micromax TV",
                                    "size": 10
                                },
                                {
                                    "name": "LG TV",
                                    "size": 10
                                },
                                {
                                    "name": "Sansui TV",
                                    "size": 10
                                },
                                {
                                    "name": "Philips TV",
                                    "size": 10
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Financial Institutions",
                    "children": [
                        {
                            "name": "Insurance",
                            "children": [
                                {
                                    "name": "Bajaj Allianz",
                                    "size": 10
                                },
                                {
                                    "name": "Birla Sun Life",
                                    "size": 10
                                },
                                {
                                    "name": "HDFC Life",
                                    "size": 10
                                },
                                {
                                    "name": "Exide Life",
                                    "size": 10
                                },
                                {
                                    "name": "LIC",
                                    "size": 10
                                },
                                {
                                    "name": "Max Life",
                                    "size": 10
                                },
                                {
                                    "name": "ICICI Prudential",
                                    "size": 10
                                },
                                {
                                    "name": "PNB Metlife",
                                    "size": 10
                                },
                                {
                                    "name": "Kotak Life",
                                    "size": 10
                                },
                                {
                                    "name": "Tata AIA",
                                    "size": 10
                                },
                                {
                                    "name": "SBI Life",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Banks",
                            "children": [
                                {
                                    "name": "State Bank Of India",
                                    "size": 10
                                },
                                {
                                    "name": "Punjab National Bank",
                                    "size": 10
                                },
                                {
                                    "name": "Bank of Baroda",
                                    "size": 10
                                },
                                {
                                    "name": "Canara Bank",
                                    "size": 10
                                },
                                {
                                    "name": "Union Bank Of India",
                                    "size": 10
                                },
                                {
                                    "name": "Bank of India",
                                    "size": 10
                                },
                                {
                                    "name": "Central Bank of India",
                                    "size": 10
                                },
                                {
                                    "name": "HDFC Bank",
                                    "size": 10
                                },
                                {
                                    "name": "ICICI Bank",
                                    "size": 10
                                },
                                {
                                    "name": "Allahabad Bank",
                                    "size": 10
                                },
                                {
                                    "name": "Axis Bank",
                                    "size": 10
                                },
                                {
                                    "name": "Yes Bank",
                                    "size": 10
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Travel",
                    "children": [
                        {
                            "name": "Airlines",
                            "children": [
                                {
                                    "name": "SpiceJet",
                                    "size": 10
                                },
                                {
                                    "name": "Air India",
                                    "size": 10
                                },
                                {
                                    "name": "Vistara",
                                    "size": 10
                                },
                                {
                                    "name": "Indigo",
                                    "size": 10
                                },
                                {
                                    "name": "Jet Airways",
                                    "size": 10
                                },
                                {
                                    "name": "GoAir",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Travel Companies",
                            "children": [
                                {
                                    "name": "MakeMyTrip",
                                    "size": 10
                                },
                                {
                                    "name": "EaseMyTrip",
                                    "size": 10
                                },
                                {
                                    "name": "OYO",
                                    "size": 10
                                },
                                {
                                    "name": "Goibibo",
                                    "size": 10
                                },
                                {
                                    "name": "East India Travel Co",
                                    "size": 10
                                },
                                {
                                    "name": "Yatra",
                                    "size": 10
                                },
                                {
                                    "name": "The Travel Guru",
                                    "size": 10
                                },
                                {
                                    "name": "Red Bus",
                                    "size": 10
                                },
                                {
                                    "name": "ClearTrip",
                                    "size": 10
                                }
                            ]
                        },
                        {
                            "name": "Resorts",
                            "children": [
                                {
                                    "name": "Club Mahindra",
                                    "size": 10
                                },
                                {
                                    "name": "Jaisalmer Marriott Resort & Spa",
                                    "size": 10
                                },
                                {
                                    "name": "Niraamaya Retreats Backwaters And Beyond",
                                    "size": 10
                                },
                                {
                                    "name": "The Roseate",
                                    "size": 10
                                },
                                {
                                    "name": "ITC Jotels",
                                    "size": 10
                                },
                                {
                                    "name": "The Naini Retreat",
                                    "size": 10
                                },
                                {
                                    "name": "The Oberoi Groups",
                                    "size": 10
                                },
                                {
                                    "name": "Le Meridien Group of Hotels in India",
                                    "size": 10
                                },
                                {
                                    "name": "Train",
                                    "size": 10
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Sports",
                    "children": [
                        {
                            "name": "Equipment",
                            "children": [
                                {
                                    "name": "Nike",
                                    "size": 10
                                },
                                {
                                    "name": "Adidas",
                                    "size": 10
                                },
                                {
                                    "name": "Puma",
                                    "size": 10
                                },
                                {
                                    "name": "HRX",
                                    "size": 10
                                },
                                {
                                    "name": "Reebox",
                                    "size": 10
                                },
                                {
                                    "name": "Perfox",
                                    "size": 10
                                },
                                {
                                    "name": "FILA",
                                    "size": 10
                                },
                                {
                                    "name": "Skechers",
                                    "size": 10
                                },
                                {
                                    "name": "Nivia",
                                    "size": 10
                                },
                                {
                                    "name": "Cosco Sports",
                                    "size": 10
                                },
                                {
                                    "name": "Sareen Sports",
                                    "size": 10
                                },
                                {
                                    "name": "Tyka",
                                    "size": 10
                                },
                                {
                                    "name": "MRF",
                                    "size": 10
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Cosmetics",
                    "children": [
                        {
                            "name": "Cosmetics",
                            "children": [
                                {
                                    "name": "Lakme",
                                    "size": 10
                                },
                                {
                                    "name": "L'Oreal",
                                    "size": 10
                                },
                                {
                                    "name": "Clean and clear",
                                    "size": 10
                                },
                                {
                                    "name": "Fair and Lovely",
                                    "size": 10
                                },
                                {
                                    "name": "Maybelline",
                                    "size": 10
                                },
                                {
                                    "name": "Lotus Herbal",
                                    "size": 10
                                },
                                {
                                    "name": "Engage",
                                    "size": 10
                                },
                                {
                                    "name": "Axe",
                                    "size": 10
                                },
                                {
                                    "name": "Park Evenue",
                                    "size": 10
                                },
                                {
                                    "name": "Denver",
                                    "size": 10
                                },
                                {
                                    "name": "Wild Stone",
                                    "size": 10
                                },
                                {
                                    "name": "Amway",
                                    "size": 10
                                },
                                {
                                    "name": "Fog",
                                    "size": 10
                                },
                                {
                                    "name": "Set Wet",
                                    "size": 10
                                },
                                {
                                    "name": "Sunsilk",
                                    "size": 10
                                },
                                {
                                    "name": "Mamaearth",
                                    "size": 10
                                },
                                {
                                    "name": "Head and Shoulder",
                                    "size": 10
                                },
                                {
                                    "name": "Himalaya Herbals",
                                    "size": 10
                                },
                                {
                                    "name": "Pantene",
                                    "size": 10
                                },
                                {
                                    "name": "Olay",
                                    "size": 10
                                },
                                {
                                    "name": "Calvin Klein",
                                    "size": 10
                                },
                                {
                                    "name": "Lux",
                                    "size": 10
                                },
                                {
                                    "name": "Garnier",
                                    "size": 10
                                },
                                {
                                    "name": "Alle 18",
                                    "size": 10
                                },
                                {
                                    "name": "Jonsons",
                                    "size": 10
                                },
                                {
                                    "name": "Ponds",
                                    "size": 10
                                },
                                {
                                    "name": "Biotique",
                                    "size": 10
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "Clothing",
                    "children": [
                        {
                            "name": "Brands",
                            "children": [
                                {
                                    "name": "Allen Solly",
                                    "size": 10
                                },
                                {
                                    "name": "Raymonds",
                                    "size": 10
                                },
                                {
                                    "name": "Da Milano",
                                    "size": 10
                                },
                                {
                                    "name": "Monte Carlo",
                                    "size": 10
                                },
                                {
                                    "name": "Peter England",
                                    "size": 10
                                },
                                {
                                    "name": "Louis Philippe",
                                    "size": 10
                                },
                                {
                                    "name": "Wood Land",
                                    "size": 10
                                },
                                {
                                    "name": "Bata",
                                    "size": 10
                                },
                                {
                                    "name": "Sparx",
                                    "size": 10
                                },
                                {
                                    "name": "Fab India",
                                    "size": 10
                                },
                                {
                                    "name": "Sketchers",
                                    "size": 10
                                },
                                {
                                    "name": "Campus",
                                    "size": 10
                                },
                                {
                                    "name": "Biba",
                                    "size": 10
                                },
                                {
                                    "name": "Provogue",
                                    "size": 10
                                },
                                {
                                    "name": "Red Chief",
                                    "size": 10
                                },
                                {
                                    "name": "Bahamas",
                                    "size": 10
                                },
                                {
                                    "name": "Gini & Jony",
                                    "size": 10
                                },
                                {
                                    "name": "Flying Machine",
                                    "size": 10
                                }
                            ]
                        }
                    ]
                }
            ]
}

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
