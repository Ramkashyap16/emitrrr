import sqlite3

conn = sqlite3.connect('language_game.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS user_progress
             (user_id integer, progress text)''')

# Insert a row of data
c.execute("INSERT INTO user_progress VALUES (1, 'Lesson 1 Complete')")

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
