import random # 匯入隨機亂數用


dict50 = {
    "あ":"a","い":"i","う":"u","え":"e","お":"o",
    "か":"ka","き":"ki","く":"ku","け":"ke","こ":"ko",
    "さ":"sa","し":"shi","す":"su","せ":"se","そ":"so",
} #50音字庫

width = 36
print("-"*width)
print("|"+"JP50Train".center(width-2)+"｜")
print("-"*width)
print("|"+"50音隨機出題系統".center(width-9)+"｜")
print("|"+"輸入【 q 】即可退出".center(width-10)+"｜")
print("-"*width)

questions = list(dict50.keys()) #把第3行的字庫拉入list變成列表，.keys是代表要抓字庫的(鍵)五十音，改成value(值)他就會變成抓右邊的讀音

score = 0
total_questions = 0
#答對數、總答題數

while True:
    quiz = random.choice(questions) #隨機拿第15行的列表出題
    correct_answer = dict50[quiz] #用中括號代表查資料，小括弧則是執行，很重要不可以打錯
    
    user_answer = input(f"請問【{quiz}】的羅馬拼音是?") #讓使用者可以填入答案 #f是格式化字串的簡寫，用處是把{}大括弧裡面的變數名稱，替換成變數實際的內容。ex.【{quiz}】 > 【う】
    
    if user_answer.lower() == 'q':
        break #使用者退出輸入q
    
    total_questions += 1
    
    #核對答案(字串比對)
    if user_answer.strip() == correct_answer:
        print("◎ 回答正確!☆")
        score += 1
    else:
        print(f"╳ 錯誤...正確答案是:{correct_answer}")
    accuracy = (score / total_questions) * 100
    print(f"目前正確率:{accuracy:.1f}%")
    