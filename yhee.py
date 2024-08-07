def makeDataFromFile(fileDir,fileName):
    students = []
    with open(fileDir+'\\'+fileName,'r') as file:
        #1-1. 파일안의 컨텐츠에 연결하여 모든 라인을 가져온다.
        lines = file.readlines()
    for line in lines:
        student = []
        # 3.가져온 한줄을 분리한다.(콤마로 분리)
        temp = line[:-1].split(',')
        # 4.분리된 데이터를 타입에 맞추어 분리한다
        stdNo = int(temp[0])
        student.append(stdNo)
        student.append(temp[1])
        for ele in temp[2:8]:
            val = int(ele)
            student.append(val)
        # 5.분리한 데이터를 리스트에 저장한다.
        for ele in temp[8:]:
            student.append(ele)
        # 6.리스트를 리스트에 저장한다.
        students.append(student)
    return students





# 지역코드가 B 인 자료에 대하여 (국어점수 + 영어점수)으로 내림차순 정렬했을 때 5번째 학번 출력하시오. 동일값 발생시 학번에 대한 오름차순 정렬하시오.
def solveQuiz1(data):
    #data = makeDataFromFile('.\data','Abc1115.csv')
    quiz1Data = [] #정렬의 대상을 저장할 리스트 선언(지역코드가 B인 학생)
    for temp in data:    # data에 있는 요소를 하나씩 꺼내서 temp에 할당한다.
    #지역코드가 B인 데이터를 quiz1Data에 저장하시오.
        if temp[10] == 'B':    # 지역코드가 B인지 확인한다.
            temp.append(temp[2]+temp[3])    # temp의 마지막에 국어+영어 점수를 추가한다.
            quiz1Data.append(temp)    # quiz1Data의 마지막에 temp를 추가한다.
        pass

    # 정렬 로직
    # quiz1Data에 있는 요소에 대한 index(마지막 제외)[:-1]를 하나씩 꺼내서 index에 할당한다.
    for index,_ in enumerate(quiz1Data[:-1]):
        # quiz1Data에 있는 요소에 대한 index(위의 index에 +1)를 하나씩 꺼내서 idx에, 값은 value에 할당한다.
        for idx,value in enumerate(quiz1Data[index+1:]):    #------------
            # 순서를 결정하는 자리에 있는 학생의 국어+영어
            number = quiz1Data[index][-1]
            # number가 비교하는 학생의 국어 + 영어 점수보다 작은지 확인한다.
            if number < value[-1]:
                temp = quiz1Data[index] #number / 순서 결정할 자리
                quiz1Data[index] = value #i
                quiz1Data[idx+(index+1)] = temp
                #break
            #print(idx,i)
            elif number == value[-1]:
                # 점수가 같을 경우 학번을 오름차순으로 정렬하기
                number = quiz1Data[index][0]
                if number > value[0]:
                    temp = quiz1Data[index] #number
                    quiz1Data[index] = value #i
                    quiz1Data[idx+(index+1)] = temp
                pass
                
            pass

    return quiz1Data[4][0] #5번째 학생(index 4)의 학번(index 0) 정보


data = makeDataFromFile('.\data','Abc1115.csv')

result = solveQuiz1(data)
print(result)