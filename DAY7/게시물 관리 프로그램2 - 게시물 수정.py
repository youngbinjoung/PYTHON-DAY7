# 게시판 명령어 입력 : help
# 조건1 : 수정이 완료되면 다시 게시물 목록을 출력

# add : 게시물 추가
# list : 게시물 목록 조회
# update : 게시물 수정

# 게시판 명령어 입력 : list
# ==========  게시물 목록  ===========
# 번호 : 1    제목 : aaa    내용 : aaa
# 번호 : 2    제목 : bbb    내용 : bbb
# 번호 : 3    제목 : ccc    내용 : ccc
# ===================================

# 게시판 명령어 입력 : update
# 수정할 게시물 번호를 입력 : 4
# 없는 게시물입니다.

# 게시판 명령어 입력 : update
# 수정할 게시물 번호를 입력 : 3
# 제목 : 제목3 
# 내용 : 내용3
# 수정이 완료되었습니다.
# ==========  게시물 목록  =============
# 번호 : 1    제목 : aaa    내용 : aaa
# 번호 : 2    제목 : bbb    내용 : bbb
# 번호 : 3    제목 : 제목3   내용 : 내용3
# ======================================

num=0
list1=[]
gg="없음"
while True:
    print("")
    command=input("게시판 명령어 입력 : ")
    print("")
    if command=="help":
        print("add : 게시물추가")
        print("list : 게시물조회")
        print("update : 게시물수정")
    elif command=="add":
        title=input("제목을 입력해주세요 :")
        body=input("내용을 입력해주세요 :")
        num+=1
        dic1={"번호":num,"제목":title,"내용":body}
        list1.append(dic1)
        print("게시물이 등록되었습니다.")
    elif command=="list":
        print("========== 게시물목록 ==========")
        for a in range(num):
            print("번호 : {}  제목 : {}  내용 : {}".format(list1[a]["번호"],list1[a]["제목"],list1[a]["내용"]))
        print("=================================")
    elif command=="update":
        modify=int(input("수정할 게시물 번호를 입력 : "))
        modify-=1
        for b in range(0,num):
            if b==modify:
                title=input("제목 :")
                body=input("내용 :")
                list1[modify]["제목"]=title
                list1[modify]["내용"]=body
                print("수정이 완료되었습니다.")
                gg="있음"
        if gg=="없음":
            print("없는 게시물입니다.")
        
                
                
