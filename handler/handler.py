import os
import shutil
import zipfile



class Handler:

    def get(project_path, args: list):

        libs_folder = os.path.join(os.getcwd(), 'libs')
        for file_name in args:
            source_file = os.path.join(libs_folder, file_name)

            if file_name.endswith('.zip'):
                try:
                    with zipfile.ZipFile(source_file, 'r') as zip_ref:
                        extracted_files = zip_ref.namelist()
                        extraction_folder = project_path
                        
                        can_extract = True
                        for extracted_file in extracted_files:
                            full_extracted_path = os.path.join(extraction_folder, extracted_file)
                            if os.path.exists(full_extracted_path):
                                print(f"압축 해제된 파일 '{full_extracted_path}'이(가) 이미 존재합니다. 압축 해제를 취소합니다.")
                                can_extract = False
                                break
                        
                        if can_extract:
                            zip_ref.extractall(extraction_folder)
                            print(f"파일 '{file_name}'이(가) {extraction_folder}으로 압축이 해제되었습니다.")
                        else:
                            print(f"파일 '{file_name}'의 압축 해제를 취소했습니다.")

                except FileNotFoundError:
                    print(f"원본 파일 '{source_file}'을 찾을 수 없습니다.")
                except zipfile.BadZipFile:
                    print(f"파일 '{source_file}'이(가) 잘못된 zip 파일입니다.")
                except Exception as e:
                    print(f"파일 '{file_name}' 압축 해제 중 오류가 발생했습니다: {e}")
            else:
                destination_file = os.path.join(project_path, file_name)
                if os.path.exists(destination_file):
                    print(f"파일 '{destination_file}'이 이미 존재합니다. 복사를 취소합니다.")
                else:
                    try:
                        shutil.copy(source_file, destination_file)
                        print(f"파일 '{file_name}'이(가) {destination_file}으로 복사되었습니다.")
                    except FileNotFoundError:
                        print(f"원본 파일 '{source_file}'을 찾을 수 없습니다.")
                    except Exception as e:
                        print(f"파일 '{file_name}' 복사 중 오류가 발생했습니다: {e}")

    def lib_list(libs_path):
        
        files = os.listdir(libs_path)
        print("\n")
        print("index │ lib name")
        print("──────┼─────────")
        for index, file in enumerate(files):
            print(f"{index:<5} │ {file}")
        print("\n")
