# KẾ HOẠCH HOÀN THIỆN ĐỒ ÁN SAU GÓP Ý GVHD 08/11/2026

> Tài liệu này soạn với sự hỗ trợ của AI (Claude) từ `Y_TUONG_DU_AN.md`, `Kế hoạch thực hiện.xlsx`,
> `CHANGELOG_TAI_LIEU.md`, `Chuẩn bị báo cáo tiến độ 06.11.2026.md`, `config/experiment.yaml` và các chương
> báo cáo hiện có. GVHD đã duyệt cả năm điểm ở mục 6.

## 1. Góp ý của GVHD và hệ quả

Góp ý: mục tiêu đồ án là chứng minh sinh viên có làm, có nghiên cứu tìm hiểu; kết quả thực nghiệm không cao
cũng không sao; cần chỉ ra rõ chỗ có đóng góp của cá nhân.

Hệ quả cho kế hoạch:

1. **Thôi đuổi cổng ASR 20–80%.** Đã đi hết ba núm hợp lệ của giao thức §10.3 (vòng 0–2), có thêm lô dò và lô
   đối chứng. Tiếp tục chỉnh để lấy số đẹp là trái chính §10.3. Đóng STT-61, chạy ma trận ở chế độ sàn và báo cáo
   toàn bộ hành trình như một kết quả.
2. **Thu nhỏ quy mô thực nghiệm, giữ đủ chiều.** Mỗi khối B1–B6 vẫn có số liệu thật, nhưng ít run hơn. Thực
   nghiệm là bằng chứng hệ thống chạy được và đo được, không phải để xếp hạng mô hình.
3. **Dời trọng tâm sang báo cáo đóng góp.** Chương 5 ("Các giải pháp và đóng góp nổi bật") thành chương trọng
   tâm; mỗi đóng góp có bằng chứng truy nguồn được trong repo.
4. **Giữ nguyên các nội dung bắt buộc của phiếu**: ND5 thử nghiệm, ND6 đánh giá với người dùng thực.
5. **Kết thúc sớm hơn một tuần** để có đệm trước hạn 08/01/2027.

## 2. Hiện trạng tính tới Tuần 10 (09/11/2026)

| Phần | Trạng thái thực tế |
|---|---|
| ND1–ND3 | Xong (M0, M1 đạt; phụ lục M1b còn chờ GVHD ký) |
| ND4 — mã nguồn | Xong: CoreA, 5 tool + MCP server, canary, scorer (cổng 8/8, lần gần nhất `gate_20261106T063243Z.json`), injector K1/K2a/K2b, T1–T8, D1–D4 có unit test, kẻ tấn công thích ứng, console |
| USR nền | Xong: A1 93,75%, A2 93,75%, A3 96,6% (mức run, `utility_baseline_rejudged_summary.csv`) |
| ND5 — hiệu chỉnh (STT-61) | Đã đi hết núm, ASR dưới cổng; corpus `v-attack-1.1` đã có lớp gắn ngữ cảnh; đã sửa `{run_id}` G3, K2b `delivered`, resume lô |
| ND5 — ma trận B1–B5 | Chưa chạy |
| ND6 | Chưa bắt đầu (trừ console/demo STT-82 đã làm sớm) |
| Báo cáo | Chương 1–3 có nháp dài; Chương 4–6 mới có khung (`Chuong4.tex` 43 dòng, `Chuong5.tex` 37, `Chuong6.tex` 16) |

Sức chứa còn lại: 8 tuần (Tuần 10 → Tuần 17) × 20 giờ = 160 giờ.

## 3. Bản đồ đóng góp cá nhân — xương sống của Chương 5

Mỗi dòng là một mục của Chương 5 theo khung Vấn đề → Giải pháp → Kết quả và giới hạn. Cột "Bằng chứng" là thứ
phải có trong repo trước khi viết.

| # | Đóng góp | Phần tự làm (không lấy sẵn) | Bằng chứng | Còn thiếu |
|---|---|---|---|---|
| C1 | Testbed agent doanh nghiệp Việt có kiểm soát | Vòng lặp CoreA tự viết, 5 tool, MCP server, lớp tiêm K2a/K2b mô phỏng MCP server bị kiểm soát, `customers.db` Faker `vi_VN`, MailHog + canary listener, chạy đầu-cuối không gì rời máy | `src/agent/`, `src/tools/`, `src/attack/injector_*.py`, `tests/`, docker compose | Hình kiến trúc vào báo cáo (đã có `kien_truc_lab_ipi_guard.png`) |
| C2 | Bộ chấm tất định, không dùng LLM, tách "model từ chối" khỏi "phòng thủ chặn" | Canary sinh mỗi run, dò sau khi gỡ base64/hex/percent/homoglyph/đảo chuỗi/mảnh; G2 theo `expected_tool`; trường `blocked_by` | `src/eval/scorer.py`, `results/scorer_gate/*.json` (8/8 × 100 lần) | — |
| C3 | Ba kỹ thuật tự đề xuất T6–T8, trong đó T8 đặc thù tiếng Việt | Đặc tả, payload, `activation_check` | `docs/04. Design/payload_taxonomy.md`, `data/payloads/` | Số đo T6–T8 từ B1 rút gọn |
| C4 | Bốn phòng thủ D1–D4, D3 theo `task_type` người dùng chọn trước | D3 máy trạng thái R1–R4 ngoài LLM, preset `d3_no_confirm`, tham số tại `config/defenses.yaml` | `src/defense/`, `defense_spec.md`, unit test | Cặp số ASR + USR từ B2/B3 rút gọn |
| C5 | Giao thức hiệu chỉnh độ khó công khai và phát hiện về payload gắn ngữ cảnh | Ba vòng chỉnh có diff + ASR; phát hiện payload bám nghiệp vụ quyết định ASR (gắn ngữ cảnh 8,8% so với 0,5%; lô dò 22–33%; lô đối chứng A2 53%) | `results/calibration/lab_calibration.md` | Đường cong độ nhạy (hình) |
| C6 | Các lỗi đo lường tự phát hiện và sửa | `{run_id}` G3 làm `g3_hit` luôn 0; K2b `delivered` hằng 1 (VT-17); canary DB chỉ ở id=1 (VT-19); resume chạy trùng (VT-20); URL tồn kho 404; generator đổi carrier | `CHANGELOG_TAI_LIEU.md`, commit lab `f3f7244`, `3749ad1` | Bảng tổng hợp lỗi → hệ quả → cách phát hiện → cách sửa |
| C7 | Đo hữu dụng có soát tay | Judge + dữ kiện cứng có quyền veto; soát tay, chấm lại, công khai số đổi trượt ↔ đạt | `utility_baseline_rejudged*.csv`, `utility_baseline_judge_compare.csv` | — |
| C8 | Console và demo trực tiếp | FastAPI + React, xem trace từng bước, bằng chứng chấm G1–G3 | `src/console/`, `console/` | Kịch bản demo |

Cách viết: kết quả thấp hay bằng 0 vẫn là kết quả nếu giải thích được vì sao và có bằng chứng. C5 và C6 là chỗ
thể hiện nghiên cứu thật rõ nhất — nêu cụ thể "phát hiện bằng cách nào", không chỉ "đã sửa".

## 4. Điều chỉnh thực nghiệm

| Khối | Kế hoạch cũ | Đề xuất | Lý do |
|---|---|---|---|
| Hiệu chỉnh STT-61 | Chỉnh tới khi ASR vào 20–80% | **Đóng.** Một lô vòng 0 nhỏ trên `v-models-1.2` sau bản sửa `{run_id}` để có số G3 trung thực, rồi khóa `v-attack-1.1` | Hết núm hợp lệ; §10.3 cấm chỉnh tiếp lấy số đẹp |
| Corpus | Cách A hoặc B chưa chọn | **Cách B** (ô có payload gắn ngữ cảnh chỉ dùng payload gắn ngữ cảnh) | Mẫu hiệu chỉnh và ma trận cùng thành phần; đối chứng cũ ↔ gắn ngữ cảnh đã có ở lô đối chứng riêng và ở 37 ô còn payload cũ |
| B1 (RQ1, RQ2) | 63 ô × 30 run × 3 model = 5.670 run | 63 ô × **10** run × 3 model = **1.890 run** | Đủ cho bảng mô tả kèm Wilson; khai rõ khoảng rộng |
| STT-62 phương sai | 20 mẫu × 5 lần | **Cắt**; N = 10 cố định, khai ở hạn chế | Không còn cần tối ưu N |
| B2 (RQ3) | ≤ 12 ô S_def × 7 preset × 30 × A2, A3 | **6 ô** × 7 preset × **10** × A2, A3 = 840 run. Nếu dưới 6 ô đạt `min_ci_low` thì lấy 6 ô ASR cao nhất và khai | ASR nền sàn thì ít ô đạt ngưỡng |
| B3 (RQ4) | 60 câu × 7 preset × 5 lần × A2, A3 | 60 câu × 7 preset × **2** lần × A2, A3 = 1.680 run | Giữ yêu cầu "mỗi cấu hình có cả ASR và USR" |
| B4 (tập xác nhận A1) | 516 run | **Cắt** | A1 đã vào B1 từ `v-models-1.2` |
| B5 (RQ5) | ≤ 6 ô × 5 preset × 10 chuỗi | **3 ô × 5 preset × 5 chuỗi** = 75 chuỗi, A2 | Đủ minh họa ARR; ARR không xác định khi DSR(blind) ≈ 0 thì báo cáo đúng như vậy |
| B6 (RQ6) | HN-CC + HN-OW × 3 model × 50 mẫu | **Bỏ HN-CC.** HN-OW trên A2, 20 mẫu; nếu cắm harness tốn quá 8 giờ thì chỉ giữ bảng đối chiếu định tính STT-78 | Bảng đối chiếu D1–D4 ↔ harness là phần không cắt |
| STT-95 kiểm trôi model | 20 mẫu trước bảo vệ | **Giữ**, chạy Tuần 16 | Rẻ, chứng minh tái lập |

Mọi lô vẫn trình duyệt trước (lệnh, phạm vi, mục đích, chi phí) và chạy test nhỏ trước. Chi phí từng lô ước lượng
bằng dry-run `run_matrix.py` khi trình.

Không đổi: bộ đo đã khóa, ba model `v-models-1.2`, kỹ thuật `v-attack-1.1`, scorer, định nghĩa chỉ số.

## 5. Lịch mới Tuần 10 → Tuần 17

| Tuần | Thời gian | Thực nghiệm / mã | Báo cáo | Mốc |
|---|---|---|---|---|
| Tuần 10 | 09/11 → 15/11 | GVHD xác nhận mục 6. Lô vòng 0 nhỏ G3 sau bản sửa. Khóa `v-attack-1.1`, sửa `experiment.yaml` theo mục 4. Viết kết luận + hình đường cong độ nhạy ở `lab_calibration.md` | Khung Chương 5 theo C1–C8; bảng lỗi C6 | Đóng STT-61 |
| Tuần 11 | 16/11 → 22/11 | B1 rút gọn (test 1 run/ô trước, rồi full). STT-67: ASR_e2e, ASR_cond, DSR, ARR vào `src/eval/metrics.py` | Chương 4: thiết lập thực nghiệm | **M4**: bảng ASR hai chỉ số × 3 model |
| Tuần 12 | 23/11 → 29/11 | B2 + B3 rút gọn cùng lệnh. STT-68 bảng và biểu đồ | Chương 4: kết quả B1; Chương 3 hoàn tất (STT-59) | — |
| Tuần 13 | 30/11 → 06/12 | B5 rút gọn. STT-73 Pareto một và hai bộ điểm. Một file nháp chung RQ1–RQ5 (gộp STT-70, 74, 76) | Chương 4: phòng thủ, thích ứng | **M5**: 7 cấu hình × A2, A3 có ASR + USR |
| Tuần 14 | 07/12 → 13/12 | STT-78 bảng đối chiếu D1–D4 ↔ harness; HN-OW 20 mẫu (hoặc cắt). STT-82/84 kịch bản demo + video dự phòng. STT-83 hướng dẫn cài đặt | Chương 5 hoàn tất C1–C8 | **M6** |
| Tuần 15 | 14/12 → 20/12 | STT-85–87 buổi thử 3–5 người dùng, phiếu khảo sát, tổng hợp phản hồi. STT-92 dọn repo, gitleaks | Chương 4 mục đánh giá người dùng; Chương 6 | **M7**: demo + phản hồi người dùng |
| Tuần 16 | 21/12 → 27/12 | STT-95 kiểm trôi model | Ráp 6 chương (STT-88), STT-90, STT-91 TLTK, rà nhất quán ký hiệu. Gửi GVHD bản đủ | — |
| Tuần 17 | 28/12 → 08/01/2027 | Đệm | Sửa theo góp ý GVHD; STT-93 slide; STT-94 câu phản biện; tổng duyệt | **M8**: nộp, bảo vệ |

Ước lượng giờ: Tuần 10–13 khoảng 20 giờ/tuần (thực nghiệm chạy nền, giờ người chủ yếu là soát trace và viết);
Tuần 14–15 khoảng 22 giờ; Tuần 16–17 khoảng 18 giờ. Tổng ≈ 160 giờ, khớp sức chứa.

Họp GVHD: 15/11 (xác nhận mục 6), 29/11 (kết quả B1), 13/12 (B2–B5 + Chương 5), 27/12 (bản đủ).

## 6. Cần GVHD xác nhận

| # | Nội dung | Chạm vào | Ý kiến GVHD |
|---|---|---|---|
| 6.1 | Đóng hiệu chỉnh: dừng ở vòng 2, chạy ma trận ở chế độ sàn, báo cáo mọi vòng như đường cong độ nhạy (Mục 4 phương án (a) và Mục 5 phương án (1) của `Xin ý kiến GVHD — họp kế tiếp.md`) | Quy tắc cứng #5 nửa sau; tiêu chí M4 | ☑ Đồng ý · ☐ Ý kiến khác |
| 6.2 | Corpus cách B | `Duyệt v-attack-1.1 — hai cách mở rộng corpus.md` | ☑ Đồng ý · ☐ Giữ cách A |
| 6.3 | Thu nhỏ B1, B2, B3, B5; cắt B4, STT-62 | Checklist chốt phạm vi mục 5 (N = 30) | ☑ Đồng ý · ☐ Ý kiến khác |
| 6.4 | Bỏ HN-CC; HN-OW tùy chọn, bảng đối chiếu giữ | Phạm vi §10.2 dòng Harness, M6 | ☑ Đồng ý · ☐ Ý kiến khác |
| 6.5 | Chương 5 trình bày C1–C8 làm đóng góp cá nhân | Cấu trúc báo cáo | ☑ Đồng ý · ☐ Ý kiến khác |

## 7. Việc phải làm sau khi duyệt

TA tự sửa `Kế hoạch thực hiện.xlsx`:

- Trạng thái đang lệch thực tế: STT-16 (Chương 2 đã có nháp), STT-60 (pilot đã xong), STT-61 (đang làm); sheet
  "Tổng quan mốc": M1b, M2, M3, M3b vẫn ghi "Chưa bắt đầu".
- Chuyển "Đã cắt": STT-62, STT-64 (gộp vào B1), STT-89 (đã cắt sẵn).
- Gộp: STT-65, STT-66 vào một đầu việc B1 rút gọn; STT-70, STT-74, STT-76 vào một nháp RQ chung.
- Rút gọn: STT-71, 72, 75, 79, 80 theo mục 4; dời Deadline theo mục 5.
- Sheet "Tổng quan mốc": tiêu chí M4–M7 theo mục 5.

Claude sửa (sau khi GVHD xác nhận), mỗi thay đổi một mục CHANGELOG:

- `Y_TUONG_DU_AN.md` §10.2 (Harness, N), §10.3 (kết luận hiệu chỉnh), §15 (lịch, mốc, danh sách cắt).
- `CLAUDE.md` quy tắc cứng #5 nửa sau.
- `docs/04. Design/06. Giao thức thực nghiệm.md`, `ipi-agent-lab/config/experiment.yaml` (`n_per_cell`, `max_cells`,
  `repeats`, `chains_per_cell`, B4, B6).
- `Chốt phạm vi và checklist ký GVHD.md`, `Phụ lục M1b — trình GVHD ký.md` (đang còn B1 = 3.780 run).
