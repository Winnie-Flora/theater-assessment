# Define sections and categories
sections = {
    "A": "Gold",
    "B": "Gold",
    "C": "Gold",
    "D": "Gold",
    "E": "Gold",
    "F": "Gold",
    "G": "Silver",
    "H": "Silver",
    "I": "Silver",
    "J": "Silver",
    "K": "Bronze",
    "L": "Bronze",
    "M": "Bronze",
    "N": "Bronze",
    "O": "Balcony",
    "P": "Balcony",
    "Q": "Balcony",
    "R": "Balcony"
}

def generate_section_with_staircases(section_label, start_seat, end_seat, staircases=[]):
    row = []
    # Insert staircase space after the specified seat
    for seat in range(start_seat, end_seat + 1):
        row.append(f"{section_label}{seat}")
        if seat in staircases:  
            row.append("STAIRCASE")
    return row

# seating arrangements with staircase spaces
theater_seating = {
    "Gold": {
        "A": generate_section_with_staircases("A", 1, 21),
        "B": generate_section_with_staircases("B", 1, 22),
        "C": generate_section_with_staircases("C", 1, 23),
        "D": generate_section_with_staircases("D", 1, 24),
        "E": generate_section_with_staircases("E", 1, 25),
        "F": generate_section_with_staircases("F", 1, 25)
    },
    "Silver": {
        "G": generate_section_with_staircases("G", 1, 28),
        "H": generate_section_with_staircases("H", 1, 30),
        "I": generate_section_with_staircases("I", 1, 30),
        "J": generate_section_with_staircases("J", 1, 28, staircases=[14]), 
    },
    "Bronze": {
        "K": generate_section_with_staircases("K", 1, 30, staircases=[15]),  
        "L": generate_section_with_staircases("L", 1, 14, staircases=[7]),
        "M": generate_section_with_staircases("M", 1, 10, staircases=[5]),
        "N": generate_section_with_staircases("N", 1, 8, staircases=[4])
    },
    "Balcony": {
        "O": generate_section_with_staircases("O", 1, 24, staircases=[15]),  
        "P": generate_section_with_staircases("P", 1, 20),
        "Q": generate_section_with_staircases("Q", 1, 8),
        "R": generate_section_with_staircases("R", 1, 2)
    }
}

# Sample inputs
print("Section J Seating Arrangement:", theater_seating["Silver"]["J"])
print("Section L Seating Arrangement:", theater_seating["Bronze"]["L"])

# Set to store selected seats persistently
selected_seats = set()

# check seat availability
def is_seat_available(section, seat_label):
    if seat_label in selected_seats:
        return False
    # Check if seat is a staircase
    for category, sections in theater_seating.items():
        if section in sections:
            if seat_label in sections[section]:
                return sections[section][sections[section].index(seat_label)] != "STAIRCASE"
    return False

# Function to select a seat
def select_seat(section, row, seat_number):
    seat_label = f"{row}{seat_number}"
    
    # Check if section and row exist in seating model
    category = sections.get(row)
    if not category or section not in theater_seating[category]:
        print("Invalid section or row.")
        return

    # Validate seat availability
    if is_seat_available(section, seat_label):
        # Mark seat as selected
        selected_seats.add(seat_label)
        print(f"Seat {seat_label} in section {section} has been successfully selected.")
    else:
        print(f"Seat {seat_label} is unavailable. Please choose a different seat.")

# Display seating arrangement for a specific section
def display_seating(category):
    print(f"\n{category.upper()} CATEGORY SEATING:")
    for section, seats in theater_seating[category].items():
        row_display = " ".join("[X]" if seat in selected_seats else seat for seat in seats)
        print(f"{section}: {row_display}")

# seat selection system
def main():
    while True:
        print("\nAvailable Categories: Gold, Silver, Bronze")
        category = input("Enter the seating category (Gold/Silver/Bronze) or 'exit' to quit: ").strip().capitalize()
        
        if category == "Exit":
            break
        elif category not in theater_seating:
            print("Invalid category. Please choose from Gold, Silver, or Bronze.")
            continue

        display_seating(category)
        
        section = input("Enter the section (e.g., A, B, C): ").strip().upper()
        row = section  
        try:
            seat_number = int(input("Enter the seat number: "))
            select_seat(section, row, seat_number)
        except ValueError:
            print("Invalid seat number. Please enter a valid number.")
        display_seating(category)

# Run the main function
main()