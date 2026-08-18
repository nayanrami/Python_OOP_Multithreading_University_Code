"""Lazy processing pipeline using generators."""

def source_records(count: int):
    for i in range(1, count + 1):
        yield {"id": i, "score": (i * 17) % 101}

def passing(records, minimum=40):
    for record in records:
        if record["score"] >= minimum:
            yield record

def project(records):
    for record in records:
        yield record["id"], record["score"]


def main():
    pipeline = project(passing(source_records(15), minimum=60))
    print(list(pipeline))


if __name__ == "__main__":
    main()
