import psycopg2
from dotenv import load_dotenv
import os


def CountData():
    load_dotenv()

    try:
        conn_string = os.environ.get("CONN_STRING")

        # Connect to the database
        conn = psycopg2.connect(conn_string)

        # Create a cursor object
        cur = conn.cursor()

        # Check all tables in DB
        # query = """
        #     SELECT table_name
        #     FROM information_schema.tables
        #     WHERE table_schema = 'public'
        #     ORDER BY table_name;
        # """

        # Create table
        # query = """
        #     CREATE TABLE ValidCodes (
        #         SurveyCode char(30),
        #         Email varchar(255)
        #     );
        # """

        # Select table
        # query = """
        #     SELECT * FROM ValidCodes
        # """

        # Insert table
        # code = '1111 2222 3333 4444 5555 66'
        # email = 'michael8pho@gmail.com'
        # query = """
        #     INSERT INTO ValidCodes 
        #     VALUES ('{}', '{}')
        # """.format(code, email)
        
        # Count rows in table
        query = "SELECT COUNT(*) FROM ValidCodes;"

        # Execute the query
        cur.execute(query)

        # Commit to DB
        conn.commit()

        # Fetch results
        tables = cur.fetchall()
        
        # Print the tables
        # for table in tables:
        #     print(table)

        cur.close()
        conn.close()

        #print(str(tables[0][0]))
        return str(tables[0][0])

    except Exception as e:
        pass
        #print(e)

#CountData()