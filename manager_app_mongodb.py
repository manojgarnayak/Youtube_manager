import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.lxl3fsq.mongodb.net/", tlsAllowInvalidCertificate=True)
# Not a good practise

db = client["manager"]
video_collection = db["videos"]

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(videoID, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(videoID)},
        {'$set': {"name": new_name, "time": new_time}}
    )

def delete_video(videoID):
    video_collection.delete_one({"_id": ObjectId(videoID)})

def main():
    while True:
        print("\n Manager App")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
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

if __name__ == "__main__":
    main()