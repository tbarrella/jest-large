import argparse
import itertools
import os

N = 12

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('out')
    args = parser.parse_args()

    with open(f"{args.out}/index.test.js", "w") as f:
        f.write(f"""
const {{ s }} = require("./{N - 1:x}/{N - 1:x}/{N - 1:x}/{N - 1:x}");

describe("sum", () => {{
    it("overflows", () => {{
        expect(s).toEqual(NaN);
    }});
}});
""")

    for a, b, c, d in itertools.product(range(N), repeat=4):
        imports = []
        terms = []
        if a > 0:
            imports.append(f'const {{ s: a }} = require("../../../{a - 1:x}/{b:x}/{c:x}/{d:x}");')
            terms.append("a")
        if b > 0:
            imports.append(f'const {{ s: b }} = require("../../../{a:x}/{b - 1:x}/{c:x}/{d:x}");')
            terms.append("b")
        if c > 0:
            imports.append(f'const {{ s: c }} = require("../../../{a:x}/{b:x}/{c - 1:x}/{d:x}");')
            terms.append("c")
        if d > 0:
            imports.append(f'const {{ s: d }} = require("../../../{a:x}/{b:x}/{c:x}/{d - 1:x}");')
            terms.append("d")
        js = "\n".join(imports + [
            " ".join(["const s = 1"] + [f"+ {x}" for x in terms] + [";"]),
            "module.exports = { s };",
            "",
        ])

        subdir = f"{args.out}/{a:x}/{b:x}/{c:x}"
        os.makedirs(subdir, exist_ok=True)
        with open (f"{subdir}/{d:x}.js", "w") as f:
            f.write(js)
        

if __name__ == "__main__":
    main()
