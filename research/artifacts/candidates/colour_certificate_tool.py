#!/usr/bin/env python3
"""Candidate certificate construction/checking, not a trusted verifier receipt.

Input JSON: {"n": nonnegative integer, "edges": [[u, v, colour], ...]}.
Vertex IDs: 0,...,n-1. Colours: 1,...,5. Graphs must be simple.
For a FIXED colouring, construct five bipartitions or one odd-cycle witness.
This program does not search for a colouring or prove universal existence.

Planned runtime: Python 3.10+, one process, one thread, timeout 30 seconds,
256 MiB memory, input <=1 MiB, n<=20000, m<=100000. No execution is asserted.
"""
from __future__ import annotations
import argparse
from collections import deque
import hashlib
import json
from pathlib import Path
from typing import Any

MAX_INPUT_BYTES = 1_048_576
MAX_N = 20_000
MAX_M = 100_000

def freeze_graph(data: Any) -> tuple[int, list[tuple[int, int, int]]]:
    if not isinstance(data, dict) or set(data) != {"n", "edges"}:
        raise ValueError("Input must contain exactly n and edges")
    n, raw = data["n"], data["edges"]
    if type(n) is not int or not 0 <= n <= MAX_N:
        raise ValueError("n is outside the admitted finite input range")
    if not isinstance(raw, list) or len(raw) > MAX_M:
        raise ValueError("Invalid or excessive edge list")
    seen: set[tuple[int, int]] = set()
    edges: list[tuple[int, int, int]] = []
    for entry in raw:
        if not isinstance(entry, list) or len(entry) != 3:
            raise ValueError("Each edge must be [u,v,colour]")
        u, v, colour = entry
        if any(type(x) is not int for x in entry):
            raise ValueError("Edge entries must be integers, not booleans")
        if not (0 <= u < n and 0 <= v < n) or u == v:
            raise ValueError("Invalid endpoint or loop")
        if not 1 <= colour <= 5:
            raise ValueError("Invalid colour")
        u, v = min(u, v), max(u, v)
        if (u, v) in seen:
            raise ValueError("Parallel or duplicate edge")
        seen.add((u, v))
        edges.append((u, v, colour))
    return n, sorted(edges)

def digest_graph(n: int, edges: list[tuple[int, int, int]]) -> str:
    raw = json.dumps({"n": n, "edges": edges}, sort_keys=True,
                     separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def tree_path(u: int, v: int, parent: list[int], depth: list[int]) -> list[int]:
    left: list[int] = []
    right: list[int] = []
    while depth[u] > depth[v]:
        left.append(u)
        u = parent[u]
    while depth[v] > depth[u]:
        right.append(v)
        v = parent[v]
    while u != v:
        left.append(u)
        right.append(v)
        u, v = parent[u], parent[v]
    return left + [u] + list(reversed(right))

def construct(data: Any) -> dict[str, Any]:
    n, edges = freeze_graph(data)
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, colour in edges:
        adjacency[u].append((v, colour))
        adjacency[v].append((u, colour))
    sides: list[list[int]] = []
    frozen_sha = digest_graph(n, edges)
    for deleted in range(1, 6):
        side = [-1] * n
        parent = [-1] * n
        depth = [0] * n
        for root in range(n):
            if side[root] != -1:
                continue
            side[root] = 0
            parent[root] = root
            queue = deque([root])
            while queue:
                u = queue.popleft()
                for v, colour in adjacency[u]:
                    if colour == deleted:
                        continue
                    if side[v] == -1:
                        side[v] = 1 - side[u]
                        parent[v], depth[v] = u, depth[u] + 1
                        queue.append(v)
                    elif side[v] == side[u]:
                        path = tree_path(u, v, parent, depth)
                        return {"kind": "odd_cycle", "graph_sha256": frozen_sha,
                                "deleted_colour": deleted, "vertices": path + [u]}
        sides.append(side)
    return {"kind": "five_bipartitions", "graph_sha256": frozen_sha,
            "sides": sides}

def check(data: Any, certificate: Any) -> bool:
    """Check the displayed finite witness by local edge conditions only."""
    try:
        n, edges = freeze_graph(data)
        if not isinstance(certificate, dict):
            return False
        if certificate.get("graph_sha256") != digest_graph(n, edges):
            return False
        if certificate.get("kind") == "five_bipartitions":
            sides = certificate.get("sides")
            if not isinstance(sides, list) or len(sides) != 5:
                return False
            if any(not isinstance(row, list) or len(row) != n or
                   any(type(bit) is not int or bit not in (0, 1) for bit in row)
                   for row in sides):
                return False
            return all(sides[i - 1][u] != sides[i - 1][v]
                       for u, v, colour in edges for i in range(1, 6)
                       if i != colour)
        if certificate.get("kind") != "odd_cycle":
            return False
        deleted = certificate.get("deleted_colour")
        vertices = certificate.get("vertices")
        if type(deleted) is not int or deleted not in range(1, 6):
            return False
        if not isinstance(vertices, list) or not 4 <= len(vertices) <= n + 1:
            return False
        if any(type(v) is not int or not 0 <= v < n for v in vertices):
            return False
        length = len(vertices) - 1
        if length % 2 != 1 or vertices[0] != vertices[-1]:
            return False
        if len(set(vertices[:-1])) != length:
            return False
        edge_colours = {(u, v): colour for u, v, colour in edges}
        for u, v in zip(vertices, vertices[1:]):
            colour = edge_colours.get((min(u, v), max(u, v)))
            if colour is None or colour == deleted:
                return False
        return True
    except (ValueError, TypeError, KeyError):
        return False

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--check", type=Path, help="Check an existing certificate")
    args = parser.parse_args()
    try:
        raw = args.input.read_bytes()
        if len(raw) > MAX_INPUT_BYTES:
            raise ValueError("Input exceeds the byte limit")
        data = json.loads(raw)
        if args.check is not None:
            raw_certificate = args.check.read_bytes()
            if len(raw_certificate) > MAX_INPUT_BYTES:
                raise ValueError("Certificate exceeds the byte limit")
            certificate = json.loads(raw_certificate)
            valid = check(data, certificate)
            print(json.dumps({"certificate_valid": valid,
                              "scope": "fixed_colouring_candidate_check"}))
            return 0 if valid else 1
        certificate = construct(data)
        print(json.dumps(certificate, separators=(",", ":")))
        return 0
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(2, f"Input error: {exc}\n")

if __name__ == "__main__":
    raise SystemExit(main())
