from db_connection import get_db_connection
import mysql.connector
def insert_group(name, tgName, memberCount, Bio):
    connection = get_db_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()

            # First, check if the group name already exists
            cursor.execute("SELECT * FROM Groups WHERE tgName = %s", (tgName,))
            if cursor.fetchone():
                # If the fetchone() method returns a row, the name exists
                print("This group name already exists, please use a different name or the tgName.")
                return False

            # If the name doesn't exist, proceed with insert
            cursor.execute("INSERT INTO Groups (name, tgName, memberCount, Bio) VALUES (%s, %s, %s, %s)", 
                           (name, tgName, memberCount, Bio))
            connection.commit()
            print("Group inserted successfully.")
            return True
        except mysql.connector.Error as error:
            print(f"Failed to insert data: {error}")
        finally:
            connection.close()
    else:
        print("Failed to get DB connection")

# def insert_place(name, location, difficulty, recommended_season):
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO Places (Name, Location, Difficulty, Recommended_Season) VALUES (%s, %s, %s, %s)",
#                    (name, location, difficulty, recommended_season))
#     connection.commit()
#     connection.close()

# def insert_visit(group_id, place_id, visit_date, price):
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO Visits (Group_ID, Place_ID, Visit_Date, Price) VALUES (%s, %s, %s, %s)",
#                    (group_id, place_id, visit_date, price))
#     connection.commit()
#     connection.close()