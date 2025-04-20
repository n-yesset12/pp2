import psycopg2

DB_PARAMS = {
    "dbname": "postgres",  
    "user": "postgres",
    "password": "12345",
    "host": "localhost",
    "port": "5432"
}

def create_tables():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()

        # Create users table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            )
        """)

        # Create user_scores table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_scores (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                score INTEGER NOT NULL DEFAULT 0,
                level INTEGER NOT NULL DEFAULT 1,
                saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        conn.commit()
        print("Tables created or already exist.")

    except Exception as e:
        print("Error creating tables:", e)
    finally:
        cur.close()
        conn.close()

def show_scores():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()

        cur.execute("""
            SELECT u.username, s.score, s.level, s.saved_at
            FROM user_scores s
            JOIN users u ON s.user_id = u.id
            ORDER BY s.score DESC
        """)

        results = cur.fetchall()

        print(f"\n{'Username':<15} {'Score':<10} {'Level':<8} {'Saved At'}")
        print("-" * 50)
        for row in results:
            username, score, level, saved_at = row
            print(f"{username:<15} {score:<10} {level:<8} {saved_at}")

        cur.close()
        conn.close()
    except Exception as e:
        print("Error displaying scores:", e)

if __name__ == "__main__":
    create_tables()
    show_scores()


