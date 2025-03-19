## Repro

### Setup

```
bazel run //pkg/a:write_gen
```

### Jest without Bazel

```
cd pkg/a
bazel run -- @pnpm --dir $PWD i
time pnpm test

# Repeat with cache
time pnpm test

# Repeat without cache
time pnpm test -- --no-cache
```

### Jest with Bazel

```
bazel test --cache_test_results=no --test_output=streamed //pkg/a:test
```
