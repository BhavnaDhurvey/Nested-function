question_list=["How many continents are there?", "What is capital of India?", "Which course is taught in navgurukul?"]
option_list=[["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
life=[["nine","seven"],["chennai","Delhi"],["Software Engineering","counseling"]]
life_solution=[2, 2, 1]
answer_list=[3,4,1]
def option(index):
    # j=0
    # while j<len(option_list[index]):
    #     print(j+1,option_list[index][j])
    #     j=j+1
    while index<len(question_list):
        print(question_list[index])
        j=0
        while j<len(option_list[index]):
            print(j+1,option_list[index][j])
            j+=1
        user=("without live line","with live line")
        print("choose your choice:")
        print("1.without live")
        print("2.with live line")
        choice=int(input("your choice:"))
        if choice==1:
            user1=int(input("enter your ans"))
            if user1==answer_list[index]:
                return True
        if choice == 2:
            user2=int(input("enter your ans"))
            if choice==life_solution[index]:
               return True
        else:
            return False
def que():
    index=0
    while index<len(question_list):
        print("Q.",index+1,question_list[index],"?")
        result=option(index)
        if result=="no":
            index+=1
        elif result==True:
            print("congratulations")
        else:
            print("you loose")
            break   
        index+=1

def main():
    que()
main()






# question_list=["How many continents are there?", "What is capital of India?", "Which course is taught in navgurukul?"]
# option_list=[["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
# answer_list=[3,4,1]
# def option(index):
#     j=0
#     while j<len(option_list[index]):
#         print(j+1,option_list[index][j])
#         j=j+1
#     user_ans = int(input('.....'))
#     if user_ans==answer_list[index]:
#         return True
#     else:
#         return False
# def que():
#     index=0
#     whiledex<len(question_list):
#         print("Q.",index+1,question_list[index],"?")
#         result=option(index)
#         if result=="no":
#             index+=1
#         elif result==True:
#             print("congratulations")
#         else:
#             print("you loose")
#             break   
#         index+=1

# def main():
#     que()
# main()
# 
# 
# 
# 
# 
#  index<len(question_list):
#         print("Q.",index+1,question_list[index],"?")
#         result=option(index)
#         if result=="no":
#             index+=1
#         elif result==True:
#             print("congratulations")
#         else:
#             print("you loose")
#             break   
#         index+=1

# def main():
#     que()
# main()

# question_list=["how many continents are there?", "what is capital of india?","which course is taught in navgurukul? "]
# option_list=[["1.four","2.nine","3.seven","4.eight"],["1.chandigarh","2.bhopal","3.chennai","4.delhi"],["1.softwere engineering","2.counseling","3.tourism","4.agriculture"]]
# answere_list=[3,4,1]
# def option(index):
#     j=0
#     while j<len(option_list[index]):
#         print(j+1,option_list[index][j])
#         j=j+1
#     user_ans=int(input("enter the option...."))
#     if user_ans==answere_list[index]:
#         return True
#     else:
#         return False
# def que():
#     index=0
#     while index<len(question_list):
#         print("Q.",index+1,question_list[index],"?")
#         result=option(index)
#         if  result=="no":
#             index=index+1
#         elif result==True:
#             print("congratulations")
#         else:
#             print("you loose")
#             break
#         index=index+1
# def main():
#     que()
# main()