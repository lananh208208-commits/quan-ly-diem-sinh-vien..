import streamlit as st
import pandas as pd

# Tiêu đề ứng dụng
st.set_page_config(page_title="QUẢN LÝ ĐIỂM SINH VIÊN-", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN-")

# Dữ liệu 10 sinh viên theo bài Python
danh_sach = [
    {"Họ tên": "Nguyễn Văn An", "Chuyên cần": 9, "Giữa kỳ": 8, "Cuối kỳ": 9},
    {"Họ tên": "Trần Thị Bình", "Chuyên cần": 8, "Giữa kỳ": 7, "Cuối kỳ": 8},
    {"Họ tên": "Lê Hoàng Nam", "Chuyên cần": 10, "Giữa kỳ": 9, "Cuối kỳ": 9},
    {"Họ tên": "Phạm Thị Lan", "Chuyên cần": 7, "Giữa kỳ": 6, "Cuối kỳ": 7},
    {"Họ tên": "Hoàng Minh Đức", "Chuyên cần": 8, "Giữa kỳ": 8, "Cuối kỳ": 8},
    {"Họ tên": "Võ Ngọc Anh", "Chuyên cần": 9, "Giữa kỳ": 8, "Cuối kỳ": 9},
    {"Họ tên": "Đặng Quốc Huy", "Chuyên cần": 6, "Giữa kỳ": 7, "Cuối kỳ": 6},
    {"Họ tên": "Bùi Thị Mai", "Chuyên cần": 10, "Giữa kỳ": 9, "Cuối kỳ": 10},
    {"Họ tên": "Đỗ Thành Công", "Chuyên cần": 7, "Giữa kỳ": 6, "Cuối kỳ": 7},
    {"Họ tên": "Nguyễn Thị Hoa", "Chuyên cần": 9, "Giữa kỳ": 8, "Cuối kỳ": 9},
]

df = pd.DataFrame(danh_sach)

# Tính điểm tổng kết: 20% chuyên cần + 30% giữa kỳ + 50% cuối kỳ
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# Bảng điểm
st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df, use_container_width=True, hide_index=True)

# Thống kê chung
diem_tb = df["Tổng kết"].mean()
sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]
so_sv_dat = int((df["Tổng kết"] >= 5).sum())

cot1, cot2, cot3, cot4 = st.columns(4)
cot1.metric("Điểm trung bình lớp", f"{diem_tb:.2f}")
cot2.metric("Điểm cao nhất", f"{sv_cao_nhat['Tổng kết']:.2f}", sv_cao_nhat["Họ tên"])
cot3.metric("Điểm thấp nhất", f"{sv_thap_nhat['Tổng kết']:.2f}", sv_thap_nhat["Họ tên"])
cot4.metric("Số sinh viên đạt (≥ 5)", f"{so_sv_dat}/10")

# Chọn sinh viên và hiển thị chi tiết
st.subheader("Tra cứu thông tin sinh viên")
ten_chon = st.selectbox("Chọn một sinh viên:", df["Họ tên"].tolist())
sv = df[df["Họ tên"] == ten_chon].iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Chuyên cần", f"{sv['Chuyên cần']:.1f}")
c2.metric("Giữa kỳ", f"{sv['Giữa kỳ']:.1f}")
c3.metric("Cuối kỳ", f"{sv['Cuối kỳ']:.1f}")
c4.metric("Điểm tổng kết", f"{sv['Tổng kết']:.2f}")
c5.metric("Xếp loại", sv["Xếp loại"])

# Biểu đồ cột
st.subheader("Biểu đồ cột điểm tổng kết")
bieudo = df.set_index("Họ tên")[["Tổng kết"]]
st.bar_chart(bieudo, y="Tổng kết", use_container_width=True)

# Chân trang: sửa MSSV thành mã số sinh viên thực tế trước khi nộp
st.divider()
st.markdown(
    '<div style="text-align:center; color:gray; font-size:12px;">'
    'Người tạo: Lê Thị Lan Anh | MSSV: ĐIỀN_MSSV_CỦA_BẠN'
    '</div>',
    unsafe_allow_html=True
)
