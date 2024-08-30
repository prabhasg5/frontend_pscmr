import sqlite3

# Database file
DB_FILE = 'epics.db'

def create_connection():
    """Create a database connection to the SQLite database specified by DB_FILE."""
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table():
    """Create the items table in the database."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    room_type TEXT NOT NULL,
                    cost_range TEXT NOT NULL,
                    price_min REAL NOT NULL,
                    price_max REAL NOT NULL,
                    link TEXT
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

def insert_item(name, room_type, cost_range, price_min, price_max, link=None):
    """Insert a new item into the items table."""
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO items (name, room_type, cost_range, price_min, price_max, link)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, room_type, cost_range, price_min, price_max, link))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting item: {e}")
        finally:
            conn.close()

def populate_sample_data():
    """Populate the items table with sample data."""
    items = {
        'Living Room': [
            ('Sofa', 'Living Room', 'Medium', 20000, 60000, 'https://www.amazon.in/s?k=amazon+online+sofa'),
             ('Coffee Table', 'Living Room', 'Low', 3000, 12000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Entertainment Center', 'Living Room', 'High', 30000, 80000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Accent Chair', 'Living Room', 'Medium', 10000, 25000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Bookshelf', 'Living Room', 'Low', 7000, 20000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Lamp', 'Living Room', 'Low', 2000, 8000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Rug', 'Living Room', 'Medium', 6000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Side Table', 'Living Room', 'Low', 4000, 12000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('TV Stand', 'Living Room', 'Medium', 10000, 30000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Ottoman', 'Living Room', 'Low', 5000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Clock','Living Room','Low',3000,15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    # Additional Items
    ('Curtains', 'Living Room', 'Medium', 5000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Wall Art', 'Living Room', 'Low', 2000, 10000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Cushions', 'Living Room', 'Low', 1500, 5000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Luxury Sofa', 'Living Room', 'High', 100000, 300000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Designer Coffee Table', 'Living Room', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Premium Entertainment System', 'Living Room', 'High', 150000, 300000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('High-End Accent Chair', 'Living Room', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Antique Bookshelf', 'Living Room', 'High', 80000, 200000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Chandelier', 'Living Room', 'High', 100000, 300000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Handcrafted Rug', 'Living Room', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
        ],
        'Master Bedroom': [
            ('Bed', 'Master Bedroom', 'High', 40000, 100000, 'http://example.com/bed'),
             ('Bed', 'Master Bedroom', 'High', 40000, 100000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Nightstand', 'Master Bedroom', 'Medium', 7000, 25000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Dresser', 'Master Bedroom', 'Medium', 15000, 40000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Wardrobe', 'Master Bedroom', 'High', 45000, 100000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Desk', 'Master Bedroom', 'Medium', 10000, 30000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Desk Chair', 'Master Bedroom', 'Low', 5000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Bedside Lamp', 'Master Bedroom', 'Low', 3000, 8000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Bookcase', 'Master Bedroom', 'Medium', 8000, 25000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Chest of Drawers', 'Master Bedroom', 'Medium', 10000, 25000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Vanity', 'Master Bedroom', 'High', 20000, 60000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    # Additional Items
    ('Mirror', 'Master Bedroom', 'Medium', 5000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Curtains', 'Master Bedroom', 'Low', 5000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Carpet', 'Master Bedroom', 'Low', 7000, 20000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ('Luxury King-Sized Bed', 'Master Bedroom', 'High', 150000, 400000,'https://www.amazon.in/s?k=amazon+online+sofa'),
        ('Designer Wardrobe', 'Master Bedroom', 'High', 200000, 500000,'https://www.amazon.in/s?k=amazon+online+sofa'),
        ('Custom Dresser', 'Master Bedroom', 'High', 80000, 200000,'https://www.amazon.in/s?k=amazon+online+sofa'),
        ('Smart Mirror', 'Master Bedroom', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
        ('Luxury Vanity', 'Master Bedroom', 'High', 100000, 300000,'https://www.amazon.in/s?k=amazon+online+sofa'),
        ('Silk Bedding Set', 'Master Bedroom', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ],
    'Kids_bedroom_items' : [
   ('Bunker Bed', 'Kids Bedroom', 'Medium', 15000, 40000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Nightstand', 'Kids Bedroom', 'Low', 4000, 12000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Dresser', 'Kids Bedroom', 'Medium', 10000, 25000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Wardrobe', 'Kids Bedroom', 'Medium', 15000, 40000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Desk', 'Kids Bedroom', 'Low', 7000, 20000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Desk Chair', 'Kids Bedroom', 'Low', 4000, 12000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Lamp', 'Kids Bedroom', 'Low', 2000, 8000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Bookshelf', 'Kids Bedroom', 'Low', 6000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Chest of Drawers', 'Kids Bedroom', 'Medium', 10000, 25000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Vanity', 'Kids Bedroom', 'Medium', 10000, 25000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Toy Stand', 'Kids Bedroom', 'Medium', 15000, 25000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Study Table', 'Kids Bedroom', 'Medium', 8000, 25000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Curtains', 'Kids Bedroom', 'Low', 3000, 10000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Bean Bag', 'Kids Bedroom', 'Low', 2000, 8000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Custom Bunker Bed', 'Kids Bedroom', 'High', 80000, 200000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Designer Wardrobe', 'Kids Bedroom', 'High', 100000, 300000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Luxury Study Desk', 'Kids Bedroom', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('High-End Toy Stand', 'Kids Bedroom', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Smart Lighting System', 'Kids Bedroom', 'High', 30000, 80000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ],
    'kitchen_items' : [
    ('Stove', 'Kitchen', 'Low', 40000, 80000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Stove', 'Kitchen', 'High', 80000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Chimney', 'Kitchen', 'High', 60000, 120000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Microwave', 'Kitchen', 'Medium', 20000, 40000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Dishwasher', 'Kitchen', 'Medium', 45000, 70000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Refrigerator', 'Kitchen', 'Low', 60000, 250000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Toaster', 'Kitchen', 'Medium', 10000, 20000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Coffee Maker', 'Kitchen', 'High', 8000, 40000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Mixer Grinder', 'Kitchen', 'Low', 5000, 20000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Blender', 'Kitchen', 'Medium', 8000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Water Purifier', 'Kitchen', 'Low', 10000, 30000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Smart Refrigerator', 'Kitchen', 'High', 200000, 500000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Professional Gas Range', 'Kitchen', 'High', 150000, 300000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Built-in Coffee Machine', 'Kitchen', 'High', 80000, 200000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Luxury Marble Countertops', 'Kitchen', 'High', 200000, 500000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Custom Cabinetry', 'Kitchen', 'High', 300000, 800000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ],
    'Dining_room_items' : [
   ('Dining Table', 'Dining Room', 'High', 40000, 100000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Dining Chairs', 'Dining Room', 'Medium', 15000, 40000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Sideboard', 'Dining Room', 'Medium', 20000, 50000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Bar Cabinet', 'Dining Room', 'High', 30000, 80000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Buffet Table', 'Dining Room', 'Medium', 25000, 60000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Dinnerware Set', 'Dining Room', 'Low', 5000, 20000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Cutlery Set', 'Dining Room', 'Low', 3000, 10000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Table Cloth', 'Dining Room', 'Low', 2000, 8000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Wall Art', 'Dining Room', 'Low', 5000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Chandelier', 'Dining Room', 'High', 20000, 50000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Custom Dining Table', 'Dining Room', 'High', 200000, 500000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Designer Dining Chairs', 'Dining Room', 'High', 80000, 200000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Luxury Sideboard', 'Dining Room', 'High', 150000, 400000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Crystal Chandelier', 'Dining Room', 'High', 100000, 300000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Handcrafted Dinnerware Set', 'Dining Room', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ],
    'Home_theatre_items' : [
   ('Projector', 'Home Theatre', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Projector Screen', 'Home Theatre', 'Medium', 15000, 40000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Sound System', 'Home Theatre', 'High', 40000, 100000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Recliner Chair', 'Home Theatre', 'High', 30000, 80000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Popcorn Machine', 'Home Theatre', 'Low', 5000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Home Theatre Lighting', 'Home Theatre', 'Medium', 20000, 50000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Blu-ray Player', 'Home Theatre', 'Medium', 10000, 30000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Media Cabinet', 'Home Theatre', 'Low', 15000, 40000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Acoustic Panels', 'Home Theatre', 'High', 20000, 50000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('4K Laser Projector', 'Home Theatre', 'High', 200000, 500000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('High-End Surround Sound System', 'Home Theatre', 'High', 150000, 400000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Luxury Recliner Chairs', 'Home Theatre', 'High', 100000, 300000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Automated Lighting System', 'Home Theatre', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Premium Acoustic Panels', 'Home Theatre', 'High', 80000, 200000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ],
    'Study_room_items' : [
    ('Desk', 'Study Room', 'Medium', 10000, 30000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Office Chair', 'Study Room', 'Low', 5000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Bookshelf', 'Study Room', 'Low', 6000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Desk Lamp', 'Study Room', 'Low', 2000, 8000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Filing Cabinet', 'Study Room', 'Medium', 15000, 30000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Whiteboard', 'Study Room', 'Low', 3000, 10000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Printer', 'Study Room', 'Medium', 8000, 20000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Rug', 'Study Room', 'Low', 3000, 10000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Curtains', 'Study Room', 'Low', 3000, 10000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Wall Art', 'Study Room', 'Low', 5000, 15000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Ergonomic Executive Chair', 'Study Room', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Luxury Wooden Desk', 'Study Room', 'High', 100000, 300000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Custom Bookshelf', 'Study Room', 'High', 80000, 200000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('High-End Filing Cabinet', 'Study Room', 'High', 50000, 150000,'https://www.amazon.in/s?k=amazon+online+sofa'),
('Smart Desk Lamp', 'Study Room', 'High', 20000, 50000,'https://www.amazon.in/s?k=amazon+online+sofa'),
    ]
    }

    for room_type, item_list in items.items():
        for item_name, room, priority, min_price, max_price, image_link in item_list:
            insert_item(item_name, room, priority, min_price, max_price, image_link)

# Create the table and populate with sample data
create_table()
populate_sample_data()