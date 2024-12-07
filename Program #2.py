import sqlite3

# The add_cities_table adds the Cities table to the database.
def add_cities_table(chr):
    # If the table already exists, drop it.
    chr.execute('DROP TABLE IF EXISTS Cities')

    # Create the table.
    chr.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,
                                        CityName TEXT,
                                        Population REAL)''')


# The add_cities function adds 20 rows to the Cities table.
def add_cities(chr):
    cities_pop = [(1, 'Tokyo', 38001000),
                  (2, 'Delhi', 25703168),
                  (3, 'Shanghai', 23740778),
                  (4, 'Sao Paulo', 21066245),
                  (5, 'Mumbai', 21042538),
                  (6, 'Mexico City', 20998543),
                  (7, 'Beijing', 20383994),
                  (8, 'Osaka', 20237645),
                  (9, 'Cairo', 18771769),
                  (10, 'New York', 18593220),
                  (11, 'Dhaka', 17598228),
                  (12, 'Karachi', 16617644),
                  (13, 'Buenos Aires', 15180176),
                  (14, 'Kolkata', 14864919),
                  (15, 'Istanbul', 14163989),
                  (16, 'Chongqing', 13331579),
                  (17, 'Lagos', 13122829),
                  (18, 'Manila', 12946263),
                  (19, 'Rio de Janeiro', 12902306),
                  (20, 'Guangzhou', 12458130)]

    for row in cities_pop:
        chr.execute('''INSERT INTO Cities (CityID, CityName, Population)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))


# The display_cities function displays the contents of
# the Cities table.
def display_cities(chr):
    print('Contents of cities.db/Cities table:')
    chr.execute('SELECT * FROM Cities')
    results = chr.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

def main():
    con = sqlite3.connect('cur.db')

    chr = con.cursor()

    add_cities_table(chr)

    add_cities(chr)

    con.commit()

    display_cities(chr)

    con.close()

if __name__ == '__main__':
    main()
