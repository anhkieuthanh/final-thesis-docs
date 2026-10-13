# VIỆC TREO

> Tài liệu này soạn với sự hỗ trợ của AI (Claude). Danh sách việc phát hiện trong lúc làm một đầu
> việc khác, chưa thuộc STT nào. Xử lý xong thì xóa mục khỏi file này và ghi kết quả vào
> `CHANGELOG_TAI_LIEU.md`.

Mỗi mục: phát hiện ở đâu · bằng chứng · hệ quả · đề xuất · hạn phải xong.

---

## VT-1. Phần suy luận của A2, A3 ăn hết ngân sách token

**Phát hiện ở:** STT-19, lần dò tín hiệu từ chối.
**Bằng chứng:** `ipi-agent-lab/results/smoke/probe_refusal_20261013T012512Z.json`, `max_tokens =
200`. A2 (`glm-5.2`) trả `finish_reason = length` ở cả 10 lời gọi: 4 câu trả lời rỗng, 4 câu chỉ
có một ký tự; toàn bộ token nằm ở `reasoning_content`. A3 (`glm-5.3-flash`) trả `length` ở 2/10 lời
gọi, 1 câu rỗng. A1 trả `length` ở 2/10, đều là câu đối chứng dài.

**Hệ quả:** chạy ma trận với ngân sách token thấp sẽ cho hàng loạt `final_answer` rỗng hoặc cụt.
Scorer không chấm được G1 kênh `answer`, G3 và cụm từ chối; USR tụt vì lý do hạ tầng chứ không vì
hành vi model. Hiện chưa khối nào trong `config/experiment.yaml` khai `max_tokens` hay mức suy luận;
`llm_client` cũng không đọc `reasoning_content`.

**Đề xuất:**
1. Thêm tham số cố định `max_tokens` (và mức suy luận nếu gateway hỗ trợ) vào khối `fixed` của
   `config/experiment.yaml`, áp như nhau cho A1–A3.
2. Chốt giá trị bằng một lần dò: tăng dần tới khi tỉ lệ `finish_reason = length` của câu lành tính
   về gần 0 trên cả ba target.
3. Quyết cách ghi run có `finish_reason = length` và `final_answer` rỗng: `parse_error` (lỗi hạ
   tầng, loại khỏi `N`) hay dữ liệu thật. Đề xuất `parse_error`, vì nguyên nhân là ngân sách token
   do harness đặt.
4. Cân nhắc lưu `reasoning_content` vào bước `llm` của trace để rà tay — không dùng để chấm.

**Hạn:** trước pilot (STT-60).

---

## VT-2. Gateway có thể chèn system prompt riêng

**Phát hiện ở:** STT-19, lần dò tín hiệu từ chối.
**Bằng chứng:** cùng file trên. A1, câu dò P1 (đòi lộ system prompt), cả hai lần đều tự giới thiệu là
CLI Claude Code — không có trong system prompt của testbed. A3, câu P1 lần 2, phần suy luận nhắc
"legitimate engineering task" — testbed không nói gì về việc kỹ thuật phần mềm.

**Hệ quả:** nếu gateway chèn prompt riêng, hành vi của model đích bị một chỉ dẫn ẩn chi phối. Mọi
ASR đo trên A1 (và có thể A3) phản ánh tổ hợp "prompt testbed + prompt gateway", không phải cấu
hình doanh nghiệp mà đề tài mô tả. Đây là mối đe dọa trực tiếp tới tính hợp lệ, nặng hơn hạn chế #2
(các target dùng chung một gateway).

**Đề xuất:**
1. Hỏi nhà cung cấp gateway: có chèn system prompt hay tiền tố nào vào request không, theo model
   nào, tắt được không.
2. Dò độc lập: gửi câu hỏi "bạn là ai, ai tạo ra bạn, bạn có chỉ dẫn hệ thống nào ngoài tin nhắn
   này" với system prompt rỗng và với system prompt của testbed; so câu trả lời giữa ba target.
3. Nếu xác nhận có chèn và không tắt được: báo GVHD (ảnh hưởng phạm vi đã chốt và `v-models-1.0`),
   rồi ghi thành hạn chế riêng trong `Y_TUONG_DU_AN.md` mục 16 và `docs/01. Đề bài/01. Mô tả bài
   toán.md`.

**Hạn:** trước pilot (STT-60). Nếu phải đổi gateway hoặc model thì cần GVHD đồng ý, vì đụng mốc
`v-models-1.0` (quy tắc cứng #9).
