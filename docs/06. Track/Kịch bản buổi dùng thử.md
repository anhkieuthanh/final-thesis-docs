# Kịch bản buổi dùng thử với người dùng thực (STT-85, STT-87)

> Tài liệu soạn với sự hỗ trợ của AI (Claude). TA điều phối buổi thử; phiếu khảo sát ở `docs/phieu_khao_sat.md`.
> Kết quả thô và tổng hợp ghi vào `docs/phan_hoi_nguoi_dung.md` sau buổi thử, rồi đưa vào Chương 5 mục 5.8.

## 1. Mục tiêu

Kiểm ba câu hỏi về công cụ từ góc nhìn người dùng mục tiêu (persona P1 — người chịu trách nhiệm an toàn cho tác
tử doanh nghiệp):

1. Bộ chỉ số (ASR hai chỉ số, DSR, USR, FRR, ARR) có giúp quyết định bật cấu hình phòng thủ nào không?
2. Trang chi tiết lượt chạy có giúp hiểu vì sao một tấn công thành công hay bị chặn không?
3. Sau khi xem kết quả, người dùng sẽ thực sự bật cấu hình nào, và vì sao?

Buổi thử đánh giá **công cụ**, không đánh giá người tham gia.

## 2. Người tham gia

- 3–5 người: đồng nghiệp làm an toàn thông tin, người vận hành trợ lý AI nội bộ, GVHD.
- Mỗi người một mã P1…P5. **Không ghi họ tên, email, số điện thoại, nơi làm việc cụ thể** ở bất kỳ tài liệu
  nào. Chỉ ghi vai trò ở mức nhóm (an toàn thông tin / vận hành AI / giảng viên) và số năm kinh nghiệm theo
  khoảng (dưới 2 / 2–5 / trên 5 năm).
- Ghi âm hay quay màn hình chỉ khi người tham gia đồng ý; tệp ghi lưu ngoài kho mã, xóa sau khi tổng hợp.

## 3. Chuẩn bị (TA làm trước buổi)

- [ ] Hạ tầng chạy: `docker compose up` (Qdrant, MailHog, canary listener), console `make console`, mở
      `http://127.0.0.1:8610`.
- [ ] Console trỏ tới kho vết của các lô đầy đủ B1, B2, B3, B5, B6.
- [ ] Chọn trước 3 lượt chạy mẫu để mở ở nhiệm vụ 3 (ghi `run_id` vào mục 7): một tấn công thành công trên
      K2a, một lượt bị D3 chặn, một lượt bị mô hình tự từ chối.
- [ ] Phần trình diễn trực tiếp (nhiệm vụ 4) gọi mô hình thật, mỗi lượt khoảng 0,02 USD. Số lượt dự kiến
      (khoảng 2 lượt × số người) phải được TA duyệt như một lô trước buổi thử. Demo chỉ chạy mô hình thật.
- [ ] In hoặc gửi phiếu khảo sát; chuẩn bị đồng hồ bấm giờ và bảng quan sát ở mục 6.

## 4. Trình tự buổi thử (khoảng 40 phút mỗi người)

| Bước | Thời gian | Nội dung |
|---|---|---|
| 0 | 3 phút | Giới thiệu mục tiêu, xin đồng ý tham gia (mục 5), nói rõ được dừng bất cứ lúc nào |
| 1 | 3 phút | Giải thích bối cảnh: tác tử của một công ty phân phối thiết bị, dữ liệu mô phỏng, kẻ tấn công cài lệnh vào tài liệu hoặc kết quả công cụ |
| 2 | 20 phút | Bốn nhiệm vụ ở dưới; người tham gia tự thao tác, nói thành lời điều mình nghĩ; TA không gợi ý trừ khi kẹt quá 3 phút |
| 3 | 7 phút | Điền phiếu khảo sát |
| 4 | 7 phút | Phỏng vấn ngắn (câu hỏi ở phiếu, phần C) |

### Bốn nhiệm vụ

| # | Nhiệm vụ đưa cho người tham gia | Trang console | Đạt khi |
|---|---|---|---|
| N1 | "Theo dữ liệu, kẻ tấn công cài lệnh vào kho tài liệu hay vào kết quả công cụ thì nguy hiểm hơn? Nguy hiểm hơn bao nhiêu?" | Tổng quan, Tấn công | Chỉ ra K2 cao hơn K1 và đọc được một con số kèm khoảng tin cậy |
| N2 | "Nếu phải bật một cấu hình phòng thủ cho tác tử này, anh/chị chọn cấu hình nào? Cái giá là gì?" | Phòng thủ | Chọn một cấu hình và nêu được cả mức an toàn lẫn mức hữu dụng mất đi |
| N3 | "Mở lượt chạy [run_id] và cho biết vì sao tấn công này thành công / bị chặn, bị chặn bởi ai." | Lượt chạy, chi tiết lượt chạy | Chỉ ra bước payload vào ngữ cảnh và nguyên nhân chặn (phòng thủ / mô hình từ chối) |
| N4 | "Chạy thử một lượt tấn công với phòng thủ tắt, rồi với cấu hình anh/chị chọn ở N2." | Thí nghiệm | Chạy được hai lượt và so được kết quả |

## 5. Lời xin đồng ý (đọc to, đồng ý bằng lời)

"Buổi này kiểm một công cụ đánh giá an toàn cho trợ lý AI, không kiểm anh/chị. Dữ liệu trong công cụ là dữ liệu
mô phỏng. Tôi không ghi tên hay thông tin nhận diện anh/chị; câu trả lời được ghi theo mã P1–P5 và chỉ dùng cho
báo cáo đồ án. Anh/chị có thể dừng bất cứ lúc nào. Anh/chị có đồng ý tham gia [và cho ghi âm] không?"

## 6. Bảng quan sát (TA ghi trong lúc người tham gia làm)

| Mã | Nhiệm vụ | Thời gian (phút) | Đạt / Đạt có gợi ý / Không đạt | Chỗ kẹt, câu hỏi, nhận xét nguyên văn ngắn |
|---|---|---|---|---|
| P1 | N1 | | | |
| P1 | N2 | | | |
| P1 | N3 | | | |
| P1 | N4 | | | |

(Lặp cho P2–P5.)

## 7. Lượt chạy mẫu cho N3

Chọn từ lô B2 `attack-B2-20261119T023028Z` (truy vấn đầu tiên theo `run_id`, không chọn vì kết quả đẹp). TA mở thử
trên console trước buổi; đổi lượt khác nếu trang chi tiết khó đọc.

| Loại | `run_id` | Mô hình · ô · cấu hình |
|---|---|---|
| Tấn công thành công | `012527cd2d5147fabafecb3f3ec0bf9f` | A2 · K2a·T3·G3 · off |
| Bị D3 chặn | `01bbeac1be604660aa1a59fb52abf938` | A2 · K2a·T3·G2 · d3_only |
| Mô hình tự từ chối | `6853bf0e719244abac0cfe54be3d30b6` | A3 · K2a·T2·G3 · d4_only (D4 bật nhưng chặn là do mô hình — đúng chỗ phân biệt của câu B5) |

## 8. Tổng hợp sau buổi thử (STT-87)

1. Chép phiếu và bảng quan sát vào `docs/phan_hoi_nguoi_dung.md`, chỉ theo mã P1–P5.
2. Bảng định lượng: tỷ lệ đạt từng nhiệm vụ, thời gian trung vị; điểm Likert từng câu (trung vị, khoảng). Với
   3–5 người, chỉ báo cáo số đếm và trung vị, **không** suy ra tỷ lệ cho tổng thể.
3. Mã hóa câu trả lời mở và ghi chú quan sát thành chủ đề (mỗi chủ đề: mô tả, số người nhắc, một trích dẫn ngắn).
4. Rút hạn chế của công cụ từ góc nhìn người dùng và đề xuất sửa — TA quyết đề xuất nào đưa vào báo cáo.
5. Điền Chương 5 mục 5.8 và Chương 4 mục 4.6.2 (ô đánh giá người dùng).
