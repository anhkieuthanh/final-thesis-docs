# PAYLOAD CHƯA ĐO PILOT — việc treo STT-60

> File việc treo theo quy tắc cứng #10: cờ "chưa đo pilot" không ghi vào file payload (dữ liệu chỉ chứa dữ liệu).
> TA quyết (2026-10-26): giữ các payload này, không loại ở pilot. Vòng hiệu chỉnh đầu của STT-61 chạy đủ 63 ô trên
> commit đã sửa P1/P2-a/P4-a (cùng một `env_hash`) sẽ đo chúng lần đầu. Quy tắc loại theo `activation_check`
> (payload_taxonomy.md mục 5) áp ở vòng hiệu chỉnh CUỐI, không áp ở vòng này.

## Bối cảnh

Pilot STT-60 (`pilot-B1-20261026T014743Z` + lô K1 chạy lại `pilot-B1-20261026T034810Z`) chạy 40 ca, chạm 29/63
payload của corpus. 34 payload còn lại chưa chạy pilot lần nào — gồm 14 payload P4-a (mới thêm) và 20 payload cũ không
rơi vào 40 ca pilot. Danh sách dưới đây sinh bằng cách đối chiếu `payload_id` trong trace hai lô với corpus hiện tại.

## Danh sách 34 payload

| payload_id | kỹ thuật | mục tiêu | lang |
|---|---|---|---|
| P-T1-G2-EN-001 | T1 | G2 | en |
| P-T1-G2-EN-003 | T1 | G2 | en |
| P-T1-G2-VI-002 | T1 | G2 | vi |
| P-T1-G2-VI-003 | T1 | G2 | vi |
| P-T1-G2-VI-901 | T1 | G2 | vi |
| P-T2-G1-VI-002 | T2 | G1 | vi |
| P-T2-G2-EN-001 | T2 | G2 | en |
| P-T2-G2-VI-001 | T2 | G2 | vi |
| P-T2-G3-EN-001 | T2 | G3 | en |
| P-T2-G3-VI-001 | T2 | G3 | vi |
| P-T3-G3-EN-001 | T3 | G3 | en |
| P-T3-G3-VI-001 | T3 | G3 | vi |
| P-T4-G1-EN-001 | T4 | G1 | en |
| P-T4-G1-VI-002 | T4 | G1 | vi |
| P-T4-G2-EN-001 | T4 | G2 | en |
| P-T4-G2-VI-001 | T4 | G2 | vi |
| P-T4-G3-EN-001 | T4 | G3 | en |
| P-T4-G3-VI-001 | T4 | G3 | vi |
| P-T5-G1-EN-001 | T5 | G1 | en |
| P-T5-G1-VI-001 | T5 | G1 | vi |
| P-T5-G2-EN-001 | T5 | G2 | en |
| P-T5-G2-VI-001 | T5 | G2 | vi |
| P-T8-G1-MIX-010 | T8 | G1 | mixed |
| P-T8-G1-VI-002 | T8 | G1 | vi |
| P-T8-G1-VI-003 | T8 | G1 | vi |
| P-T8-G1-VI-004 | T8 | G1 | vi |
| P-T8-G1-VI-006 | T8 | G1 | vi |
| P-T8-G1-VI-008 | T8 | G1 | vi |
| P-T8-G1-VI-009 | T8 | G1 | vi |
| P-T8-G2-MIX-005 | T8 | G2 | mixed |
| P-T8-G2-VI-001 | T8 | G2 | vi |
| P-T8-G2-VI-002 | T8 | G2 | vi |
| P-T8-G3-VI-001 | T8 | G3 | vi |
| P-T8-G3-VI-004 | T8 | G3 | vi |

## Khi nào gỡ file này

Sau vòng hiệu chỉnh đầu của STT-61: mọi payload trên đã có ít nhất một run D=OFF. Lúc đó cập nhật/gỡ file, và áp quy tắc
loại ở vòng cuối theo `payload_taxonomy.md` mục 5.
