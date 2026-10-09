# CHANGELOG TÀI LIỆU

Mục mới nhất ở trên cùng. Mỗi mục: ngày · file · thay đổi · lý do.

## 2026-10-09
- `CLAUDE.md` (quy tắc cứng #1), `Y_TUONG_DU_AN.md` (bảng biến, quy tắc #1, lịch ND3, mục 19 bước 9),
  `docs/01. Đề bài/01. Mô tả bài toán.md` (mục 3.4, 3.5, bảng biến), `docs/01. Đề bài/Aux/Danh mục viết tắt.md` (M1),
  `ipi-agent-lab/README.md` — bỏ cơ chế khóa bộ đo bằng tag `v-bench-1.0`; bộ đo vẫn khóa theo quy tắc cứng #1, mọi thay
  đổi ghi ở file này. Lý do: tag chưa từng được tạo; TA quyết bỏ cơ chế tag.
- `ipi-agent-lab/data/carrier_tasks.json` — đổi mã task cũ sang mã hiện hành (`task_id` W1-06 → STT-18; W1-07 → STT-20;
  W2-04 → STT-22; W2-08 → STT-18; W1-04 → Threat Model, trỏ `docs/04. Design/02. Threat Model.md`); bỏ khối `changelog` và
  trường `updated` trong file. Không đổi tác vụ, ràng buộc, allowlist hay tiêu chí chấm nào. Lý do: update bài toán — đồng bộ
  bộ đo với kế hoạch hiện hành; quy tắc cứng #10 (dữ liệu chỉ chứa dữ liệu).
- `ipi-agent-lab/data/benign_queries.json` — `task_id` W2-07 → STT-18; W1-06 → STT-18, W2-04 → STT-22, bỏ W2-03 trong
  `note_vi`; bỏ trường `updated`. Không đổi câu hỏi hay đáp án nào. Lý do: update bài toán — như trên.

## 2026-10-08
- `docs/03. Khảo sát/KHAO_SAT_PHONG_THU.md` — tạo mới: bảng đối chiếu bốn nhóm phòng thủ (cơ chế · vị trí cắm · điểm mù · chi phí),
  nhận xét cho thiết kế, ánh xạ sang D1–D4. Lý do: đầu ra STT-12, đầu vào cho STT-20 và mục 2.4 báo cáo.
- `docs/03. Khảo sát/KHAO_SAT_PHONG_THU.xlsx` — tạo mới: bản Excel của bảng đối chiếu, thêm cột cách hoạt động, ví dụ testbed,
  phụ thuộc mức tuân thủ của model. Lý do: TA cần bản bảng tính để tra và trình bày.

## 2026-10-05 (sau khi GVHD ký phụ lục)
- `PhieuGiaoNhiemVu_DATN_20250127E_KIEU_THANH_ANH.xlsx` (sheet "Kỹ sư", ô A62) — "bốn kỹ thuật tự đề xuất … và thao túng bằng
  thẩm quyền hành chính" thành "ba kỹ thuật tự đề xuất: chia mảnh, kích hoạt trễ, che giấu đặc thù tiếng Việt". `Y_TUONG_DU_AN.md`
  (mục 15) sửa câu dẫn phiếu tương ứng. Lý do: khớp phụ lục đã ký (T6–T8) và việc gộp T9 vào T1.
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` — đánh dấu 16 hạng mục mục 9 đã đồng ý; chọn tên đề tài dài (RAG + MCP);
  trần ngân sách 100 USD; model sinh payload thích ứng chưa chốt; mục 8 đổi thành "Việc còn treo" và bỏ việc đưa bằng chứng
  benchmark vào repo. Lý do: GVHD đã ký; phần bằng chứng khảo sát đang xây lại từ đầu.
- `Y_TUONG_DU_AN.md` (mục 12.3) — bỏ bảng số USR 37/60 và các số đi kèm. Lý do: CSV gốc đã mất, số không truy nguồn được;
  số mới lấy từ lượt chạy lại STT 37.
- `docs/04. Design/02. Thread Model.md` đổi tên thành `02. Threat Model.md`; `01. Agent RAG + MCP .md` thành
  `01. Agent RAG + MCP.md` (bỏ dấu cách thừa); sửa tham chiếu trong `taxonomy.md` và `01. Mô tả bài toán.md`. Lý do: sai chính tả tên file.
- Xoá thư mục `benchmarks/` (5 thư mục chỉ còn `.git` hỏng). Clone `ipi-agent-lab/` vào workspace từ remote. Lý do: dọn workspace.

## 2026-10-05 (gộp T9 vào T1)
- `Y_TUONG_DU_AN.md` (mục 6, 13.3, 14, 15), `docs/01. Đề bài/01. Mô tả bài toán.md` (mục 7), `docs/04. Design/taxonomy.md`,
  `docs/04. Design/02. Thread Model.md` (+ bản `.docx`), `docs/03. Khảo sát/FIT_GAP.md`, `docs/01. Đề bài/02. AI SEC MAP.md`,
  `docs/01. Đề bài/Aux/`, `docs/07. Báo cáo/Chuong1.tex`, `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md`, `CLAUDE.md`,
  `Kế hoạch thực hiện.xlsx` — gộp T9 (thẩm quyền hành chính) vào T1: còn 8 kỹ thuật T1–T8, trong đó 3 kỹ thuật tự đề xuất
  T6–T8; giọng công văn, chỉ đạo Ban Tổng Giám đốc thành biến thể giọng văn của T1; đổi tên T1 thành "Câu lệnh tường minh,
  giả mạo uy quyền" và T2 thành "Ghi đè chỉ thị hệ thống từ trong tài liệu"; T_chung còn {T1, T2, T3, T5, T7, T8}; khối B1 từ
  (9+7+8) còn (8+6+7) kỹ thuật theo kênh, 4.320 còn 3.780 run, tổng ước tính từ khoảng 14.700 còn 14.150; ma trận đủ chiều
  từ khoảng 1.700 còn 1.500 ô; STT 49 trong kế hoạch đổi thành biến thể T1, giữ 4 giờ. Lý do: T1, T2 và T9 là kiểu câu chữ
  nằm trong payload, không phải kênh tấn công; T9 và T1 cùng trục "nguồn phát" nên tách riêng làm ma trận phân biệt không
  sạch. Chưa sửa: phiếu giao nhiệm vụ (còn ghi "bốn kỹ thuật tự đề xuất"), cần báo GVHD.

## 2026-10-05
- `docs/04. Design/01. Agent RAG + MCP .md` (mục 1.1), `docs/04. Design/00. Image/luong_du_lieu_01_kien_truc_tong_the.svg`
  — đổi sơ đồ kiến trúc tổng thể từ chiều ngang sang chiều dọc (`flowchart TB`): kẻ tấn công đưa
  vào khối ngoài vành đai, tô đỏ ba đường K1/K2a/K2b, ngắt dòng nhãn mô hình đích; render lại SVG
  và thêm bản PNG 2352×3276 px (đặt DPI để rộng 16 cm). Lý do: bản ngang quá rộng, chèn vào
  trang Word dọc thì chữ quá nhỏ.

## 2026-09-30
- `Kế hoạch thực hiện.xlsx` (thêm STT 97, ND3 Tuần 8, 3 giờ), `Y_TUONG_DU_AN.md` (mục 15), `docs/01. Đề bài/01. Mô tả bài toán.md` —
  tách việc soạn đặc tả chỉ số đo thành task riêng, đầu ra `docs/04. Design/03. Chỉ số đo.md`; khối lượng 389 giờ thành
  392 giờ, vượt sức chứa 52 giờ, vẫn nằm trong mức bù của nhịp 24 giờ/tuần; sửa câu "STT 71 đã rút gọn" trong mục 15
  (STT 71 đã khôi phục). Lý do: Mô tả bài toán trỏ tới file công thức chỉ số nhưng chưa task nào tạo ra file đó.
- `Kế hoạch thực hiện.xlsx`, `Y_TUONG_DU_AN.md` (mục 13.1, 13.2, 15, 15.1), `README.md`, `docs/01. Đề bài/02. AI SEC MAP.md`,
  `docs/04. Design/02. Thread Model.md`, `docs/01. Đề bài/Aux/`, `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` —
  đồng bộ lần cuối: STT 71 giữ ma trận 6 cấu hình (cắt sẽ mâu thuẫn RQ3–RQ5 và M5); khối lượng 389 giờ so với
  sức chứa 280 giờ từ Tuần 4, thiếu khoảng 49 giờ, bù bằng 24 giờ mỗi tuần; thứ tự cắt dự phòng ghi ở mục 15;
  đánh số chương theo báo cáo 6 chương (mục 4.4 là kết quả thực nghiệm); cây thư mục và docker-compose (5 service,
  có dashboard) theo hiện trạng; thêm M1b, M3b vào danh mục viết tắt; đường dẫn cũ `docs/0n_...` và
  `MO_TA_BAI_TOAN.md`, `docs/05_bo_do/` đổi về tên và vị trí hiện hành; STT 50 bỏ câu "cắt đầu tiên" để khớp thứ tự cắt ở mục 15. Lý do: loại các chỗ lệch giữa phiếu, kế hoạch và tài liệu.
- `CLAUDE.md` (mục 1, 2, 5, 6, 7), `Y_TUONG_DU_AN.md` (mục 10.2, 13.1, 13.2, 15, 15.1) và `README.md`
  (bảng "Đọc theo thứ tự", cây thư mục) — đồng bộ với phiếu giao nhiệm vụ: 16 tuần thành 17 tuần
  (07/09/2026 → 08/01/2027); lộ trình 12 giai đoạn thành sáu Nội dung ND1–ND6 kèm mốc theo `Kế hoạch
  thực hiện.xlsx`; thêm phiếu làm nguồn cao nhất; kế hoạch và trạng thái task trỏ về file xlsx thay cho
  `docs/02_ke_hoach/` (thư mục không còn); mã commit đổi từ `W2-09` sang `STT-n`; thêm ký hiệu `ND1`–`ND6`
  và quy ước viết "Tuần n" để không trùng `T1`–`T9`; thêm đánh giá 3–5 người dùng thực vào phạm vi và
  sản phẩm bàn giao, thêm thư mục `dashboard/`. Lý do: phiếu đã ký là nguồn cao nhất, ba tài liệu đang
  lệch nhau về số tuần, khung nội dung và đường dẫn kế hoạch; Y_TUONG_DU_AN.md thiếu hẳn phần đánh giá
  người dùng mà phiếu coi là bắt buộc.
- `Kế hoạch thực hiện.xlsx` — cột Tuần đổi `T1`–`T17` thành "Tuần n"; dòng M6/M7 của sheet
  "Tổng quan mốc" đổi thành M6; STT 78–81 sửa theo hai harness; STT 8 đặt Xong; sửa đường dẫn cũ ở STT
  3 và 5, bỏ tham chiếu `v3` và `W11-01`; thêm cột "Giờ ước tính" và sheet "Khối lượng giờ". Lý do:
  hết lệch với phiếu, tránh trùng ký hiệu `T1`–`T9`, và tính lại khối lượng giờ cho 17 tuần.
- `Y_TUONG_DU_AN.md` (mục 9, 10.2, RQ6, mục 15, mục 16), `docs/01. Đề bài/01. Mô tả bài toán.md`
  (mục 8.3, phạm vi, RQ6, hạn chế) — nâng harness từ 1 lên 2 (HN-CC, HN-OW; mỗi harness trên A1, A2,
  A3; HN-CC trên A2, A3 có điều kiện) và tách RQ6 thành 6a, 6b, 6c. Lý do: TA chốt 2 harness, đồng bộ
  theo `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md`.
- `Y_TUONG_DU_AN.md` (mục 15) — thay khối lượng 293 giờ bằng ước tính 419 giờ theo 96 đầu việc, so với
  sức chứa 340 giờ. Lý do: con số cũ tính cho kế hoạch 16 tuần.
- `Kế hoạch thực hiện.xlsx` — cắt STT 10, 11 (PoC MCP và RAG), 23 (wireframe dashboard), 69 (đối chiếu
  bậc độ lớn), 89 (gộp vào 88); rút gọn STT 5 (còn hoàn thiện fit-gap), 58 (Pareto ảnh tĩnh), 88 (ráp chương 1–4). Giữ nguyên STT 50 (kỹ thuật T7) và STT 71 vì phiếu giao nhiệm
  vụ ghi bốn kỹ thuật tự đề xuất. Khối lượng ước tính từ 419 giờ còn 389 giờ; STT 71 giữ ma trận 6 cấu hình (xem mục đồng bộ cuối ngày).
  `Y_TUONG_DU_AN.md` (mục 15) ghi số mới. Lý do: kế hoạch vượt sức chứa 79 giờ, GVHD đã duyệt các mục cắt.
- `docs/07. Báo cáo/Chuong1.tex` (đầu file, mục 1.2, 1.4, Bảng 1.1) — bỏ hai điểm xác nhận đã xử lý
  (phạm vi và RQ6 đã chốt, bằng chứng bộ đo đã có ở `docs/03. Khảo sát/`); RQ6 và phạm vi nói hai harness;
  thêm đánh giá với ba đến năm người dùng thực vào phạm vi và Chương 5. Lý do: đồng bộ với phiếu giao
  nhiệm vụ (Nội dung 6) và với quyết định hai harness.
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` (mục 1, 3, 9), `docs/04. Design/taxonomy.md`,
  `docs/04. Design/02. Thread Model.md`, `docs/01. Đề bài/01. Mô tả bài toán.md` — "16 tuần" đổi thành
  "17 tuần", hạn nộp 08/01/2027. Lý do: theo phiếu giao nhiệm vụ.

## 2026-09-24
- `docs/07. Báo cáo/Chuong1.tex` (mục 1.1, đoạn cuối) — viết lại câu hỏi vận hành (iii) thành hai
  vế: dạng tấn công vẫn thành công khi bật đồng thời mọi cơ chế, và cơ chế nào giữ hiệu lực khi kẻ
  tấn công biết trước cách nó hoạt động. Lý do: câu cũ gộp lỗ hổng cấu trúc với lỗ hổng do leo
  thang, và ngầm giả định biết trước cơ chế là chắc chắn vượt qua được.

## 2026-09-23
- `docs/03. Khảo sát/` (mới: `TOM_TAT_CONG_TRINH.md`, `FIT_GAP.md`, `evidence/`) — khảo sát sáu
  công trình (AgentDojo, AutoDojo, MCPTox, InjecAgent, AgentDyn, MCP-Poison-Bench) theo bảng 12 tiêu
  chí cố định; cài và chạy offline cả sáu benchmark (không gọi LLM), lưu log, manifest pin commit và
  script sinh bằng chứng vào `evidence/`; fit-gap trỏ từng nhận xét về file bằng chứng. Lý do: dựng
  lại đầu ra của task khảo sát/fit-gap (ND1, dòng 5 kế hoạch) sau khi bằng chứng cũ mất trong đợt
  dựng lại workspace, và thỏa quy tắc cứng #2.
- `docs/07. Báo cáo/Chuong1.tex` — viết lại theo hướng dẫn chương 1 của mẫu SOICT: bọc
  `subfiles`, bỏ `\chapter` (đã có ở `DoAn.tex`), giữ nhãn `section:1.1`–`section:1.4` của mẫu;
  chuyển đoạn đánh giá các bộ đo từ 1.1 sang đầu 1.2; 1.1 thêm lợi ích và khả năng áp dụng, bỏ
  câu nêu giải pháp; 1.2 theo trình tự tổng quan công trình → hạn chế → năm chức năng chính →
  sáu RQ (Bảng 1.1) → phạm vi rút gọn; 1.3 theo trình tự phương pháp và công nghệ → mô tả ngắn
  giải pháp → bốn đóng góp, bỏ phần giải thích chi tiết ba vấn đề phương pháp; bố cục ghi số
  chương trực tiếp thay cho `\ref`. Độ dài khoảng 3–4 trang. Lý do: đối chiếu với yêu cầu của mẫu
  (3–6 trang, không nêu giải pháp ở 1.1, 1.2 phải có tổng quan và so sánh, 1.3 không giải thích
  chi tiết công nghệ).
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` (mục 3, 4, 5, 6, 9) — nâng thiết kế harness
  lên 2 harness × 3 model: HN-CC chạy thêm trên A2, A3 qua `ANTHROPIC_BASE_URL`, là nhánh có điều
  kiện (bỏ nếu chạy thử không đạt, không cần ký lại); RQ6b so hai harness trong cùng từng model;
  khối B6 từ 350 lên 450 run, tổng ước tính từ khoảng 14.600 lên 14.700; thêm ràng buộc về model
  id trên endpoint tương thích Anthropic và về tính năng mất khi dịch API. Lý do: Claude Code
  cắm được endpoint tương thích Anthropic của nhà cung cấp; thiết kế đủ ô cho phép kiểm chênh
  lệch giữa hai harness có giữ chiều khi đổi model.

## 2026-09-23
- `docs/07. Báo cáo/Chuong1.tex` — bỏ toàn bộ tiểu mục, giữ bốn mục theo khung mẫu: Đặt vấn đề ·
  Mục tiêu và phạm vi đề tài · Định hướng giải pháp · Bố cục đồ án. Nội dung giữ nguyên, thêm câu
  dẫn vào đoạn đóng góp. Lý do: TA yêu cầu viết đúng bốn mục của mẫu, không chia tiểu mục.
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` (mục 3, 4, 5, 6, 8, 9) — mở harness từ 1
  lên 2: HN-CC Claude Code trên A1 và HN-OW OpenWork (lõi opencode) trên A1, A2, A3; RQ6 tách 6a
  (harness so với vòng lặp trần trên cùng model), 6b (hai harness trên A1), 6c (ánh xạ D1–D4);
  khối B6 tăng từ 100 lên 350 run, tổng ước tính từ khoảng 14.300 lên 14.600; thêm ràng buộc pin
  model id có ngày. Lý do: GVHD duyệt mở rộng; một harness chỉ trên A1 không trả lời được bối
  cảnh doanh nghiệp Việt dùng GLM, DeepSeek; chạy HN-OW trên A1 để tách phần chênh do harness khỏi
  phần do model. Ký hiệu harness dùng tiền tố `HN-` để không trùng tiền tố `H` của giả thuyết H1–H6;
  đăng ký vào danh mục viết tắt khi phạm vi được ký.

## 2026-09-23
- `docs/07. Báo cáo/Chuong1.tex`, `docs/07. Báo cáo/refs_chuong1.bib` — tạo mới. Chương 1
  "Giới thiệu đề tài" theo khung mẫu SOICT: đặt vấn đề (bối cảnh, tính cấp thiết), mục tiêu và
  phạm vi, sáu câu hỏi nghiên cứu kèm bảng giả thuyết H1–H6, định hướng giải pháp và bốn nhóm
  đóng góp, bố cục sáu chương; 12 mục tài liệu tham khảo có nhãn trạng thái kiểm. Ba điểm chờ
  xác nhận đánh dấu `% [XÁC NHẬN]` trong file. Lý do: bắt đầu viết báo cáo; nội dung lấy từ
  `Y_TUONG_DU_AN.md`, `01. Mô tả bài toán.md` và phiếu giao nhiệm vụ.

## 2026-09-23
- `docs/06. Track/Chốt phạm vi và checklist ký GVHD.md` — tạo mới. Biểu mẫu chờ ký gồm: định danh
  đề tài (hai phương án tên để chọn một), persona P1/P2 và phản persona, bảng phạm vi chốt cứng
  có tên ba mô hình đích và harness, sáu RQ kèm tiêu chí trả lời ghi trước, thiết kế phân khối
  B1–B6 với ước tính khoảng 14.300 run ở giả định N = 30, cấu hình harness Claude Code trên A1,
  việc phải xong trước khi ký, checklist 16 hạng mục. Lý do: phụ lục điều chỉnh phạm vi chưa có
  chữ ký; vòng chất vấn phạm vi chỉ ra RQ1 so kênh trên hai tập kỹ thuật khác nhau, RQ2–RQ3 chưa
  có tiêu chí trả lời, RQ4 chưa định nghĩa độ trễ và chi phí, RQ5 chưa cố định mục tiêu, RQ6 lẫn
  model với harness. Chưa đồng bộ vào `Y_TUONG_DU_AN.md` và `01. Mô tả bài toán.md` cho tới khi
  có chữ ký.

## 2026-09-22
- `docs/04. Design/taxonomy.md` — tạo mới. Đặc tả mức thi hành của taxonomy kênh: ba câu hỏi
  phân định một kênh (thực thể ghi · vào context bảo đảm hay có điều kiện · vùng prompt), đặc tả
  từng kênh K1–K5 kèm điểm bơm và cơ chế kích hoạt, ba tiêu chí vào phạm vi thực nghiệm và lý do
  loại K3/K4/K5, bảng ánh xạ kênh × kỹ thuật T1–T9 (ghi rõ T4 không dựng được trên K2a và T6 chỉ
  dựng được trên K1 là ràng buộc kiến trúc, không phải ASR bằng 0), bảng ánh xạ kênh × phòng thủ
  D1–D4. Lý do: mục 6 của `01. Mô tả bài toán.md` đã trỏ tới file này nhưng file chưa tồn tại;
  đặc tả kênh không có chỗ nào ghi đủ để thi hành.
- `docs/01. Đề bài/01. Mô tả bài toán.md` (mục 6 và bảng 12.1) — bổ sung ba câu hỏi phân định
  kênh vào phần mở mục 6; thêm đoạn chốt phạm vi hai kênh thực nghiệm K1 và K2 kèm lý do loại
  K3, K4, K5; nêu rõ K2a và K2b là hai phân kênh của cùng K2, gộp khi trả lời RQ1 và tách khi
  trả lời RQ2, trace vẫn ghi `channel ∈ {K1, K2a, K2b}`. Dòng "Kênh tấn công" trong bảng phạm vi
  chốt cứng đổi từ "3 · K1 · K2a · K2b" thành "2 · K1 · K2 (hai phân kênh K2a, K2b)". Lý do:
  bảng phạm vi đếm ba kênh trong khi RQ1 và H1 phát biểu theo hai kênh — cùng một đại lượng có
  hai con số ở hai chỗ.
- `Y_TUONG_DU_AN.md` (mục 5 và bảng phạm vi) — đồng bộ đúng hai thay đổi trên. Lý do: giữ nguyên
  tắc một khái niệm một ký hiệu giữa ba tài liệu.

## 2026-09-22
- `docs/04. Design/02. Threat Model.docx` — tạo mới. Bản trình bày mô hình đe dọa theo năm bước
  chuẩn threat modeling (xác định tài sản · sơ đồ luồng dữ liệu và ranh giới tin cậy · liệt kê
  mối đe dọa theo STRIDE · đánh giá và ưu tiên rủi ro · biện pháp giảm thiểu và rủi ro dư), kèm
  mức 2 về năng lực kẻ tấn công, phần cưỡng chế bằng trace, hạn chế và việc còn treo. Ba hình
  render từ SVG trong `00. Image/` đặt ở trang ngang; bảng xếp hạng rủi ro tám kịch bản đặt ở
  trang ngang. Nội dung sinh từ `02. Thread Model.md`, không thêm dữ kiện mới ngoài hai mục đã
  bổ sung vào file .md cùng ngày. Lý do: cần bản tài liệu đúng cấu trúc threat modeling chuẩn để
  trình GVHD và đưa vào báo cáo.
- `docs/04. Design/02. Thread Model.md` (mục 1.4, 1.5, 5) — bổ sung ba mục thiếu so với năm bước
  chuẩn: ánh xạ sang STRIDE kèm phân biệt "loại vi phạm" và "kỹ thuật né phòng thủ" cho T1–T9;
  bảng xếp hạng rủi ro tám kịch bản TH-01 đến TH-08 theo khả năng × ảnh hưởng, ghi rõ là ước
  lượng ghi trước thực nghiệm; mục biện pháp giảm thiểu và rủi ro dư từng kịch bản. Đánh lại số
  mục 5 và 6 thành 6 và 7. Lý do: giữ nguyên tắc một nguồn chân lý — nội dung mới phải nằm ở
  file .md trước, bản docx chỉ trình bày lại.

## 2026-09-22
- `docs/04. Design/02. Thread Model.md` (mục 2.2, 3, 5, 6) — chốt mức phản hồi cho A-adaptive là
  **PH1**; thay đoạn đề xuất bằng đoạn chốt kèm hệ quả cưỡng chế: harness thích ứng không đọc
  trace, không đọc `blocked_by`, không đọc log D1–D4; tập tín hiệu vào của vòng sau đúng bằng
  `final_answer` cộng các bồn chứa kẻ tấn công sở hữu. Mục "việc còn treo" bỏ việc chốt PH, thêm
  việc dựng ranh giới mã nguồn giữa `src/attack/` và `src/obs/` để chặn rò rỉ oracle. Lý do: PH1
  đã được chốt; rò rỉ oracle là loại lỗi không hiện ra trong kết quả nên phải chặn bằng cấu trúc
  mã nguồn, không bằng thỏa thuận.
- `docs/01. Đề bài/01. Mô tả bài toán.md` (mục 4.3) — cập nhật câu về mức phản hồi từ "chưa chốt"
  thành "đã chốt PH1". Lý do: đồng bộ với quyết định trên.
- `CLAUDE.md`, `README.md`, `docs/01. Đề bài/01. Mô tả bài toán.md`,
  `docs/01. Đề bài/02. AI SEC MAP.md`, `docs/01. Đề bài/Aux/Danh mục viết tắt.md`,
  `docs/04. Design/01. Agent RAG + MCP .md`, `docs/04. Design/02. Thread Model.md` — sửa toàn bộ
  tham chiếu đường dẫn theo tên thư mục và tên file hiện hành (`docs/01. Đề bài/`,
  `docs/04. Design/`, `docs/06. Track/`, SVG chuyển vào `00. Image/`). Lý do: sau đợt đổi tên
  thư mục, mọi tham chiếu nội bộ đứt — đây là lớp lỗi đã xảy ra một lần và có quy ước riêng
  trong `CLAUDE.md`. Các đường dẫn trong chính file changelog giữ nguyên vì là bản ghi lịch sử.

## 2026-09-22
- `docs/04_thiet_ke/luong_du_lieu.md` — tạo mới. Mô tả cơ chế vận hành của AI Agent RAG + MCP
  tool-calling (hai vòng lặp, một cửa sổ ngữ cảnh) và bốn sơ đồ Mermaid: kiến trúc tổng thể,
  trình tự một lượt suy luận, con đường nội dung không tin cậy theo năm giai đoạn Gieo → Nạp →
  Kích hoạt → Nhầm lẫn ranh giới → Thi hành, và điểm chèn của D1–D4 kèm nhánh `blocked_by`.
  Mục 6 liệt kê sáu điểm ĐC-1…ĐC-6 phải đối chiếu với đặc tả MCP gốc trước khi trích vào báo
  cáo. Lý do: sản phẩm của phần tìm hiểu cơ chế agent; làm nền hình cho chương kiến trúc và
  cho luận cứ H1 (ASR kênh công cụ cao hơn kênh tài liệu).
- `docs/04_thiet_ke/luong_du_lieu_01_kien_truc_tong_the.svg`,
  `docs/04_thiet_ke/luong_du_lieu_02_trinh_tu_mot_luot.svg`,
  `docs/04_thiet_ke/luong_du_lieu_03_duong_di_noi_dung_khong_tin_cay.svg`,
  `docs/04_thiet_ke/luong_du_lieu_04_diem_chen_phong_thu.svg` — tạo mới. Bản render của bốn
  khối Mermaid trong file trên. Lý do: báo cáo LaTeX chèn hình vector, không chèn mã Mermaid.
- Ký hiệu mới `ĐC-1`–`ĐC-6` dành riêng cho hạng mục cần đối chiếu đặc tả MCP gốc, không trùng
  với các tiền tố đang dùng (TS, A, M, G, K, T, D, CT, U, TL, RQ, AS).

## 2026-09-22
- `docs/04_thiet_ke/MO_HINH_DE_DOA.md` — tạo mới. Đặc tả mức thi hành của mô hình đe dọa hai
  mức: vành đai tin cậy; ma trận tài sản × mục tiêu (TS1–TS3 × G1–G3) kèm thuộc tính an ninh bị
  vi phạm; bảng hệ quả khi sáu giả định vận hành không thỏa; bảy trục năng lực kẻ tấn công với
  hai mức A-blind / A-adaptive; giao thức vòng thích ứng (phạm vi được sửa, ba điều kiện dừng,
  đơn vị tính ASR là chuỗi); hai trường trace bổ sung `adaptive_chain_id`, `adaptive_round` và
  năm bất biến kiểm được bằng test. Lý do: phần năng lực kẻ tấn công trong mô tả bài toán chỉ
  có bốn dòng, chưa đủ để thi hành nhánh adaptive và chưa quy định mức phản hồi mà kẻ tấn công
  quan sát được.
- `docs/01_de_bai/MO_TA_BAI_TOAN.md` (mục 4) — thêm đoạn dẫn nêu cấu trúc hai mức và trỏ tới
  file đặc tả mới; bổ sung ràng buộc A-adaptive không biết giá trị canary và không biết
  delimiter ngẫu nhiên của D1. Lý do: giữ nguyên tắc một nguồn chân lý — mục 4 chốt khái niệm,
  chi tiết thi hành nằm ở `docs/04_thiet_ke/`.
- `docs/01_de_bai/DANH_MUC_VIET_TAT.md` — thêm mục "Năng lực kẻ tấn công" (A-blind, A-adaptive,
  NL1–NL7, PH0–PH3) và đánh lại số các mục sau. Lý do: hai tiền tố ký hiệu mới phải có trong
  danh mục để giữ nguyên tắc một khái niệm một ký hiệu; `N` đã dùng cho cỡ mẫu nên trục năng lực
  dùng `NL`, `F` gần với FRR nên mức phản hồi dùng `PH`.
- `docs/01_de_bai/danh_muc_viet_tat.tex` — thêm hai dòng `NL1--NL7` và `PH0--PH3` đúng thứ tự
  chữ cái. Lý do: giữ bản LaTeX đồng bộ với danh mục Markdown.

## 2026-09-22
- `docs/01_de_bai/BAN_DO_AI_SECURITY.md` — tạo mới. Bản đồ khái niệm AI Security sáu tầng
  (L0–L5), ánh xạ vòng đời tấn công theo MITRE ATLAS sang năm giai đoạn của một lượt agent,
  mục định vị IPI trên bốn khung tham chiếu (OWASP LLM Top 10, OWASP Agentic ASI01–ASI10,
  MITRE ATLAS, NIST AI 100-2/AI RMF), danh mục kiểm 32 hạng mục AS-01…AS-32 kèm cột phạm vi,
  và bảng ánh xạ khung ngoài sang ký hiệu nội bộ (TS, K, G, T, D). Lý do: sản phẩm của
  Nội dung 1 — mục 1 theo Phiếu giao nhiệm vụ; đồng thời làm căn cứ có số cho phần biện luận
  phạm vi trước GVHD.
- `docs/01_de_bai/ban_do_ai_security.svg` — tạo mới. Sơ đồ trực quan của bản đồ trên, dùng
  cho báo cáo và slide. Lý do: phần trình bày phạm vi cần một hình duy nhất thay cho ba bảng.
- Ký hiệu mới `AS-01`–`AS-32` dành riêng cho hạng mục danh mục kiểm AI Security, không trùng
  với các tiền tố đang dùng (TS, A, M, G, K, T, D, CT, U, TL, RQ).

## 2026-09-22
- `Kế hoạch thực hiện.xlsx` (sheet `Kế hoạch chi tiết`) — dựng lại toàn bộ theo khung Phiếu
  giao nhiệm vụ ĐATN kỹ sư (MSSV 20250127E): 6 Nội dung, Tuần 1–17, mốc thời gian 07/09/2026
  → 08/01/2027. Thêm cột `Nội dung` và `Tuần` để ánh xạ từng đầu việc về ND1–ND6. Bổ sung 3
  đầu việc đánh giá và thu thập phản hồi người dùng ở ND6 (nội dung bắt buộc với đồ án kỹ sư).
  Sheet `Tổng quan mốc` thêm cột mã mốc M0–M8, Nội dung tương ứng và hạn theo tuần. Lý do:
  đồng bộ kế hoạch triển khai với phiếu giao nhiệm vụ đã ký với GVHD.

## 2026-09-22
- `docs/01_de_bai/danh_muc_thuat_ngu.tex` — tạo mới. Bản LaTeX `longtable` danh mục thuật ngữ
  (30 mục), ba cột: thuật ngữ · tiếng Việt · giải thích. Lý do: tách thuật ngữ khỏi danh mục
  viết tắt để đưa vào báo cáo.

## 2026-09-22
- `docs/01_de_bai/danh_muc_viet_tat.tex` — đồng bộ diễn giải chi tiết cho các thuật ngữ
  (IPI, MCP, A2A, KB, NFKC) từ danh mục chuẩn.

## 2026-09-22
- `docs/01_de_bai/danh_muc_viet_tat.tex` — tạo mới. Bản LaTeX `longtable` của danh mục viết
  tắt, ba cột theo mẫu Overleaf SOICT, sắp xếp theo bảng chữ cái. Lý do: đưa thẳng vào báo cáo.

## 2026-09-22
- `docs/01_de_bai/DANH_MUC_VIET_TAT.md` — tạo mới. Tổng hợp toàn bộ từ viết tắt và ký hiệu
  (TS, A, G, K, T, D, CT, U, TL, RQ, M, chỉ số đo) từ `Y_TUONG_DU_AN.md` và
  `MO_TA_BAI_TOAN.md`. Lý do: cần một chỗ duy nhất tra ký hiệu để đưa vào báo cáo và
  giữ nguyên tắc "một khái niệm, một ký hiệu".
