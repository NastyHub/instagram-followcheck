import instaloader
import json

def get_user_password():
    with open("setting.json") as f:
        jsondata = json.load(f)
        f.close()
    
    return jsondata["username"], jsondata["password"]

user = get_user_password()[0]
password = get_user_password()[1]

print("조금만 기다려 주세요 프로그램 시작 중입니다")
print("제작자: 이찬우")
print("="*50)
L = instaloader.Instaloader()
L.login(user, password)
print("로그인 완료")
print("="*50)
profile = instaloader.Profile.from_username(L.context, "2coldwoo_04")

#Get Follower list
followerlist = []
followeelist = []
resultlist = []

for i in profile.get_followers():
    followerlist.append(i.username)

print(f"{len(followerlist)}명의 팔로워를 찾았습니다")

for i in profile.get_followees():
    followeelist.append(i.username)

print(f"{len(followeelist)}명의 팔로잉을 찾았습니다")

for following in followeelist:
    if following not in followerlist:
        resultlist.append(following)

print("="*50)

with open("result.json", "w") as f:
    json.dump(resultlist, f, indent=2)
    f.close()


print(f"총 결과: {len(resultlist)}명의 사람이 맞팔을 하고 있지 않습니다.\n자세한 내용은 result.json 파일로 저장했습니다.")