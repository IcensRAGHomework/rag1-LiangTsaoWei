from student_assignment import demo, generate_hw01, generate_hw02, generate_hw03, generate_hw04

if __name__ == "__main__":
    
    print("Question 1:")
    question1 = "2024年台灣10月紀念日有哪些?"
    response = generate_hw01(question1)
    print(response)
    
    print("Question 2:")
    question2 = "2024年台灣10月紀念日有哪些?"
    response = generate_hw02(question2)
    print(response)
    
    """print("Question 3:")
    question2 = "2024年台灣10月紀念日有哪些?"
    question3 = "根據先前的節日清單，這個節日{\"date\": \"10-31\", \"name\": \"蔣公誕辰紀念日\"}是否有在該月份清單？"
    response = generate_hw03(question2, question3)
    print(response)
    
    print("Question 4:")
    question4 = "請問中華台北的積分是多少"
    response = generate_hw04(question4)
    print(response)"""
    
    
    