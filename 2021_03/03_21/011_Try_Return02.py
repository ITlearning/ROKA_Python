# finally 키워드 활용
def write_text_file(file_name, text):
    try:
        file = open(file_name, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()
        
        
write_text_file("text.txt", "안녕하세요")

# 파일을 여는 것까지는 try 문에서 실행되었지만, return 을 만나 try 구문을 빠져 나갔고, 곧바로 finally 구문이 file을 닫았다.