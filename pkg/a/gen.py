import argparse
import itertools
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('out')
    args = parser.parse_args()

    for a, b, c, d in itertools.product(range(16), repeat=4):
        imports = []
        fns = []
        if a > 0:
            prev = a - 1
            # imports.append(f"import {{ a as i }} from '../../../{prev:x}/{b:x}/{c:x}/{d:x}'")
            imports.append(f'const {{ a: i }} = require("../../../{prev:x}/{b:x}/{c:x}/{d:x}")')
            fns.append("i")
        if b > 0:
            prev = b - 1
            # imports.append(f"import {{ b as j }} from '../../../{a:x}/{prev:x}/{c:x}/{d:x}'")
            imports.append(f'const {{ b: j }} = require("../../../{a:x}/{b:x}/{prev:x}/{d:x}")')
            fns.append("j")
        if c > 0:
            prev = c - 1
            # imports.append(f"import {{ c as k }} from '../../../{a:x}/{b:x}/{prev:x}/{d:x}'")
            imports.append(f'const {{ c: k }} = require("../../../{a:x}/{b:x}/{prev:x}/{d:x}")')
            fns.append("k")
        if d > 0:
            prev = d - 1
            # imports.append(f"import {{ d as l }} from '../../../{a:x}/{b:x}/{c:x}/{prev:x}'")
            imports.append(f'const {{ d: l }} = require("../../../{a:x}/{b:x}/{c:x}/{prev:x}")')
            fns.append("l")
        txt = "\n".join(imports + [" ".join([
            "const s = 1",
        ] + [
            f"+ {x}" for x in fns
        ])] + [
            # "export const a = s",
            # "export const b = s",
            # "export const c = s",
            # "export const d = s",
            "const a = s",
            "const b = s",
            "const c = s",
            "const d = s",
            "module.exports = { a, b, c, d }"
        ])

        di = f"{args.out}/{a:x}/{b:x}/{c:x}"
        os.makedirs(di, exist_ok=True)
        with open (f"{di}/{d:x}.js", "w") as f:
            f.write(txt)
        

if __name__ == "__main__":
    main()