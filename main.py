import os
import yaml
import datetime

from handler.command import Command as Command



print("\n\n\n")
print("┌ 현재시간: " + str(datetime.datetime.now()))
print("│ LibHander가 정상적으로 실행되었습니다.")
print("└ 프로그램을 종료하려면 [exit] 명령어를 입력하십시오.")
print("\n\n\n")



while True:
    project_path = str(input("프로젝트의 path를 입력 >>> "))
    if os.path.exists(project_path):
        try:
            files = os.listdir(project_path)
            break
        except:
            print("프로젝트가 존재하나 접근하는데 실패하였습니다.")
    else:
        if project_path == "exit":
            exit()
        print(f"'{project_path}' 프로젝트가 존재하지 않습니다.")



print("프로젝트에 성공적으로 접근하였습니다.")
print("명령어를 사용하여 작업을 시작할 수 있습니다.")


command = Command(project_path)

while True:
    command_input = str(input(">>> "))
    try:
        command.command_input(command_input)
        command.run()
    except Exception as e:
        print(f"명령어를 실행도중 에러가 발생하였습니다.\n{e}")

    # command.command_input(command_input)
    # command.run()