import os
import datetime
from datetime import timedelta

# Base directory
base_dir = "/home/ubuntu/wellness_calendar_ultra_simple"

# Start date (April 24, 2025)
start_date = datetime.datetime(2025, 4, 24)

# End date (3 months from start date)
end_date = start_date + timedelta(days=90)

# Dietary styles by month
dietary_styles = {
    4: "Mediterranean (Spring)",  # April
    5: "Mediterranean (Spring)",  # May
    6: "Mediterranean (Summer)",  # June
    7: "Okinawan (Summer)",       # July
}

# Exercise types rotation (7-day cycle)
exercise_types = [
    "Zone 2 Cardio (25-30 minutes)",
    "Strength Training - Upper Body (25-30 minutes)",
    "Rest Day or Light Mobility Work",
    "Zone 2 Cardio (25-30 minutes)",
    "Strength Training - Lower Body (Knee-Friendly) (25-30 minutes)",
    "HIIT or Sprints (20-25 minutes)",
    "Mobility, Animal Flow, or Rope Flow (25-30 minutes)"
]

# Daily quotes
quotes = [
    "\"The first wealth is health.\" - Ralph Waldo Emerson",
    "\"Take care of your body. It's the only place you have to live.\" - Jim Rohn",
    "\"Health is a state of complete harmony of the body, mind, and spirit.\" - B.K.S. Iyengar",
    "\"The greatest wealth is health.\" - Virgil",
    "\"Physical fitness is not only one of the most important keys to a healthy body, it is the basis of dynamic and creative intellectual activity.\" - John F. Kennedy",
    "\"Health is not valued until sickness comes.\" - Thomas Fuller",
    "\"To keep the body in good health is a duty, otherwise we shall not be able to keep our mind strong and clear.\" - Buddha",
    "\"A healthy outside starts from the inside.\" - Robert Urich",
    "\"The groundwork for all happiness is good health.\" - Leigh Hunt",
    "\"Health is a relationship between you and your body.\" - Terri Guillemets",
    "\"Happiness is nothing more than good health and a bad memory.\" - Albert Schweitzer",
    "\"The human body is the best picture of the human soul.\" - Ludwig Wittgenstein",
    "\"Your body hears everything your mind says.\" - Naomi Judd",
    "\"Health is the greatest gift, contentment the greatest wealth, faithfulness the best relationship.\" - Buddha",
    "\"The body is a sacred garment.\" - Martha Graham",
    "\"Nurturing yourself is not selfish – it's essential to your survival and your well-being.\" - Renee Peterson Trudeau",
    "\"Almost everything will work again if you unplug it for a few minutes, including you.\" - Anne Lamott",
    "\"Sleep is that golden chain that ties health and our bodies together.\" - Thomas Dekker",
    "\"Movement is a medicine for creating change in a person's physical, emotional, and mental states.\" - Carol Welch",
    "\"The food you eat can be either the safest and most powerful form of medicine or the slowest form of poison.\" - Ann Wigmore"
]

# Meal plans by dietary style
meal_plans = {
    "Mediterranean (Spring)": [
        {
            "Breakfast": "Greek yogurt with honey, walnuts, and fresh berries",
            "Morning Snack": "Small handful of almonds and an apple",
            "Lunch": "Mediterranean salad with chickpeas, feta, olives, cucumber, tomatoes, and olive oil dressing",
            "Afternoon Snack": "Hummus with carrot and cucumber sticks",
            "Dinner": "Grilled fish with lemon, roasted vegetables, and quinoa"
        },
        {
            "Breakfast": "Overnight oats with Greek yogurt, chia seeds, and fresh fruit",
            "Morning Snack": "Fresh orange and a small piece of cheese",
            "Lunch": "Greek salad with olives, feta, tomatoes, cucumber, and olive oil dressing",
            "Afternoon Snack": "Hummus with carrot and cucumber sticks",
            "Dinner": "Baked cod with tomatoes, olives, and herbs, served with roasted vegetables"
        },
        {
            "Breakfast": "Mediterranean vegetable frittata with whole grain toast",
            "Morning Snack": "Fresh pear and a small piece of cheese",
            "Lunch": "Quinoa bowl with roasted vegetables, chickpeas, and tahini dressing",
            "Afternoon Snack": "Greek yogurt with a drizzle of honey",
            "Dinner": "Grilled Mediterranean vegetables with farro and herb-marinated tofu"
        },
        {
            "Breakfast": "Whole grain toast with avocado and poached eggs",
            "Morning Snack": "Greek yogurt with berries and a drizzle of honey",
            "Lunch": "Quinoa bowl with roasted vegetables, chickpeas, and tahini dressing",
            "Afternoon Snack": "Small handful of mixed nuts and dried apricots",
            "Dinner": "Grilled Mediterranean vegetables with farro and herb-marinated tofu"
        },
        {
            "Breakfast": "Spinach and feta omelet with whole grain toast",
            "Morning Snack": "Fresh pear and a small handful of pistachios",
            "Lunch": "Quinoa salad with roasted vegetables, chickpeas, and lemon-herb dressing",
            "Afternoon Snack": "Greek yogurt with a drizzle of honey and cinnamon",
            "Dinner": "Baked Mediterranean fish with tomatoes, olives, and herbs, served with brown rice"
        }
    ],
    "Mediterranean (Summer)": [
        {
            "Breakfast": "Fresh fruit salad with Greek yogurt and a drizzle of honey",
            "Morning Snack": "Small handful of almonds and fresh cherries",
            "Lunch": "Chilled gazpacho soup with whole grain bread and olive oil",
            "Afternoon Snack": "Tzatziki with cucumber slices and bell pepper strips",
            "Dinner": "Grilled fish with a summer vegetable ratatouille and herb-infused olive oil"
        },
        {
            "Breakfast": "Whole grain toast with ricotta, fresh figs, and honey",
            "Morning Snack": "Watermelon slices with a sprinkle of feta",
            "Lunch": "Mediterranean couscous salad with cucumber, tomatoes, olives, and herbs",
            "Afternoon Snack": "Handful of pistachios and fresh apricots",
            "Dinner": "Grilled chicken souvlaki with tzatziki, tomato, and cucumber salad"
        },
        {
            "Breakfast": "Chilled overnight oats with peaches and almonds",
            "Morning Snack": "Greek yogurt with fresh berries",
            "Lunch": "Niçoise salad with tuna, eggs, olives, and summer vegetables",
            "Afternoon Snack": "Melon wrapped in prosciutto (small portion)",
            "Dinner": "Grilled vegetable and halloumi skewers with quinoa tabbouleh"
        },
        {
            "Breakfast": "Smoothie bowl with Greek yogurt, summer berries, and granola",
            "Morning Snack": "Fresh nectarine and a small piece of cheese",
            "Lunch": "Chickpea and vegetable salad with lemon-herb dressing",
            "Afternoon Snack": "Olives and a small piece of whole grain bread",
            "Dinner": "Grilled Mediterranean vegetables with herb-marinated tofu and farro"
        },
        {
            "Breakfast": "Tomato and basil omelet with whole grain toast",
            "Morning Snack": "Fresh peach and a small handful of walnuts",
            "Lunch": "Greek-style stuffed bell peppers with quinoa, vegetables, and feta",
            "Afternoon Snack": "Cucumber slices with hummus",
            "Dinner": "Grilled fish with summer squash, tomatoes, and herb sauce"
        }
    ],
    "Okinawan (Summer)": [
        {
            "Breakfast": "Miso soup with tofu, seaweed, and green onions",
            "Morning Snack": "Edamame beans with sea salt",
            "Lunch": "Brown rice bowl with stir-fried vegetables and tofu",
            "Afternoon Snack": "Small sweet potato with green tea",
            "Dinner": "Grilled fish with bitter melon stir-fry and brown rice"
        },
        {
            "Breakfast": "Silken tofu with ginger, soy sauce, and green onions",
            "Morning Snack": "Fresh melon slices",
            "Lunch": "Soba noodle salad with cucumber, carrots, and sesame dressing",
            "Afternoon Snack": "Handful of dried goji berries and nuts",
            "Dinner": "Vegetable and tofu stir-fry with shiitake mushrooms and brown rice"
        },
        {
            "Breakfast": "Brown rice porridge with vegetables and a small piece of fish",
            "Morning Snack": "Fresh pineapple chunks",
            "Lunch": "Seaweed salad with cucumber, sesame seeds, and rice vinegar dressing",
            "Afternoon Snack": "Boiled sweet potato with green tea",
            "Dinner": "Miso-glazed fish with stir-fried vegetables and brown rice"
        },
        {
            "Breakfast": "Scrambled tofu with vegetables and a small bowl of miso soup",
            "Morning Snack": "Fresh lychee or dragon fruit",
            "Lunch": "Brown rice onigiri (rice balls) with seaweed and pickled vegetables",
            "Afternoon Snack": "Edamame beans with sea salt",
            "Dinner": "Stir-fried bitter melon, tofu, and vegetables with brown rice"
        },
        {
            "Breakfast": "Okinawan-style vegetable soup with a small bowl of brown rice",
            "Morning Snack": "Fresh papaya slices",
            "Lunch": "Cold soba noodles with dipping sauce and vegetable tempura",
            "Afternoon Snack": "Seaweed snacks and a small sweet potato",
            "Dinner": "Grilled fish with stir-fried vegetables and shirataki noodles"
        }
    ]
}

# Generate day pages
current_date = start_date
day_number = 0

# Create a list to store all day numbers
all_day_numbers = []

while current_date <= end_date:
    # Get month number for dietary style
    month = current_date.month
    dietary_style = dietary_styles.get(month, "Mediterranean (Spring)")  # Default to Mediterranean if month not found
    
    # Get exercise type for this day
    exercise_type = exercise_types[day_number % len(exercise_types)]
    
    # Get meal plan for this dietary style
    meal_plan = meal_plans.get(dietary_style, meal_plans["Mediterranean (Spring)"])[day_number % len(meal_plans.get(dietary_style, meal_plans["Mediterranean (Spring)"]))]
    
    # Get quote for this day
    quote = quotes[day_number % len(quotes)]
    
    # Format date for display
    date_display = current_date.strftime("%B %d, %Y")
    
    # Calculate previous and next day numbers
    prev_day = day_number - 1 if day_number > 0 else 0
    next_day = day_number + 1
    
    # Create HTML file content
    with open(os.path.join(base_dir, "day_template.html"), "r") as template_file:
        template = template_file.read()
    
    # Replace placeholders with actual values
    day_content = template.replace("{{day_number}}", str(day_number))
    day_content = day_content.replace("{{prev_day}}", str(prev_day))
    day_content = day_content.replace("{{next_day}}", str(next_day))
    day_content = day_content.replace("{{date_display}}", date_display)
    day_content = day_content.replace("{{dietary_style}}", dietary_style)
    day_content = day_content.replace("{{exercise_type}}", exercise_type)
    day_content = day_content.replace("{{breakfast}}", meal_plan["Breakfast"])
    day_content = day_content.replace("{{morning_snack}}", meal_plan["Morning Snack"])
    day_content = day_content.replace("{{lunch}}", meal_plan["Lunch"])
    day_content = day_content.replace("{{afternoon_snack}}", meal_plan["Afternoon Snack"])
    day_content = day_content.replace("{{dinner}}", meal_plan["Dinner"])
    day_content = day_content.replace("{{quote}}", quote)
    
    # Write day page to file
    with open(os.path.join(base_dir, f"day{day_number}.html"), "w") as f:
        f.write(day_content)
    
    # Add day number to list
    all_day_numbers.append(day_number)
    
    # Move to next day
    current_date += timedelta(days=1)
    day_number += 1

print(f"Generated {day_number} day pages from {start_date.strftime('%B %d, %Y')} to {(start_date + timedelta(days=day_number-1)).strftime('%B %d, %Y')}")
print(f"Day numbers: {all_day_numbers[0]} to {all_day_numbers[-1]}")
