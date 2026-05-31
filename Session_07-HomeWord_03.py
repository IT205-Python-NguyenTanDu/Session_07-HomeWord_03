raws_data = "eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT"

while True:
    print("==== HỆ THỐNG QUẢN LÍ NHÂN SỰ ====")
    print("1. Hiển thị chuỗi dữ liệu gốc\n"
        "2. Chuẩn hóa dữ liệu và in báo cáo\n"
        "3. Tìm kiếm nhân viên theo mã ID\n"
        "4. Thoát chương trình\n")

    choice =  input("Nhập lựa chọn của bạn (1-4): ")
    if not choice.isdigit():
        print("Vui lòng nhập lựa chọn là một số trong khoảng 1-4!\n")
        continue
    choice = int(choice)
    match choice:
        case 1:
            print("==== Dữ liệu gốc ====")
            print(raws_data)
            print("\n")
        case 2:
            print("==== Báo cáo nhân sự ====")
            print(f"{'ID':^10} {'Họ tên':^20} {'{Phòng ban':^15} {'Số điện thoại':^15}")
            print("="*65)
            employees = raws_data.split("|")

            for employees in employees:
                field = employees.split(";")
                id = field[0].strip().upper()
                fullname = field[1].strip().title()
                department = field[3].strip().upper()
                phone = field[2].strip().replace("-", "")

                if phone.isdigit():
                    phone = "******" + phone[-4:]
                else:
                    phone = "Invalid Format"

                print(f"{id:^10} {fullname:^20} {department:^15} {phone:^15}")
                print("=" * 65)
        case 3:
            search_id = input("Nhập ID cần tìm: ")
            search_id = search_id.strip().upper()
            employees = raws_data.split("|")
            flag = False
            for employees in employees:
                field = employees.split(";")
                id = field[0].upper()
                fullname = field[1].strip().title()
                department = field[3].strip().upper()
                phone = field[2].strip().replace("-", "")

                if search_id == id:

                    if phone.isdigit():
                        phone = "******" + phone[-4:]
                    else:
                        phone = "Invalid Format"

                    print("\n===== THÔNG TIN NHÂN VIÊN =====")
                    print(f"ID        : {id}")
                    print(f"Họ tên    : {fullname}")
                    print(f"Điện thoại: {phone}")
                    print(f"Phòng ban : {department}")
                    print("\n")

                    flag = True
                    break

            if not flag:
                print(f"Không tìm  thấy nhân viên có id là {search_id}")

        case 4:
            print("Thoát chương trình!")
            break