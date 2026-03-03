import json

def load_video():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [""]
    
def save_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print ("*" * 80)
    for id , vid in enumerate(videos, start=1) :
        print (f"{id}. {vid} \n")
    print ("*" * 80)
   

def add_video(videos):
    name = input("enter video name :  ")
    time = input("enter video time :  ")
    videos.append({"name": name , "time": time})
    save_helper(videos)    

def update_video(videos):
    list_all_videos(videos)
    id = int(input("enter video id have you update  :  "))
    if 1 <= id <= len(videos):
        new_name = input("enter new video name :  ")
        new_time = input("enter new video time :  1")
        videos[id - 1] = {"name": new_name, "time": new_time}
        save_helper(videos)
    else :
        print ("invalid choice")

def delete_video(videos):
    list_all_videos(videos)
    id = int(input("please enter id want you delete :  "))
    if 1 <= id <= len(videos):
        del videos[id-1]
        save_helper(videos)
    else :
        print ("please select correct id !")


def main():
    videos = load_video()
    while True:
        print("\n Youtube manager || please enter choice")
        print("1. list all videos")
        print("2. add video")
        print("3. update video")
        print("4. delete video")
        print("5. exit app")
        choice = input ("please enter your choice \n")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()

            
            
