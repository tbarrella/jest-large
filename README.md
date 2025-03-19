## Repro

```
cd pkg/a
bazel run -- @pnpm --dir $PWD i
bazel run -- @pnpm --dir $PWD test
```

## Jest fails with Bazel

```
bazel test --test_output=streamed //pkg/a:test
```

### Workaround

In pkg/a/BUILD.bazel, uncomment

```
  #
```
