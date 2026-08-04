# Software-Vulnerabilities-and-Executable-Security-Properties

Week 1 Demo 1 Software Vulnerabilities and Executable Security Properties

## Layout

- `app/tools/kb_retrieve.py` — safe retrieval logic at `v0-clean`, deliberately vulnerable logic at `v1-vulnerability`
- `tests/test_kb_retrieve.py` — verifies tenant isolation and demonstrates the leak on the vulnerable tag
- `invariants.yaml` — pre-populated with `INV-1`
- `threat_model.yaml` — empty stub for later weeks
- `app/tools/ticket_lookup.py`, `app/tools/email_draft.py`, `identity.yaml`, `memory/`, `deploy/` — scaffolded for later weeks

## Runbook

Safe baseline:

```bash
git checkout v0-clean
pytest tests/test_kb_retrieve.py
```

Expected output:

```text
============================= test session starts ==============================
collected 3 items

tests/test_kb_retrieve.py ...                                            [100%]

============================== 3 passed in 0.XXs ===============================
```

Reveal the defect:

```bash
git diff v0-clean v1-vulnerability -- app/tools/kb_retrieve.py
```

Vulnerable version:

```bash
git checkout v1-vulnerability
pytest tests/test_kb_retrieve.py
python -m app.agent customer_a "TICKET-100' OR '1'='1"
```

Expected pytest output:

```text
============================= test session starts ==============================
collected 3 items

tests/test_kb_retrieve.py .FF                                            [100%]

=================================== FAILURES ===================================
...
E       AssertionError: customer_b's ticket content returned to customer_a
...
========================= 2 failed, 1 passed in 0.XXs ==========================
```

Expected PoC behavior: the command returns all three tickets on `v1-vulnerability`.
