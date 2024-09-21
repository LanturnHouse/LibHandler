import os
from handler.handler import Handler as Handler

class Command:

    def __init__(self, project_path):
        self.project_path = project_path
        self.command = ""
        self.args = []
        pass


    def command_input(self, arg: str):
        parts = arg.split()
        if parts:
            self.command = parts[0]
            self.args = parts[1:] if len(parts) > 1 else []

        # command and arg split test print code
        # print(self.command)
        # print(self.args)



    def help(self, arg: None):
        if not arg:
            print("이 프로그램은 오프라인에서 python의 라이브러리를 핸들링하기 위한 코드입니다.")
            print("LibHandler가 압축하여 라이브러리를 가지고 있다가")
            print("라이브러리가 필요한 프로젝트 폴더에 압축해제하여 추가하는 역할을 수행합니다.")
            print("명령어는 [help, exit, get, lib_list]가 있습니다.")
            print("help [명령어] 로 명령어에 대한 도움말을 확인 가능합니다.")
        if arg == "exit":
            print("프로그램을 종료합니다.")
        if arg == "get":
            print("get [lib-name] 를 통해 LibHandler의 라이브러리를 프로젝트 폴더로 가져옵니다.")
            print("get [lib-name lib-name lib-name] 과 같은 방식으로 여러개의 라이브러리를 가져올 수 있습니다.")
        if arg == "lib_list":
            print("LibHandler가 가지고 있는 라이브러리들을 보여줍니다.")
            print("lib_list, liblst, lib-list 로 실행 가능합니다.")
        else:
            print("존재하지 않는 도움말입니다.")

    def exit(self):
        exit()

    def get(self, lib_name:list):
        
        def has_extension(file_name):
            _, ext = os.path.splitext(file_name)
            return bool(ext)
        
        if not lib_name:
            print("가져올 라이브러리 이름(SN or TAG)를 입력해 주세요.")
            return
        
        lib_name_with_extension = [
            f"{name}.zip" if not has_extension(name) else name for name in lib_name
        ]
        
        Handler.get(self.project_path, lib_name_with_extension)

    def lib_list(self):
        Handler.lib_list(os.path.join(os.getcwd(), 'libs'))



    def run(self):
        if self.command == "help":
            self.help()
        elif self.command == "exit":
            self.exit()
        elif self.command == "get":
            self.get(self.args)
        elif self.command in ["lib_list", "liblist", "lib-list"]:
            self.lib_list()
        else:
            print("!!! 존재하지 않는 명령어입니다 !!!\n!!! 도움말을 얻으려면 [help] 명령어를 입력하십시오 !!!")