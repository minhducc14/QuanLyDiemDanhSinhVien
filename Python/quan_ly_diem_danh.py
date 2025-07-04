from datetime import datetime
from tep_json import doc_du_lieu, ghi_du_lieu

TAP_TIN_SINH_VIEN = 'du_lieu_sinh_vien.json'
TAP_TIN_DIEM_DANH = 'du_lieu_diem_danh.json'

# 1 Thêm sinh viên
def them_sinh_vien():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    ma = input("Nhập mã sinh viên: ")
    ten = input("Nhập họ tên sinh viên: ")
    lop = input("Nhập lớp: ")
    danh_sach.append({"ma": ma, "ten": ten, "lop": lop})
    ghi_du_lieu(TAP_TIN_SINH_VIEN, danh_sach)
    print("Đã thêm sinh viên thành công.")

# 2 Cập nhật thông tin sv
def sua_sinh_vien():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    ma = input("Nhập mã sinh viên cần sửa: ")
    for sv in danh_sach:
        if sv['ma'] == ma:
            sv['ten'] = input("Nhập tên mới: ")
            sv['lop'] = input("Nhập lớp mới: ")
            ghi_du_lieu(TAP_TIN_SINH_VIEN, danh_sach)
            print("Đã cập nhật.")
            return
    print("Không tìm thấy sinh viên.")

# 3 Xóa sinh viên
def xoa_sinh_vien():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    ma = input("Nhập mã sinh viên cần xoá: ")
    danh_sach = [sv for sv in danh_sach if sv['ma'] != ma]
    ghi_du_lieu(TAP_TIN_SINH_VIEN, danh_sach)
    print("Đã xoá sinh viên.")

# 4 Tìm sv theo mã
def tim_theo_ma():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    ma = input("Nhập mã sinh viên: ")
    for sv in danh_sach:
        if sv['ma'] == ma:
            print(sv)
            return
    print("Không tìm thấy sinh viên.")

# 5 Tìm sv theo tên
def tim_theo_ten():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    ten = input("Nhập tên cần tìm: ").lower()
    ket_qua = [sv for sv in danh_sach if ten in sv['ten'].lower()]
    for sv in ket_qua:
        print(sv)

# 6 Tìm sv theo lớp
def tim_theo_lop():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    lop = input("Nhập lớp: ")
    for sv in danh_sach:
        if sv['lop'] == lop:
            print(sv)

# 7 Hiển thị ds sv
def hien_thi_danh_sach():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    if not danh_sach:
        print("Danh sách sinh viên trống!")
        return

    print("\nDanh sách sinh viên:")
    print("Mã SV  | Họ tên           | Lớp")
    for sv in danh_sach:
        print(f"{sv['ma_sv']:<6} | {sv['ten']:<15} | {sv['lop']}")

# 8 Sắp xếp theo tên
def sap_xep_theo_ten():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    danh_sach.sort(key=lambda sv: sv['ten'])
    for sv in danh_sach:
        print(sv)

# 9 Sx theo lớp
def sap_xep_theo_lop():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    danh_sach.sort(key=lambda sv: sv['lop'])
    for sv in danh_sach:
        print(sv)

# 10 Thống kê theo lớp
def thong_ke_so_luong_theo_lop():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    thong_ke = {}
    for sv in danh_sach:
        lop = sv['lop']
        thong_ke[lop] = thong_ke.get(lop, 0) + 1
    for lop, so_luong in thong_ke.items():
        print(f"Lớp {lop}: {so_luong} sinh viên")

# 11 Điểm danh theo lớp
def diem_danh_theo_lop():
    ds_sv = doc_du_lieu(TAP_TIN_SINH_VIEN)
    lop = input("Nhập lớp cần điểm danh: ")
    ngay = datetime.today().strftime('%Y-%m-%d')
    danh_sach_lop = [sv for sv in ds_sv if sv['lop'] == lop]
    ghi_nhan = []
    for sv in danh_sach_lop:
        co_mat = input(f"{sv['ten']} ({sv['ma']}): Có mặt? (y/n): ").lower() == 'y'
        ghi_nhan.append({"ma": sv['ma'], "co_mat": co_mat})
    ds_diem_danh = doc_du_lieu(TAP_TIN_DIEM_DANH)
    ds_diem_danh.append({"lop": lop, "ngay": ngay, "danh_sach": ghi_nhan})
    ghi_du_lieu(TAP_TIN_DIEM_DANH, ds_diem_danh)
    print("Đã ghi nhận điểm danh.")

# 12 Điểm dtheo tên
def diem_danh_theo_ten():
    ds_sv = doc_du_lieu(TAP_TIN_SINH_VIEN)
    ten = input("Nhập tên sinh viên: ").lower()
    ket_qua = [sv for sv in ds_sv if ten in sv['ten'].lower()]
    if len(ket_qua) == 0:
        print("Không có sinh viên.")
        return
    if len(ket_qua) > 1:
        for i, sv in enumerate(ket_qua):
            print(f"{i+1}. {sv['ten']} ({sv['ma']}) - {sv['lop']}")
        chon = int(input("Chọn số: ")) - 1
        sv = ket_qua[chon]
    else:
        sv = ket_qua[0]
    co_mat = input(f"{sv['ten']} có mặt? (y/n): ").lower() == 'y'
    ngay = datetime.today().strftime('%Y-%m-%d')
    ds_diem_danh = doc_du_lieu(TAP_TIN_DIEM_DANH)
    for lan in ds_diem_danh:
        if lan['lop'] == sv['lop'] and lan['ngay'] == ngay:
            lan['danh_sach'].append({"ma": sv['ma'], "co_mat": co_mat})
            break
    else:
        ds_diem_danh.append({
            "lop": sv['lop'],
            "ngay": ngay,
            "danh_sach": [{"ma": sv['ma'], "co_mat": co_mat}]
        })
    ghi_du_lieu(TAP_TIN_DIEM_DANH, ds_diem_danh)
    print("Đã điểm danh.")

# 13 Hiển thị dd
def hien_thi_diem_danh():
    du_lieu = doc_du_lieu(TAP_TIN_DIEM_DANH)
    for lan in du_lieu:
        print(f"Lớp: {lan['lop']} - Ngày: {lan['ngay']}")
        for sv in lan['danh_sach']:
            print(f"  {sv['ma']}: {'Có mặt' if sv['co_mat'] else 'Vắng'}")

# 14 TK điểm danh
def thong_ke_diem_danh():
    ds_diem_danh = doc_du_lieu(TAP_TIN_DIEM_DANH)
    thong_ke = {}
    for lan in ds_diem_danh:
        for sv in lan['danh_sach']:
            if sv['ma'] not in thong_ke:
                thong_ke[sv['ma']] = {'co': 0, 'vang': 0}
            if sv['co_mat']:
                thong_ke[sv['ma']]['co'] += 1
            else:
                thong_ke[sv['ma']]['vang'] += 1
    for ma, tt in thong_ke.items():
        print(f"{ma}: Có mặt {tt['co']} lần, Vắng {tt['vang']} lần")

# 15 Lưu file
def luu_file_sinh_vien():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    ghi_du_lieu(TAP_TIN_SINH_VIEN, danh_sach)
    print("Đã lưu.")

# 16 Đọc file
def doc_file_sinh_vien():
    danh_sach = doc_du_lieu(TAP_TIN_SINH_VIEN)
    for sv in danh_sach:
        print(sv)

# 17
def luu_file_diem_danh():
    du_lieu = doc_du_lieu(TAP_TIN_DIEM_DANH)
    ghi_du_lieu(TAP_TIN_DIEM_DANH, du_lieu)
    print("Đã lưu.")

# 18
def doc_file_diem_danh():
    du_lieu = doc_du_lieu(TAP_TIN_DIEM_DANH)
    for dd in du_lieu:
        print(dd)

# 19
def xoa_toan_bo_sinh_vien():
    ghi_du_lieu(TAP_TIN_SINH_VIEN, [])
    print("Đã xoá toàn bộ sinh viên.")

# 20
def xoa_toan_bo_diem_danh():
    ghi_du_lieu(TAP_TIN_DIEM_DANH, [])
    print("Đã xoá toàn bộ điểm danh.")

def main():
    while True:
        print("\n=== MENU QUẢN LÝ ĐIỂM DANH ===")
        print("1. Thêm sinh viên")
        print("2. Sửa sinh viên")
        print("3. Xoá sinh viên")
        print("4. Tìm sinh viên theo mã")
        print("5. Tìm sinh viên theo tên")
        print("6. Tìm sinh viên theo lớp")
        print("7. Hiển thị danh sách sinh viên")
        print("8. Sắp xếp theo tên")
        print("9. Sắp xếp theo lớp")
        print("10. Thống kê số lượng sinh viên theo lớp")
        print("11. Điểm danh theo lớp")
        print("12. Điểm danh theo tên")
        print("13. Hiển thị điểm danh")
        print("14. Thống kê điểm danh")
        print("15. Lưu file sinh viên")
        print("16. Đọc file sinh viên")
        print("17. Lưu file điểm danh")
        print("18. Đọc file điểm danh")
        print("19. Xoá toàn bộ sinh viên")
        print("20. Xoá toàn bộ dữ liệu điểm danh")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == '1':
            them_sinh_vien()
        elif chon == '2':
            sua_sinh_vien()
        elif chon == '3':
            xoa_sinh_vien()
        elif chon == '4':
            tim_theo_ma()
        elif chon == '5':
            tim_theo_ten()
        elif chon == '6':
            tim_theo_lop()
        elif chon == '7':
            hien_thi_danh_sach()
        elif chon == '8':
            sap_xep_theo_ten()
        elif chon == '9':
            sap_xep_theo_lop()
        elif chon == '10':
            thong_ke_so_luong_theo_lop()
        elif chon == '11':
            diem_danh_theo_lop()
        elif chon == '12':
            diem_danh_theo_ten()
        elif chon == '13':
            hien_thi_diem_danh()
        elif chon == '14':
            thong_ke_diem_danh()
        elif chon == '15':
            luu_file_sinh_vien()
        elif chon == '16':
            doc_file_sinh_vien()
        elif chon == '17':
            luu_file_diem_danh()
        elif chon == '18':
            doc_file_diem_danh()
        elif chon == '19':
            xoa_toan_bo_sinh_vien()
        elif chon == '20':
            xoa_toan_bo_diem_danh()
        elif chon == '0':
            print("Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()