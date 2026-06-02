# ==========================
# HỆ THỐNG QUẢN LÝ NHÂN SỰ
# ==========================

raw_data = (
    " eMP-001; nguyen van a ;0987654321;sale | "
    "Emp-002; Tran Thi B; 0912-345-678 ; mkt | "
    "EMP-003 ; le van C ; 0988abc123 ; IT "
)


def process_phone(phone):
    """
    Chuẩn hóa số điện thoại
    - Xóa dấu '-'
    - Nếu hợp lệ: che 6 số đầu
    - Nếu không hợp lệ: Invalid Format
    """
    phone = phone.strip().replace("-", "")

    if phone.isdigit():
        return "******" + phone[-4:]

    return "Invalid Format"


def parse_employees():
    """
    Chuyển dữ liệu thô thành danh sách nhân viên đã chuẩn hóa
    """
    employee_list = []

    employees = raw_data.split("|")

    for employee in employees:
        fields = employee.split(";")

        employee_id = fields[0].strip().upper()
        name = fields[1].strip().title()
        phone = process_phone(fields[2])
        department = fields[3].strip().upper()

        employee_list.append(
            {
                "id": employee_id,
                "name": name,
                "phone": phone,
                "department": department
            }
        )

    return employee_list


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn: ").strip()

    # Chức năng 1
    if choice == "1":
        print("\nDỮ LIỆU GỐC:")
        print(raw_data)

    # Chức năng 2
    elif choice == "2":
        employee_list = parse_employees()

        print("\nBÁO CÁO NHÂN SỰ")
        print("-" * 70)

        print(
            f"{'ID':<12}"
            f"{'HỌ TÊN':<25}"
            f"{'SỐ ĐIỆN THOẠI':<20}"
            f"{'PHÒNG BAN':<10}"
        )

        print("-" * 70)

        for emp in employee_list:
            print(
                f"{emp['id']:<12}"
                f"{emp['name']:<25}"
                f"{emp['phone']:<20}"
                f"{emp['department']:<10}"
            )

    # Chức năng 3
    elif choice == "3":
        search_id = input("Nhập mã nhân viên: ")

        search_id = search_id.strip().upper()

        employee_list = parse_employees()

        found = False

        for emp in employee_list:
            if emp["id"] == search_id:
                print("\nTHÔNG TIN NHÂN VIÊN")
                print(f"ID: {emp['id']}")
                print(f"Họ tên: {emp['name']}")
                print(f"Số điện thoại: {emp['phone']}")
                print(f"Phòng ban: {emp['department']}")

                found = True
                break

        if not found:
