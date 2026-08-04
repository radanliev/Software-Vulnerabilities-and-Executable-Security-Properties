from __future__ import annotations

import json
import sys

from app.tools.kb_retrieve import retrieve_tickets


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 2:
        print('usage: python -m app.agent <requester> <query>', file=sys.stderr)
        return 2

    requester, query = args
    print(json.dumps(retrieve_tickets(requester, query), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
