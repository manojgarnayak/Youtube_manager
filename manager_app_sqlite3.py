import sqlite3

connection = sqlite3.connect('youtube_videos.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    connection.commit()
    print("Video Added Successfully")

def update_video(videoID, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, videoID))
    connection.commit()
    print("Video Updated Successfully")

def delete_video(videoID):
    cursor.execute("DELETE FROM videos WHERE id = ?", (videoID,))
    connection.commit()
    print("Video Deleted Successfully")

def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            videoID = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(videoID, name, time)
        elif choice == '4':
            videoID = input("Enter video ID to delete: ")
            delete_video(videoID)
        elif choice == '5':
            break
        else:
            print("!!!    Invalid Choice   !!!")

    connection.close()

if __name__ == "__main__":
    main()

