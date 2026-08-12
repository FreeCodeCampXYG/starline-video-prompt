#!/usr/bin/env python3
"""检查视频提示词的字符上限与导演结构，不调用任何生成服务。"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def prompt_body(text: str) -> str:
    """优先取 Markdown 中的 text 代码块，兼容直接输入纯提示词。"""
    match = re.search(r"```text\s*(.*?)\s*```", text, flags=re.DOTALL)
    return (match.group(1) if match else text).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a video prompt without submitting it.")
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--limit", type=int, required=True, help="用户已确认的平台字符上限")
    parser.add_argument("--confirmed-limit", action="store_true", help="确认 --limit 来自用户或当前平台页面，而非默认猜测")
    parser.add_argument("--require-timed-score", action="store_true")
    args = parser.parse_args()
    if not args.confirmed_limit:
        raise SystemExit("请先由用户确认提示词字符上限，再传入 --limit <N> --confirmed-limit")
    if args.limit <= 0:
        raise SystemExit("提示词字符上限必须为正整数")

    body = prompt_body(args.prompt.read_text(encoding="utf-8"))
    failures: list[str] = []
    if len(body) > args.limit:
        failures.append(f"提示词为 {len(body)} 字符，超过 {args.limit} 上限")
    if not body:
        failures.append("提示词为空")
    if args.require_timed_score:
        lower = body.lower()
        for marker in ("0", "seconds"):
            if marker not in lower:
                failures.append(f"缺少 20 秒镜头必要结构：{marker}")
        if not any(marker in lower for marker in ("end frame", "continuity frame", "final frame")):
            failures.append("缺少 20 秒镜头必要结构：稳定尾帧契约")
    print(f"prompt_chars={len(body)} limit={args.limit}")
    if failures:
        for failure in failures:
            print(f"错误：{failure}")
        raise SystemExit(2)
    print("验证通过：字符数与导演结构符合本地约束")


if __name__ == "__main__":
    main()
