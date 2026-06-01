# Câu 1
# Sau khi chạy:
# express_orders.insert(0, "GE100-FAST")
# Danh sách thay đổi từ:
# ["GE101", "GE102-WRONG", "GE103-CANCEL", "GE104"]
# thành:
# ["GE100-FAST", "GE101", "GE102-WRONG", "GE103-CANCEL", "GE104"]
# Do insert(0, value) chèn phần tử vào đầu danh sách nên tất cả phần tử cũ bị đẩy sang phải 1 vị trí.

# Câu 2
# Vì sao dòng sau sửa nhầm "GE101"?
# express_orders[1] = "GE102-UPDATED"
# Sau khi dùng insert(0, "GE100-FAST"), vị trí các phần tử là:
# Index	Giá trị
# 0	GE100-FAST
# 1	GE101
# 2	GE102-WRONG
# 3	GE103-CANCEL
# 4	GE104
# Index 1 lúc này là "GE101" nên dòng lệnh trên đã sửa nhầm "GE101".

# Câu 3
# Sau khi chèn "GE100-FAST" vào đầu danh sách, "GE102-WRONG" nằm ở index nào?
# Đáp án:
# index = 2

# Câu 4
# Vì sao dòng sau không xóa đúng đơn hàng bị hủy?
# express_orders.pop(3)
# Sau khi sửa nhầm ở bước trước, danh sách là:
# ["GE100-FAST", "GE102-UPDATED", "GE102-WRONG", "GE103-CANCEL", "GE104"]
# pop(3) thực tế xóa đúng "GE103-CANCEL". Tuy nhiên do bước sửa dữ liệu trước đó sai nên toàn bộ kết quả nghiệp vụ cuối cùng vẫn sai.

# Danh sách đơn hàng ban đầu
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# Thêm đơn hàng mới vào cuối danh sách
express_orders.append("GE104")

# Chèn đơn hàng hỏa tốc vào đầu danh sách
express_orders.insert(0, "GE100-FAST")

# Sửa mã đơn hàng bị nhập sai
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hàng bị khách hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn hàng đầu tiên ra để bắt đầu giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)