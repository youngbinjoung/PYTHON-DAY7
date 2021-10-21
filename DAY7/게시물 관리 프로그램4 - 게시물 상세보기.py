# 게시판 명령어 입력 : help
# 조건1 : 목록에서 내용은 제외
# 조건2 : 작성자 정보 추가. 값은 일단 모두 익명으로 해주세요.

# add : 게시물 추가
# list : 게시물 목록 조회
# update : 게시물 수정
# delete : 게시물 삭제
# detail : 게시물 상세 조회

# 게시판 명령어 입력 : list

# ==========  게시물 목록  =========
# 번호 : 1    제목 : aaa  
# 번호 : 2    제목 : bbb   
# 번호 : 3    제목 : ccc   
# =================================

# 게시판 명령어 입력 : detail
# 상세보기 할 게시물 번호 입력 : 2

# ==========  게시물 상세 =========
# 번호 : 1 
# 제목 : aaa
# 내용 : aaa
# 작성자 : 익명
# ----- 댓글 -----
# ================================= 


# 게시판 명령어 입력 : detail
# 상세보기 할 게시물 번호 입력 : 3

# ==========  게시물 상세  =========
# 번호 : 3 
# 제목 : ccc
# 내용 : ccc
# 작성자 : 익명
# ----- 댓글 -----
# ================================= 

num=0
list1=[]
gg="없음"
gg2="없음"
delete=-1
while True:
    print("")
    command=input("게시판 명령어 입력 : ")
    print("")
    if command=="help":
        print("add : 게시물 추가")
        print("list : 게시물 조회")
        print("update : 게시물 수정")
        print("delete : 게시물 삭제")
        print("detail : 게시물 상세 조회")
    elif command=="add":
        title=input("제목을 입력해주세요 :")
        body=input("내용을 입력해주세요 :")
        num+=1
        dic1={"번호":num,"제목":title,"내용":body}
        list1.append(dic1)
        print("게시물이 등록되었습니다.")
    elif command=="list":
        print("========== 게시물목록 ===========")
        for a in range(num):
            if a!=delete:
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
    elif command=="delete":
        delete=int(input("삭제할 게시물을 입력하세요 :"))
        delete-=1
        for b in range(num):
            if b==delete: 
               del list1[delete]["번호"]
               gg2="있음"
               print("삭제 성공!")
        if gg2=="없음":
            print("없는 번호입니다.")
        
    elif command=="detail":
        detail=int(input("상세보기 할 게시물번호 입력 :"))
        detail-=1
        print("========== 게시물 상세 ==========")
        print("번호 : {}".format(list1[detail]["번호"]))
        print("제목 : {}".format(list1[detail]["제목"]))
        print("내용 : {}".format(list1[detail]["내용"]))
        print("작성자 : 익명")
        print("----- 댓글 -----")
        print("=================================")
        
