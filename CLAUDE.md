# CLAUDE.md — Hướng dẫn làm việc trên dự án "Final Thesis"

> Tài liệu này soạn với sự hỗ trợ của AI (Claude). Đây là hướng dẫn cho AI và trợ lý code,
> không thay thế `Y_TUONG_DU_AN.md` (ý tưởng tổng thể) hay các nguồn chân lý ở mục 2.

## 1. Đề tài

Nghiên cứu và xây dựng hệ thống đánh giá, phòng chống tấn công tiêm nhiễm gián tiếp
(Indirect Prompt Injection — IPI) trên AI Agent dùng RAG + MCP tool-calling.

Đồ án **ứng dụng** — sản phẩm bàn giao là công cụ. Nhịp 20 giờ/tuần, 16 tuần dương lịch.

Bốn đóng góp cốt lõi: testbed agent doanh nghiệp Việt có kiểm soát · bộ đo ASR/DSR/ARR/USR
lặp lại được · bốn cơ chế phòng thủ D1–D4 đánh giá theo cặp an toàn/hữu dụng · đo độ bền
trước kẻ tấn công thích ứng.

## 2. Nguồn chân lý — không có nguồn thứ năm

| Hỏi về | Đọc |
|---|---|
| Ý tưởng tổng thể, mọi quyết định đã chốt | `Y_TUONG_DU_AN.md` |
| Bài toán: phạm vi, threat model, biến, RQ | `docs/01_de_bai/MO_TA_BAI_TOAN.md` |
| Kế hoạch: lịch, mốc, ngân sách | `docs/02_ke_hoach/KE_HOACH.md` |
| Trạng thái task — cái gì đã DONE | `docs/02_ke_hoach/TASKS.md` — **luôn kiểm trước khi đề xuất việc kế tiếp, đừng giả định** |

Chỉ giữ bản hiện hành trong cây thư mục. Lịch sử thay đổi ghi ở
`docs/06_theo_doi/CHANGELOG_TAI_LIEU.md`.

## 3. Hai repo Git tách biệt — chủ ý

- Repo ngoài: tài liệu, kế hoạch, báo cáo. **Phải có remote** — không để tồn tại một bản
  duy nhất trên đĩa.
- `ipi-agent-lab/`: mã nguồn, repo Git riêng có remote riêng, bị `.gitignore` của repo
  ngoài loại trừ. Khi làm việc trong đó, luôn `cd` vào trước khi chạy `git`.
- `benchmarks/`: clone bên thứ ba, không theo Git.
- Mọi file dữ liệu thô của một cổng nghiệm thu phải được Git theo dõi, hoặc có bản sao
  ngoài máy. Số nào vào báo cáo thì số đó phải truy nguồn được.

## 4. Mười quy tắc cứng — không được vi phạm

1. **Không sửa file bộ đo đã khóa** (`data/benign_queries.json`, `data/carrier_tasks.json`,
   khóa bằng tag `v-bench-1.0`). Mọi thay đổi ghi vào
   `docs/06_theo_doi/CHANGELOG_TAI_LIEU.md` kèm lý do — **không** ghi changelog trong chính
   file JSON.
2. **Không nhận xét hay dùng số liệu về AgentDojo / AutoDojo / MCPTox nếu chưa thực sự cài
   và chạy**, và bằng chứng chạy thật phải nằm trong repo.
3. **Không thêm bước phân loại ý định tự do (regex/NLU/LLM) vào D3.** `task_type` là input
   người dùng chọn trước.
4. **Mọi tham số hành vi của D1–D4 nằm ở `config/defenses.yaml`**, không hard-code trong
   `src/defense/*.py`.
5. **Không sang giai đoạn ma trận nếu kiểm chứng scorer chưa đạt ngưỡng đã chốt.** Không
   chạy full matrix nếu hiệu chỉnh độ khó chưa đưa ASR pilot vào 20–80%.
6. **Dữ liệu là mô phỏng** — `customers.db` sinh bằng Faker `vi_VN`, seed cố định. Không
   đưa dữ liệu cá nhân hay khách hàng thật vào bất kỳ đâu trong dự án.
7. **MCPTox chỉ chạy chế độ mô phỏng**, không nhắm MCP server thật của bên thứ ba. Payload
   `verbatim` / `adapted` phải dẫn đúng điều khoản giấy phép qua trường `source.license`.
8. **Không ghi "model từ chối" thành "phòng thủ chặn".** `blocked_by ∈ {defense,
   model_refusal, harness}` là trường bắt buộc trong trace.
9. **Phiên bản harness phải pin và ghi vào trace.** Không đổi model đích sau
   `v-models-1.0`; không thêm kỹ thuật payload sau `v-attack-1.0`.
10. **Tài liệu chỉ giữ bản hiện hành.** Không nhãn phiên bản trong thân bài, không bảng đối
    chiếu bản cũ, không dòng "cập nhật ngày", không ghi chú sửa đổi. Sửa là thay thẳng nội
    dung rồi ghi một mục lên đầu `CHANGELOG_TAI_LIEU.md`: ngày · file · thay đổi · lý do.
    Áp cho **cả file dữ liệu `.json`** — dữ liệu chỉ chứa dữ liệu. Biểu mẫu chờ ký và việc
    còn treo không phải ghi chú lịch sử: để ở file riêng trong `docs/06_theo_doi/`.

Hai quy tắc vận hành kèm theo: kiểm chi phí API mỗi 2 giờ trong 4 giờ đầu mọi lần chạy lô,
vượt 120% dự toán thì dừng ngay; hạn mức lấy từ `.env` và **không mở hay sửa `.env` thay
người dùng**. Nội dung do AI soạn phải ghi rõ ở đầu tài liệu, đặc biệt với bản trình GVHD.

## 5. Một khái niệm, một ký hiệu

| Tiền tố | Dùng cho |
|---|---|
| `TS1`–`TS3` | Ba tài sản cần bảo vệ (system prompt · customers.db · quyền gọi tool) |
| `A1`–`A3` | Ba mô hình đích (frontier · doanh nghiệp Việt · lớp rẻ) |
| `M0`–`M8` | Các mốc nghiệm thu |
| `G1`–`G3` | Mục tiêu tấn công · `K1`–`K5` kênh · `T1`–`T9` kỹ thuật · `D1`–`D4` phòng thủ |
| `CT-01`–`CT-06` | Tác vụ chở · `U1`–`U5` nhóm câu hỏi lành tính |

Không tái sử dụng một tiền tố cho hai khái niệm. Ngưỡng nghiệm thu viết một lần, một chỗ.

## 6. Quy ước kỹ thuật

- Dependency bằng **uv**: `cd ipi-agent-lab && uv sync --all-groups`.
- Test `uv run pytest -v`; lint `uv run ruff check .` (line-length 100, target py310).
- Commit message gắn mã task: `docs(W2-09): ...` / `feat(W2-09): ...`.
- Model đích cấu hình qua `config/models.yaml` + `.env` (mẫu ở `.env.example`). Đổi model =
  đổi `.env` + một khối `targets`, **không sửa code**.
- `config/` là hợp đồng, viết trước `src/`.
- Đổi cấu trúc thư mục thì sửa luôn mọi tham chiếu đường dẫn trong `src/`, `config/`,
  `scripts/` và tài liệu — đây là lớp lỗi đã xảy ra một lần.

## 7. Nhịp làm việc

- Đầu tuần: đọc bước lớn và mốc phải đạt trong `KE_HOACH.md`.
- Cuối tuần: đối chiếu % giờ đã dùng, rà ngưỡng rủi ro, đếm hạng mục ngoài phạm vi.
- Họp GVHD tối thiểu 2 tuần một lần.
- Viết báo cáo 2 giờ mỗi tuần, không dồn cuối.

## 8. Khi không chắc

Nếu một hành động ảnh hưởng tới bộ đo đã khóa, ngân sách API, hoặc phạm vi đã chốt với
GVHD — **dừng lại và hỏi trước**, đừng tự quyết.
