import json
from functools import reduce
from deepmerge import always_merger

def run(args):
    objects = [json.load(f) for f in args.files]
    merged = reduce(lambda a,b: always_merger.merge(a,b), objects)

    if args.out is None:
        print(json.dumps(merged, indent=2))
    else:
        json.dump(merged, args.out, ensure_ascii=False, indent=2)

