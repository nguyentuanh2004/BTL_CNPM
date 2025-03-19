import streamlit as st
import pandas as pd

st.markdown("<h2 style='color:darkblue;'>DỰ ĐOÁN KẾT QUẢ HỌC TẬP SINH VIÊN</h1>", unsafe_allow_html=True)
st.header("Thông tin điểm")

mon_hoc = {
    "Năm 1": {
        "Học Kỳ 1": ["Triết học Mác-Lê nin", "Giải tích 1", "Đại số tuyến tính", "Vật lý", "Nhập môn nghành CNTT",
                     "Tin học đại cương", "Kinh tết chính trị Mác-Lê nin"],
        "Học Kỳ 2": ["Chủ nghĩa xã hội khoa học", "Giải tích số", "Giải tích 2", "Xác xuất thống kê",
                     "Kỹ thuật lập trình"]
    },
    "Năm 2": {
        "Học Kỳ 1": ["Tư tưởng Hồ Chí Minh", "Toán rời rạc", "Nguyên lý hệ điều hành", "Kiến trúc và tổ chức máy tính",
                     "Lập trình hướng đối tượng", "Cấu trúc dữ liệu và giải thuật"],
        "Học Kỳ 2": ["Lịch sử Đảng Cộng sản Việt Nam", "Cơ sở dữ liệu", "Phân tích thiết kế thuật toán",
                     "Mạng máy tính", "Công nghệ Java"]
    },
    "Năm 3": {
        "Học Kỳ 1": ["Tiếng Anh Chuyên nghành", "Các phương pháp tối ưu", "An toàn và bảo mật thông tin",
                     "Phân tích thiết kế hướng đối tượng", "Thuật toán và ứng dụng", "Hệ quản trị cơ sở dữ liệu"],
        "Học Kỳ 2": ["Kiến trúc các hệ thống thông tin", "Trí tuệ nhân tạo", "Học máy cơ bản", "Công nghệ phần mềm",
                     "Lập trình web", "Lập trình API"]
    },
    "Năm 4": {
        "Học Kỳ 1": ["Đặc tả phần mềm", "Đảm bảo chất lượng phần mềm", "Thị giác máy tính", "Hệ cơ sở tri thức",
                     "Project 1"],
        "Học Kỳ 2": ["Thực tập", "Đồ án"]
    }
}

# Sidebar chọn năm học
st.sidebar.header("Chọn năm học:")
nam_hoc = st.sidebar.selectbox("Chọn năm học", list(mon_hoc.keys()))

# Lấy danh sách các năm từ Năm 1 đến năm được chọn
nam_hoc_index = list(mon_hoc.keys()).index(nam_hoc)
nam_hoc_hien_thi = list(mon_hoc.keys())[:nam_hoc_index + 1]

# Sidebar chọn học kỳ
hoc_ky_chon = st.sidebar.selectbox("Chọn học kỳ", ["Học Kỳ 1", "Học Kỳ 2"])
hoc_ky_hien_thi = ["Học Kỳ 1", "Học Kỳ 2"] if hoc_ky_chon == "Học Kỳ 2" else ["Học Kỳ 1"]
hien_thi_day_du = hoc_ky_chon == "Học Kỳ 2"

diem = {}

# Duyệt qua tất cả các năm từ Năm 1 đến năm được chọn
for nam in nam_hoc_hien_thi:
    st.sidebar.markdown(f"### {nam}")
    diem[nam] = {
        hoc_ky: {
            mon: st.sidebar.number_input(f"{mon}", 0.0, 10.0, 0.0)
            for mon in mon_hoc[nam].get(hoc_ky, [])
        }
        for hoc_ky in ["Học Kỳ 1", "Học Kỳ 2"]
        if nam != nam_hoc or hien_thi_day_du or hoc_ky in hoc_ky_hien_thi
    }

# Hiển thị bảng điểm
for nam in nam_hoc_hien_thi:
    st.markdown(f"## 📖 {nam}")

    col1, col2 = st.columns(2)
    hoc_ky_list = ["Học Kỳ 1", "Học Kỳ 2"]

    for i, col in enumerate([col1, col2]):
        hoc_ky = hoc_ky_list[i]
        if hoc_ky in diem[nam]:
            with col:
                st.markdown(f"### {hoc_ky}")
                df = pd.DataFrame(list(diem[nam][hoc_ky].items()), columns=["Môn", "Điểm"])
                st.dataframe(df, hide_index=True, use_container_width=True)


# Hàm 1: Dự đoán dựa trên GPA trung bình
def du_doan_gpa(diem):
    diem_list = [diem_so for nam in diem for hoc_ky in diem[nam] for diem_so in diem[nam][hoc_ky].values()]

    gpa = sum(diem_list) / len(diem_list) if diem_list else 0
    danh_hieu = "Xuất sắc" if gpa >= 9 else "Giỏi" if gpa >= 8 else "Khá" if gpa >= 6.5 else "Trung bình"

    return (gpa, "Bạn có khả năng ra trường không đúng hạn.", "error") if gpa < 4 else \
        (gpa, f"Chúc mừng bạn có khả năng ra trường đúng hạn với kết quả **{danh_hieu}**!", "success")


# Hàm 2: Dự đoán dựa trên số môn bị điểm dưới 5
def du_doan_mon_duoi_5(diem):
    diem_list = [diem_so for nam in diem for hoc_ky in diem[nam] for diem_so in diem[nam][hoc_ky].values()]
    so_mon_duoi_5 = sum(1 for d in diem_list if d < 5)

    gpa = sum(diem_list) / len(diem_list) if diem_list else 0
    danh_hieu = "Xuất sắc" if gpa >= 9 else "Giỏi" if gpa >= 8 else "Khá" if gpa >= 6.5 else "Trung bình"

    return (gpa, "Bạn có khả năng ra trường không đúng hạn do có quá nhiều môn bị điểm dưới trung bình.", "error") \
        if so_mon_duoi_5 > 3 else (gpa, f"Chúc mừng bạn có khả năng ra trường với kết quả **{danh_hieu}**!", "success")


# Chọn thuật toán dự đoán
st.markdown("🔍 **Chọn thuật toán dự đoán**")
thuat_toan = st.selectbox("Chọn thuật toán", ["Dựa trên GPA trung bình", "Dựa trên số môn dưới 5"])

# Gọi hàm dự đoán tương ứng
if thuat_toan == "Dựa trên GPA trung bình":
    gpa, ket_qua, status = du_doan_gpa(diem)
else:
    gpa, ket_qua, status = du_doan_mon_duoi_5(diem)

# Hiển thị kết quả dự đoán
st.markdown(f"📊 **GPA của bạn: {gpa:.2f}**")
if status == "error":
    st.error(ket_qua)
else:
    st.success(ket_qua)
